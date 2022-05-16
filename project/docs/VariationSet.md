
# Class: VariationSet


An unconstrained set of Variation members.

URI: [GA4GHVRSDefinitions:VariationSet](GA4GHVRSDefinitionsVariationSet)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[CURIE]<_id%200..1-++[VariationSet&#124;type:string;members:string%20%2B],[CURIE])](https://yuml.me/diagram/nofunky;dir:TB/class/[CURIE]<_id%200..1-++[VariationSet&#124;type:string;members:string%20%2B],[CURIE])

## Referenced by Class


## Attributes


### Own

 * [VariationSet➞_id](VariationSet__id.md)  <sub>0..1</sub>
     * Description: Variation Id. MUST be unique within document.
     * Range: [CURIE](CURIE.md)
 * [VariationSet➞type](VariationSet_type.md)  <sub>1..1</sub>
     * Description: MUST be "VariationSet"
     * Range: [String](types/String.md)
 * [VariationSet➞members](VariationSet_members.md)  <sub>1..\*</sub>
     * Range: [String](types/String.md)
