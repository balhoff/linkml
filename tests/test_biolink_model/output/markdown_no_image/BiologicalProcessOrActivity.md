
# Class: biological process or activity


Either an individual molecular activity, or a collection of causally connected molecular activities in a biological system.

URI: [biolink:BiologicalProcessOrActivity](https://w3id.org/biolink/vocab/BiologicalProcessOrActivity)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[PhysicalEntity],[OntologyClass],[Occurrent],[NamedThing],[MolecularActivity],[PhysicalEntity]<enabled%20by%200..*-%20[BiologicalProcessOrActivity&#124;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[NamedThing]<has%20output%200..*-%20[BiologicalProcessOrActivity],[NamedThing]<has%20input%200..*-%20[BiologicalProcessOrActivity],[BiologicalProcessOrActivity]uses%20-.->[Occurrent],[BiologicalProcessOrActivity]uses%20-.->[OntologyClass],[BiologicalProcessOrActivity]^-[MolecularActivity],[BiologicalProcessOrActivity]^-[BiologicalProcess],[BiologicalEntity]^-[BiologicalProcessOrActivity],[BiologicalProcess],[BiologicalEntity],[Attribute],[Agent])](https://yuml.me/diagram/nofunky;dir:TB/class/[PhysicalEntity],[OntologyClass],[Occurrent],[NamedThing],[MolecularActivity],[PhysicalEntity]<enabled%20by%200..*-%20[BiologicalProcessOrActivity&#124;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[NamedThing]<has%20output%200..*-%20[BiologicalProcessOrActivity],[NamedThing]<has%20input%200..*-%20[BiologicalProcessOrActivity],[BiologicalProcessOrActivity]uses%20-.->[Occurrent],[BiologicalProcessOrActivity]uses%20-.->[OntologyClass],[BiologicalProcessOrActivity]^-[MolecularActivity],[BiologicalProcessOrActivity]^-[BiologicalProcess],[BiologicalEntity]^-[BiologicalProcessOrActivity],[BiologicalProcess],[BiologicalEntity],[Attribute],[Agent])

## Identifier prefixes

 * GO
 * REACT

## Parents

 *  is_a: [BiologicalEntity](BiologicalEntity.md)

## Uses Mixins

 *  mixin: [Occurrent](Occurrent.md) - A processual entity.
 *  mixin: [OntologyClass](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a biolink compatible KG can be considered both instances of biolink classes, and OWL classes in their own right. In general you should not need to use this class directly. Instead, use the appropriate biolink class. For example, for the GO concept of endocytosis (GO:0006897), use bl:BiologicalProcess as the type.

## Children

 * [BiologicalProcess](BiologicalProcess.md) - One or more causally connected executions of molecular functions
 * [MolecularActivity](MolecularActivity.md) - An execution of a molecular function carried out by a gene product or macromolecular complex.

## Referenced by class

 *  **[PhysicalEntity](PhysicalEntity.md)** *[enables](enables.md)*  <sub>0..\*</sub>  **[BiologicalProcessOrActivity](BiologicalProcessOrActivity.md)**

## Attributes


### Own

 * [has input](has_input.md)  <sub>0..\*</sub>
     * Description: holds between a process and a continuant, where the continuant is an input into the process
     * Range: [NamedThing](NamedThing.md)
     * in subsets: (translator_minimal)
 * [has output](has_output.md)  <sub>0..\*</sub>
     * Description: holds between a process and a continuant, where the continuant is an output of the process
     * Range: [NamedThing](NamedThing.md)
     * in subsets: (translator_minimal)
 * [enabled by](enabled_by.md)  <sub>0..\*</sub>
     * Description: holds between a process and a physical entity, where the physical entity executes the process
     * Range: [PhysicalEntity](PhysicalEntity.md)
     * in subsets: (translator_minimal)

### Inherited from biological entity:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     * Range: [String](types/String.md)
     * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>0..1</sub>
     * Description: An IRI for an entity. This is determined by the id using expansion rules.
     * Range: [IriType](types/IriType.md)
     * in subsets: (translator_minimal,samples)
 * [type](type.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for an attribute or entity.
     * Range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal,samples)
 * [description](description.md)  <sub>0..1</sub>
     * Description: a human-readable description of an entity
     * Range: [NarrativeText](types/NarrativeText.md)
     * in subsets: (translator_minimal)
 * [source](source.md)  <sub>0..1</sub>
     * Description: a lightweight analog to the association class 'has provider' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
     * Range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal)
 * [provided by](provided_by.md)  <sub>0..\*</sub>
     * Description: connects an association to the agent (person, organization or group) that provided it
     * Range: [Agent](Agent.md)
 * [has attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: connects any entity to an attribute
     * Range: [Attribute](Attribute.md)
     * in subsets: (samples)
 * [named thing➞category](named_thing_category.md)  <sub>1..\*</sub>
     * Range: [NamedThing](NamedThing.md)
