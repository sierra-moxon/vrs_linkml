
# Class: ChromosomeLocation


A Location on a chromosome defined by a species and chromosome name.

URI: [GA4GHVRSDefinitions:ChromosomeLocation](GA4GHVRSDefinitionsChromosomeLocation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[CytobandInterval],[CytobandInterval]<interval%201..1-++[ChromosomeLocation&#124;type:string;chr:string],[CURIE]<species_id%201..1-++[ChromosomeLocation],[CURIE]<_id%200..1-++[ChromosomeLocation],[CURIE])](https://yuml.me/diagram/nofunky;dir:TB/class/[CytobandInterval],[CytobandInterval]<interval%201..1-++[ChromosomeLocation&#124;type:string;chr:string],[CURIE]<species_id%201..1-++[ChromosomeLocation],[CURIE]<_id%200..1-++[ChromosomeLocation],[CURIE])

## Referenced by Class


## Attributes


### Own

 * [ChromosomeLocation➞_id](ChromosomeLocation__id.md)  <sub>0..1</sub>
     * Description: Location Id. MUST be unique within document.
     * Range: [CURIE](CURIE.md)
 * [ChromosomeLocation➞type](ChromosomeLocation_type.md)  <sub>1..1</sub>
     * Description: MUST be "ChromosomeLocation"
     * Range: [String](types/String.md)
 * [ChromosomeLocation➞species_id](ChromosomeLocation_species_id.md)  <sub>1..1</sub>
     * Description: CURIE representing a species from the [NCBI species taxonomy](https://registry.identifiers.org/registry/taxonomy). Default: "taxonomy:9606" (human)
     * Range: [CURIE](CURIE.md)
 * [ChromosomeLocation➞chr](ChromosomeLocation_chr.md)  <sub>1..1</sub>
     * Description: The symbolic chromosome name. For humans, For humans, chromosome names MUST be one of 1..22, X, Y (case-sensitive)
     * Range: [String](types/String.md)
 * [ChromosomeLocation➞interval](ChromosomeLocation_interval.md)  <sub>1..1</sub>
     * Description: The chromosome region defined by a CytobandInterval
     * Range: [CytobandInterval](CytobandInterval.md)
