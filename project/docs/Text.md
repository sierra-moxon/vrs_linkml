
# Class: Text


A free-text definition of variation.

URI: [GA4GHVRSDefinitions:Text](GA4GHVRSDefinitionsText)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[CURIE]<_id%200..1-++[Text&#124;type:string;definition:string],[CURIE])](https://yuml.me/diagram/nofunky;dir:TB/class/[CURIE]<_id%200..1-++[Text&#124;type:string;definition:string],[CURIE])

## Referenced by Class


## Attributes


### Own

 * [Text➞_id](Text__id.md)  <sub>0..1</sub>
     * Description: Variation Id. MUST be unique within document.
     * Range: [CURIE](CURIE.md)
 * [Text➞type](Text_type.md)  <sub>1..1</sub>
     * Description: MUST be "Text"
     * Range: [String](types/String.md)
 * [Text➞definition](Text_definition.md)  <sub>1..1</sub>
     * Description: A textual representation of variation not representable by other subclasses of Variation.
     * Range: [String](types/String.md)
