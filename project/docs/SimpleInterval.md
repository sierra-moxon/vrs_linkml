
# Class: SimpleInterval


DEPRECATED: A SimpleInterval represents a span of sequence. Positions are always represented by contiguous spans using interbase coordinates. This class is deprecated. Use SequenceInterval instead.

URI: [GA4GHVRSDefinitions:SimpleInterval](GA4GHVRSDefinitionsSimpleInterval)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SimpleInterval&#124;type:string;start:integer;end:integer])](https://yuml.me/diagram/nofunky;dir:TB/class/[SimpleInterval&#124;type:string;start:integer;end:integer])

## Referenced by Class


## Attributes


### Own

 * [SimpleInterval➞type](SimpleInterval_type.md)  <sub>1..1</sub>
     * Description: MUST be "SimpleInterval"
     * Range: [String](types/String.md)
 * [SimpleInterval➞start](SimpleInterval_start.md)  <sub>1..1</sub>
     * Description: The start coordinate
     * Range: [Integer](types/Integer.md)
 * [SimpleInterval➞end](SimpleInterval_end.md)  <sub>1..1</sub>
     * Description: The end coordinate
     * Range: [Integer](types/Integer.md)
