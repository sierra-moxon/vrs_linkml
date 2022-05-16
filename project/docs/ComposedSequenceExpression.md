
# Class: ComposedSequenceExpression


An expression of a sequence composed from multiple other  Sequence Expressions  objects. MUST have at least one component that is not a  ref:`LiteralSequenceExpression`. CANNOT be composed from  nested composed sequence expressions.

URI: [GA4GHVRSDefinitions:ComposedSequenceExpression](GA4GHVRSDefinitionsComposedSequenceExpression)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ComposedSequenceExpression&#124;type:string;components:string%20%2B])](https://yuml.me/diagram/nofunky;dir:TB/class/[ComposedSequenceExpression&#124;type:string;components:string%20%2B])

## Referenced by Class


## Attributes


### Own

 * [ComposedSequenceExpression➞type](ComposedSequenceExpression_type.md)  <sub>1..1</sub>
     * Description: MUST be "ComposedSequenceExpression"
     * Range: [String](types/String.md)
 * [ComposedSequenceExpression➞components](ComposedSequenceExpression_components.md)  <sub>1..\*</sub>
     * Range: [String](types/String.md)
