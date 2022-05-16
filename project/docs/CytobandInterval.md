
# Class: CytobandInterval


A contiguous span on a chromosome defined by cytoband features. The span includes the constituent regions described by the start and end cytobands, as well as any intervening regions.

URI: [GA4GHVRSDefinitions:CytobandInterval](GA4GHVRSDefinitionsCytobandInterval)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[HumanCytoband],[HumanCytoband]<end%201..1-++[CytobandInterval&#124;type:string],[HumanCytoband]<start%201..1-++[CytobandInterval],[ChromosomeLocation]++-%20interval%201..1>[CytobandInterval],[ChromosomeLocation])](https://yuml.me/diagram/nofunky;dir:TB/class/[HumanCytoband],[HumanCytoband]<end%201..1-++[CytobandInterval&#124;type:string],[HumanCytoband]<start%201..1-++[CytobandInterval],[ChromosomeLocation]++-%20interval%201..1>[CytobandInterval],[ChromosomeLocation])

## Referenced by Class

 *  **[ChromosomeLocation](ChromosomeLocation.md)** *[ChromosomeLocation➞interval](ChromosomeLocation_interval.md)*  <sub>1..1</sub>  **[CytobandInterval](CytobandInterval.md)**

## Attributes


### Own

 * [CytobandInterval➞type](CytobandInterval_type.md)  <sub>1..1</sub>
     * Description: MUST be "CytobandInterval"
     * Range: [String](types/String.md)
 * [CytobandInterval➞start](CytobandInterval_start.md)  <sub>1..1</sub>
     * Description: The start cytoband region. MUST specify a region nearer the terminal end (telomere) of the chromosome p-arm than `end`.
     * Range: [HumanCytoband](HumanCytoband.md)
 * [CytobandInterval➞end](CytobandInterval_end.md)  <sub>1..1</sub>
     * Description: The start cytoband region. MUST specify a region nearer the terminal end (telomere) of the chromosome q-arm than `start`.
     * Range: [HumanCytoband](HumanCytoband.md)
