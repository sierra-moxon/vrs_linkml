
# Class: SequenceLocation


A Location defined by an interval on a referenced Sequence.

URI: [GA4GHVRSDefinitions:SequenceLocation](GA4GHVRSDefinitionsSequenceLocation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[CURIE]<sequence_id%201..1-++[SequenceLocation&#124;type:string;interval:string],[CURIE]<_id%200..1-++[SequenceLocation],[Allele]++-%20location%201..1>[SequenceLocation],[DerivedSequenceExpression]++-%20location%201..1>[SequenceLocation],[Allele]++-%20location(i)%201..1>[SequenceLocation],[DerivedSequenceExpression]++-%20location(i)%201..1>[SequenceLocation],[DerivedSequenceExpression],[CURIE],[Allele])](https://yuml.me/diagram/nofunky;dir:TB/class/[CURIE]<sequence_id%201..1-++[SequenceLocation&#124;type:string;interval:string],[CURIE]<_id%200..1-++[SequenceLocation],[Allele]++-%20location%201..1>[SequenceLocation],[DerivedSequenceExpression]++-%20location%201..1>[SequenceLocation],[Allele]++-%20location(i)%201..1>[SequenceLocation],[DerivedSequenceExpression]++-%20location(i)%201..1>[SequenceLocation],[DerivedSequenceExpression],[CURIE],[Allele])

## Referenced by Class

 *  **[Allele](Allele.md)** *[Allele➞location](Allele_location.md)*  <sub>1..1</sub>  **[SequenceLocation](SequenceLocation.md)**
 *  **[DerivedSequenceExpression](DerivedSequenceExpression.md)** *[DerivedSequenceExpression➞location](DerivedSequenceExpression_location.md)*  <sub>1..1</sub>  **[SequenceLocation](SequenceLocation.md)**
 *  **None** *[location](location.md)*  <sub>1..1</sub>  **[SequenceLocation](SequenceLocation.md)**

## Attributes


### Own

 * [SequenceLocation➞_id](SequenceLocation__id.md)  <sub>0..1</sub>
     * Description: Location Id. MUST be unique within document.
     * Range: [CURIE](CURIE.md)
 * [SequenceLocation➞type](SequenceLocation_type.md)  <sub>1..1</sub>
     * Description: MUST be "SequenceLocation"
     * Range: [String](types/String.md)
 * [SequenceLocation➞sequence_id](SequenceLocation_sequence_id.md)  <sub>1..1</sub>
     * Description: A VRS Computed Identifier for the reference Sequence.
     * Range: [CURIE](CURIE.md)
 * [SequenceLocation➞interval](SequenceLocation_interval.md)  <sub>1..1</sub>
     * Description: Reference sequence region defined by a SequenceInterval.
     * Range: [String](types/String.md)
