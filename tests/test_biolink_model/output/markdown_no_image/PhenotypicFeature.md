
# Class: phenotypic feature




URI: [biolink:PhenotypicFeature](https://w3id.org/biolink/vocab/PhenotypicFeature)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[EntityToPhenotypicFeatureAssociationMixin]-%20object%201..1>[PhenotypicFeature&#124;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[PhenotypicFeature]^-[ClinicalFinding],[PhenotypicFeature]^-[BehavioralFeature],[DiseaseOrPhenotypicFeature]^-[PhenotypicFeature],[OrganismTaxon],[NamedThing],[EntityToPhenotypicFeatureAssociationMixin],[DiseaseOrPhenotypicFeature],[ClinicalFinding],[BiologicalEntity],[BehavioralFeature],[Attribute],[Agent])](https://yuml.me/diagram/nofunky;dir:TB/class/[EntityToPhenotypicFeatureAssociationMixin]-%20object%201..1>[PhenotypicFeature&#124;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[PhenotypicFeature]^-[ClinicalFinding],[PhenotypicFeature]^-[BehavioralFeature],[DiseaseOrPhenotypicFeature]^-[PhenotypicFeature],[OrganismTaxon],[NamedThing],[EntityToPhenotypicFeatureAssociationMixin],[DiseaseOrPhenotypicFeature],[ClinicalFinding],[BiologicalEntity],[BehavioralFeature],[Attribute],[Agent])

## Identifier prefixes

 * HP
 * EFO
 * NCIT
 * UMLS
 * MEDDRA
 * MP
 * ZP
 * UPHENO
 * APO
 * FBcv
 * WBPhenotype
 * SNOMEDCT
 * MESH

## Parents

 *  is_a: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) - Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.

## Children

 * [BehavioralFeature](BehavioralFeature.md) - A phenotypic feature which is behavioral in nature.
 * [ClinicalFinding](ClinicalFinding.md) - this category is currently considered broad enough to tag clinical lab measurements and other biological attributes taken as 'clinical traits' with some statistical score, for example, a p value in genetic associations.

## Referenced by class

 *  **[EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md)** *[entity to phenotypic feature association mixin➞object](entity_to_phenotypic_feature_association_mixin_object.md)*  <sub>1..1</sub>  **[PhenotypicFeature](PhenotypicFeature.md)**
 *  **[BiologicalEntity](BiologicalEntity.md)** *[has phenotype](has_phenotype.md)*  <sub>0..\*</sub>  **[PhenotypicFeature](PhenotypicFeature.md)**

## Attributes


### Inherited from disease or phenotypic feature:

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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | sign |
|  | | symptom |
|  | | phenotype |
|  | | trait |
|  | | endophenotype |
| **In Subsets:** | | model_organism_database |
| **Exact Mappings:** | | UPHENO:0001001 |
|  | | SIO:010056 |
|  | | WIKIDATA:Q104053 |
| **Narrow Mappings:** | | UMLSSC:T184 |
|  | | UMLSST:sosy |
|  | | WIKIDATA:Q169872 |
|  | | WIKIDATA:Q25203551 |

