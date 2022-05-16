
# Class: Allele


The state of a molecule at a Location.

URI: [GA4GHVRSDefinitions:Allele](GA4GHVRSDefinitionsAllele)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SequenceLocation],[CURIE],[SequenceLocation]<location%201..1-++[Allele&#124;type:string;state:string],[CURIE]<_id%200..1-++[Allele])](https://yuml.me/diagram/nofunky;dir:TB/class/[SequenceLocation],[CURIE],[SequenceLocation]<location%201..1-++[Allele&#124;type:string;state:string],[CURIE]<_id%200..1-++[Allele])

## Referenced by Class


## Attributes


### Own

 * [Allele➞_id](Allele__id.md)  <sub>0..1</sub>
     * Description: Variation Id. MUST be unique within document.
     * Range: [CURIE](CURIE.md)
 * [Allele➞type](Allele_type.md)  <sub>1..1</sub>
     * Description: MUST be "Allele"
     * Range: [String](types/String.md)
 * [Allele➞location](Allele_location.md)  <sub>1..1</sub>
     * Description: Where Allele is located
     * Range: [SequenceLocation](SequenceLocation.md)
 * [Allele➞state](Allele_state.md)  <sub>1..1</sub>
     * Description: An expression of the sequence state
     * Range: [String](types/String.md)
