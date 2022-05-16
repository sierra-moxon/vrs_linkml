
# Class: SequenceInterval


A SequenceInterval represents a span on a Sequence. Positions are always represented by contiguous spans using interbase coordinates or coordinate ranges.

URI: [GA4GHVRSDefinitions:SequenceInterval](GA4GHVRSDefinitionsSequenceInterval)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SequenceInterval&#124;type:string;start:integer;end:integer])](https://yuml.me/diagram/nofunky;dir:TB/class/[SequenceInterval&#124;type:string;start:integer;end:integer])

## Referenced by Class


## Attributes


### Own

 * [SequenceInterval➞type](SequenceInterval_type.md)  <sub>1..1</sub>
     * Description: MUST be "SequenceInterval"
     * Range: [String](types/String.md)
 * [SequenceInterval➞start](SequenceInterval_start.md)  <sub>1..1</sub>
     * Description: The start coordinate or range of the interval. The minimum value of this coordinate or range is 0. MUST represent a coordinate or range less than the value of `end`.
     * Range: [Integer](types/Integer.md)
 * [SequenceInterval➞end](SequenceInterval_end.md)  <sub>1..1</sub>
     * Description: The end coordinate or range of the interval. The minimum value of this coordinate or range is 0. MUST represent a coordinate or range greater than the value of `start`.
     * Range: [Integer](types/Integer.md)
