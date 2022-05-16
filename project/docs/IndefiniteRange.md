
# Class: IndefiniteRange


A half-bounded range of numbers represented as a number bound and associated comparator. The bound operator is interpreted as follows: '>=' are all numbers greater than and including `value`, '<=' are all numbers less than and including `value`.

URI: [GA4GHVRSDefinitions:IndefiniteRange](GA4GHVRSDefinitionsIndefiniteRange)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[IndefiniteRange&#124;type:string;value:float;comparator:comparator_options])](https://yuml.me/diagram/nofunky;dir:TB/class/[IndefiniteRange&#124;type:string;value:float;comparator:comparator_options])

## Referenced by Class


## Attributes


### Own

 * [IndefiniteRange➞type](IndefiniteRange_type.md)  <sub>1..1</sub>
     * Description: MUST be "IndefiniteRange"
     * Range: [String](types/String.md)
 * [IndefiniteRange➞value](IndefiniteRange_value.md)  <sub>1..1</sub>
     * Description: The bounded value; inclusive
     * Range: [Float](types/Float.md)
 * [IndefiniteRange➞comparator](IndefiniteRange_comparator.md)  <sub>1..1</sub>
     * Description: MUST be one of "<=" or ">=", indicating which direction the range is indefinite
     * Range: [comparator_options](comparator_options.md)
