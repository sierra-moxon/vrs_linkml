
# Class: SequenceState


DEPRECATED. A Sequence as a State. This is the State class to use for representing "ref-alt" style variation, including SNVs, MNVs, del, ins, and delins. This class is deprecated. Use LiteralSequenceExpression instead.

URI: [GA4GHVRSDefinitions:SequenceState](GA4GHVRSDefinitionsSequenceState)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Sequence]<sequence%201..1-++[SequenceState&#124;type:string],[Sequence])](https://yuml.me/diagram/nofunky;dir:TB/class/[Sequence]<sequence%201..1-++[SequenceState&#124;type:string],[Sequence])

## Referenced by Class


## Attributes


### Own

 * [SequenceState➞type](SequenceState_type.md)  <sub>1..1</sub>
     * Description: MUST be "SequenceState"
     * Range: [String](types/String.md)
 * [SequenceState➞sequence](SequenceState_sequence.md)  <sub>1..1</sub>
     * Description: A string of Residues
     * Range: [Sequence](Sequence.md)
