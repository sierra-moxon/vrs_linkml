
# Class: CopyNumber


The absolute count of discrete copies of a MolecularVariation, Feature, SequenceExpression, or a CURIE reference within a system (e.g. genome, cell, etc.).

URI: [GA4GHVRSDefinitions:CopyNumber](GA4GHVRSDefinitionsCopyNumber)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[CURIE]<_id%200..1-++[CopyNumber&#124;type:string;subject:string;copies:string],[CURIE])](https://yuml.me/diagram/nofunky;dir:TB/class/[CURIE]<_id%200..1-++[CopyNumber&#124;type:string;subject:string;copies:string],[CURIE])

## Referenced by Class


## Attributes


### Own

 * [CopyNumber➞_id](CopyNumber__id.md)  <sub>0..1</sub>
     * Description: Variation Id. MUST be unique within document.
     * Range: [CURIE](CURIE.md)
 * [CopyNumber➞type](CopyNumber_type.md)  <sub>1..1</sub>
     * Description: MUST be "CopyNumber"
     * Range: [String](types/String.md)
 * [CopyNumber➞subject](CopyNumber_subject.md)  <sub>1..1</sub>
     * Description: Subject of the Copy Number object
     * Range: [String](types/String.md)
 * [CopyNumber➞copies](CopyNumber_copies.md)  <sub>1..1</sub>
     * Description: The integral number of copies of the subject in a system
     * Range: [String](types/String.md)
