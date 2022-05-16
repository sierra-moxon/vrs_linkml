
# Class: Haplotype


A set of non-overlapping Allele members that co-occur on the same molecule.

URI: [GA4GHVRSDefinitions:Haplotype](GA4GHVRSDefinitionsHaplotype)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[CURIE]<_id%200..1-++[Haplotype&#124;type:string;members:string%20%2B],[CURIE])](https://yuml.me/diagram/nofunky;dir:TB/class/[CURIE]<_id%200..1-++[Haplotype&#124;type:string;members:string%20%2B],[CURIE])

## Referenced by Class


## Attributes


### Own

 * [Haplotype➞_id](Haplotype__id.md)  <sub>0..1</sub>
     * Description: Variation Id. MUST be unique within document.
     * Range: [CURIE](CURIE.md)
 * [Haplotype➞type](Haplotype_type.md)  <sub>1..1</sub>
     * Description: MUST be "Haplotype"
     * Range: [String](types/String.md)
 * [Haplotype➞members](Haplotype_members.md)  <sub>1..\*</sub>
     * Range: [String](types/String.md)
