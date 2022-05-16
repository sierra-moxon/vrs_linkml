
# Class: DerivedSequenceExpression


An approximate expression of a sequence that is derived from a referenced sequence location. Use of this class indicates that the derived sequence is *approximately equivalent* to the reference indicated, and is typically used for describing large regions in contexts where the use of an approximate sequence is inconsequential.

URI: [GA4GHVRSDefinitions:DerivedSequenceExpression](GA4GHVRSDefinitionsDerivedSequenceExpression)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SequenceLocation],[SequenceLocation]<location%201..1-++[DerivedSequenceExpression&#124;type:string;reverse_complement:boolean])](https://yuml.me/diagram/nofunky;dir:TB/class/[SequenceLocation],[SequenceLocation]<location%201..1-++[DerivedSequenceExpression&#124;type:string;reverse_complement:boolean])

## Referenced by Class


## Attributes


### Own

 * [DerivedSequenceExpression➞type](DerivedSequenceExpression_type.md)  <sub>1..1</sub>
     * Description: MUST be "DerivedSequenceExpression"
     * Range: [String](types/String.md)
 * [DerivedSequenceExpression➞location](DerivedSequenceExpression_location.md)  <sub>1..1</sub>
     * Description: The location from which the approximate sequence is derived
     * Range: [SequenceLocation](SequenceLocation.md)
 * [DerivedSequenceExpression➞reverse_complement](DerivedSequenceExpression_reverse_complement.md)  <sub>1..1</sub>
     * Description: A flag indicating if the expressed sequence is the reverse complement of the sequence referred to by `location`
     * Range: [Boolean](types/Boolean.md)
