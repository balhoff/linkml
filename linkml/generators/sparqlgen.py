import os
from collections import defaultdict
from pathlib import Path
from typing import Union, TextIO, Optional, cast, Dict, List
import logging

import click
from jinja2 import Template
from linkml_runtime.utils.schemaview import SchemaView
from rdflib import Graph, URIRef, RDF, OWL, Literal, BNode
from rdflib.collection import Collection
from rdflib.namespace import RDFS, SKOS
from rdflib.plugin import plugins as rdflib_plugins, Parser as rdflib_Parser

from linkml import LOCAL_METAMODEL_YAML_FILE, METAMODEL_NAMESPACE_NAME, METAMODEL_NAMESPACE, METAMODEL_YAML_URI, META_BASE_URI
from linkml_runtime.linkml_model.meta import ClassDefinitionName, SchemaDefinition, ClassDefinition, SlotDefinitionName, \
    TypeDefinitionName, SlotDefinition, TypeDefinition, Element, EnumDefinitionName, Prefix
from linkml_runtime.utils.formatutils import camelcase, underscore
from linkml.utils.generator import Generator, shared_arguments
from linkml.utils.schemaloader import SchemaLoader

template="""
{% for pfxn, pfx in schema.prefixes.items() -%}
PREFIX {{pfxn}}: <{{pfx.prefix_reference}}>
{% endfor %}

{% for cn, c in schema.classes.items() if not c.mixin and not c.abstract %}

## --
## Checks for {{ cn }}
## --

# @CHECK permitted_{{cn}}
SELECT ?g ?s ?p WHERE {
 GRAPH ?g {
  ?s rdf:type {{ schema_view.get_uri(cn) }} ;
     ?p ?o .
  FILTER ( ?p NOT IN (
   {% for sn in schema_view.class_slots(cn) -%}
   {{ schema_view.get_uri(schema_view.get_slot(sn, attributes=True)) }},
   {% endfor -%}
   rdf:type ))
 }
 {{ extra }}
} {{ limit }}


{% for slot in schema_view.class_induced_slots(cn) -%}

{% if slot.required %}
# @CHECK required_{{cn}}_{{slot.name}}
SELECT
  ?check
  ?graph
  ?subject
  ?predicate WHERE {
 GRAPH ?graph {
  ?subject rdf:type {{ schema_view.get_uri(cn) }} .
  FILTER NOT EXISTS { ?subject  {{ schema_view.get_uri(slot) }} ?o  }
 }
 VALUES ?check { linkml:required }
 VALUES ?predicate { {{schema_view.get_uri(slot)}} }
 {{ extra }}
}  {{ limit }}
{% endif %}

{% if slot.range in schema_view.all_class() %}
# @CHECK object_range_{{cn}}_{{slot.name}}
SELECT
  ?check
  ?graph
  ?subject
  ?predicate
  ?object
WHERE {
 GRAPH ?graph {
  ?subject rdf:type {{ schema_view.get_uri(cn) }} ;
     ?predicate ?object .
  FILTER NOT EXISTS {
    ?object rdf:type ?otype .
    FILTER ( ?otype IN (
      {% for a in schema_view.class_descendants(slot.range) -%}
      {{ schema_view.get_uri(a) }}
      {{ ", " if not loop.last else "" }}
      {% endfor -%} ))
  }
 }
 VALUES ?check { linkml:range }
 VALUES ?predicate { {{ schema_view.get_uri(slot) }}  }
 {{ extra }}
}  {{ limit }}
{% endif %}

{%- endfor %}


## -- End of checks for {{ cn }}
{% endfor %}
"""

x="""
{% for sn in schema_view.class_slots(c.name) %}
     {{ schema.slots[sn].slot_uri }}
   {% endfor %}
"""

def materialize_schema(schemaview: SchemaView):
    schema = schemaview.schema
    if 'rdf' not in schema.prefixes:
        schema.prefixes['rdf'] = Prefix('rdf', str(RDF.uri))
    for scn in schemaview.imports_closure():
        for pfxn, pfx in schemaview.schema_map[scn].prefixes.items():
            if pfxn not in schema:
                schema.prefixes[pfxn] = pfx
    for cn, c in schemaview.all_class().items():
        for a in list(c.attributes.values()):
            schema.slots[a.name] = a
            c.slots.append(a.name)
            del c.attributes[a.name]
    schemaview.set_modified()
    for cn, c in schemaview.all_class().items():
        for s in schemaview.class_induced_slots(cn):
            if s.name not in c.slots:
                c.slots.append(s.name)
            c.slot_usage[s.name] = s
            s.slot_uri = schemaview.get_uri(s)

class SparqlGenerator(Generator):
    generatorname = os.path.basename(__file__)
    valid_formats = ['sparql']
    visit_all_class_slots = False

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition],
                 format: str = valid_formats[0],
                 named_graphs: List[str] = None,
                 limit: int = None,
                 **kwargs) -> None:
        self.sourcefile = schema
        self.schemaview = SchemaView(schema)
        self.schema = self.schemaview.schema
        schemaview = self.schemaview
        schema = self.schema
        self.sparql = None
        materialize_schema(schemaview)
        queries = self.generate_sparql(named_graphs=named_graphs, limit=limit)
        self.queries = queries

    def generate_sparql(self, named_graphs=None, limit: int = None):
        template_obj = Template(template)
        extra = ""
        if named_graphs is not None:
            extra += f'FILTER( ?graph in ( {",".join(named_graphs)} ))'
        print(f'NGS = {named_graphs} // extra={extra}')
        if limit is not None and isinstance(limit, int):
            limit = f'LIMIT {limit}'
        else:
            limit = ""
        sparql = template_obj.render(schema_view=self.schemaview, schema=self.schema, limit=limit, extra=extra)
        self.sparql = sparql
        queries = self.split_sparql(sparql)
        return queries

    def serialize(self, directory=None) -> str:
        if directory is not None:
            Path(directory).mkdir(parents=True, exist_ok=True)
            for qn, q in self.queries.items():
                qpath = os.path.join(directory, f'{qn}.rq')
                with open(qpath, 'w') as stream:
                    stream.write(q)
        return self.sparql

    def split_sparql(self, sparql: str) -> Dict[str,str]:
        lines = sparql.split("\n")
        prolog = ""
        queries = defaultdict(str)
        q = None
        for line in lines:
            if line.startswith('# @'):
                q = underscore(line.replace('# @', ''))
                queries[q] = prolog + '\n'
            elif q is None:
                if line.lower().startswith('prefix'):
                    prolog += line + "\n"
            else:
                queries[q] += line + "\n"
        return queries

@shared_arguments(SparqlGenerator)
@click.command()
@click.option("--dir", "-d", help="Output directory")
def cli(yamlfile, dir, **kwargs):
    """ Generate SPARQL queries for validation """
    SparqlGenerator(yamlfile, **kwargs).serialize(directory=dir)


if __name__ == '__main__':
    cli()



