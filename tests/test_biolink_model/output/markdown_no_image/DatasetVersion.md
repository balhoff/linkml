
# Class: dataset version


an item that holds version level information about a dataset.

URI: [biolink:DatasetVersion](https://w3id.org/biolink/vocab/DatasetVersion)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[InformationContentEntity],[DatasetDistribution]<has%20distribution%200..1-%20[DatasetVersion&#124;ingest_date:string%20%3F;license(i):string%20%3F;rights(i):string%20%3F;format(i):string%20%3F;creation_date(i):date%20%3F;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[Dataset]<has%20dataset%200..1-%20[DatasetVersion],[InformationContentEntity]^-[DatasetVersion],[DatasetDistribution],[Dataset],[Attribute],[Agent])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[InformationContentEntity],[DatasetDistribution]<has%20distribution%200..1-%20[DatasetVersion&#124;ingest_date:string%20%3F;license(i):string%20%3F;rights(i):string%20%3F;format(i):string%20%3F;creation_date(i):date%20%3F;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[Dataset]<has%20dataset%200..1-%20[DatasetVersion],[InformationContentEntity]^-[DatasetVersion],[DatasetDistribution],[Dataset],[Attribute],[Agent])

## Parents

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - a piece of information that typically describes some topic of discourse or is used as support.

## Referenced by class


## Attributes


### Own

 * [has dataset](has_dataset.md)  <sub>0..1</sub>
     * Range: [Dataset](Dataset.md)
 * [ingest date](ingest_date.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [has distribution](has_distribution.md)  <sub>0..1</sub>
     * Range: [DatasetDistribution](DatasetDistribution.md)

### Inherited from information content entity:

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
 * [license](license.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [rights](rights.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [format](format.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [creation date](creation_date.md)  <sub>0..1</sub>
     * Description: date on which an entity was created. This can be applied to nodes or edges
     * Range: [Date](types/Date.md)
