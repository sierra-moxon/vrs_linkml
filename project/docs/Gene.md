
# Class: Gene


A reference to a Gene as defined by an authority. For human genes, the use of [hgnc](https://registry.identifiers.org/registry/hgnc) as the gene authority is RECOMMENDED.

URI: [GA4GHVRSDefinitions:Gene](GA4GHVRSDefinitionsGene)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[CURIE]<gene_id%201..1-++[Gene&#124;type:string],[CURIE])](https://yuml.me/diagram/nofunky;dir:TB/class/[CURIE]<gene_id%201..1-++[Gene&#124;type:string],[CURIE])

## Referenced by Class


## Attributes


### Own

 * [Gene➞type](Gene_type.md)  <sub>1..1</sub>
     * Description: MUST be "Gene"
     * Range: [String](types/String.md)
 * [Gene➞gene_id](Gene_gene_id.md)  <sub>1..1</sub>
     * Description: A CURIE reference to a Gene concept
     * Range: [CURIE](CURIE.md)
