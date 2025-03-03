# Slots

Slots operate the same way as "fields" in traditional object languages and the same ways as "columns" in spreadsheets and relational databases.

If you have a JSON object that is conformant to a LinkML schema, then
the keys for that object must correspond to slots in the schema, that
are applicable to that class.

for example, if we have an object instantiating a Person class:

```json
{"id": "PERSON001",
 "name": "....",
 "email": "....",
 ...
```

then `id`, `email`, `name` should all be valid slots

If we have tabular data

|id|name|email|
|---|---|---|
|PERSON0001|...|...|

then the same constraints hold.

## ranges

Each slot must have a [range](https://w3id.org/linkml/range) - if this is not declared explicitly, then [default_range](https://w3id.org/linkml/default_range) is used.

The range must be one of:

 * A [ClassDefinition](https://w3id.org/linkml/ClassDefinition)
 * A [SlotDefinition](https://w3id.org/linkml/SlotDefinition)
 * An [EnumDefinition](https://w3id.org/linkml/EnumDefinition)

## slot_usage

The [slot_usage](https://w3id.org/linkml/slot_usage) slot can be used to specify how a particular slot ought to be used in a class.

For example, imagine a schema with a generic "Relationship" class:

```yaml
  Relationship:
    slots:
      - started_at_time
      - ended_at_time
      - related_to
      - type
```

with subtypes such as `FamilialRelationship`, `BusinessRelationship`, etc

we can use `slot_usage` to constrain the meaning of more generic slots such as `type` and `related to`:

```yaml
  FamilialRelationship:
    is_a: Relationship
    slot_usage:
      type:
        range: FamilialRelationshipType
        required: true
      related to:
        range: Person
        required: true
```        

## Slot cardinality

### multivalued

The [multivalued](https://w3id.org/linkml/multivalued) indicates that the range of the slot is a list


### required

The [required](https://w3id.org/linkml/required) slot can be used to define whether a slot is required.

When a slot is declared as required, any class that uses that slot must have a value for that slot.

### recommended

The [recommended](https://w3id.org/linkml/recommended) slot can be used to define whether a slot is recommended.

If data is missing a recommended slot, it is still considered valid. However, validators may choose to issue warnings.



## inverse

The `inverse` slot can be used to specify the inverse predicate of a given predicate slot relationship.

```yaml
  affects:
    is_a: related to
    description: >-
      describes an entity that has a direct affect on the state or quality
      of another existing entity. Use of the 'affects' predicate implies that
      the affected entity already exists, unlike predicates such as
      'affects risk for' and 'prevents, where the outcome is something
      that may or may not come to be.
    inverse: affected by
    in_subset:
      - translator_minimal
```
