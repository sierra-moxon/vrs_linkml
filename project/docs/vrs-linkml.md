
# GA4GHVRSDefinitions


**metamodel version:** 1.7.0

**version:** None





### Classes

 * [Allele](Allele.md) - The state of a molecule at a Location.
 * [CURIE](CURIE.md) - A [W3C Compact URI](https://www.w3.org/TR/curie/) formatted string. A CURIE string has the structure ``prefix``:``reference``, as defined by the W3C syntax.
 * [ChromosomeLocation](ChromosomeLocation.md) - A Location on a chromosome defined by a species and chromosome name.
 * [ComposedSequenceExpression](ComposedSequenceExpression.md) - An expression of a sequence composed from multiple other  Sequence Expressions  objects. MUST have at least one component that is not a  ref:`LiteralSequenceExpression`. CANNOT be composed from  nested composed sequence expressions.
 * [CopyNumber](CopyNumber.md) - The absolute count of discrete copies of a MolecularVariation, Feature, SequenceExpression, or a CURIE reference within a system (e.g. genome, cell, etc.).
 * [CytobandInterval](CytobandInterval.md) - A contiguous span on a chromosome defined by cytoband features. The span includes the constituent regions described by the start and end cytobands, as well as any intervening regions.
 * [DefiniteRange](DefiniteRange.md) - A bounded, inclusive range of numbers.
 * [DerivedSequenceExpression](DerivedSequenceExpression.md) - An approximate expression of a sequence that is derived from a referenced sequence location. Use of this class indicates that the derived sequence is *approximately equivalent* to the reference indicated, and is typically used for describing large regions in contexts where the use of an approximate sequence is inconsequential.
 * [Feature](Feature.md) - A named entity that can be mapped to a Location. Genes, protein domains, exons, and chromosomes are some examples of common biological entities that may be Features.
 * [Gene](Gene.md) - A reference to a Gene as defined by an authority. For human genes, the use of [hgnc](https://registry.identifiers.org/registry/hgnc) as the gene authority is RECOMMENDED.
 * [Haplotype](Haplotype.md) - A set of non-overlapping Allele members that co-occur on the same molecule.
 * [HumanCytoband](HumanCytoband.md) - A character string representing cytobands derived from the *International System for Human Cytogenomic Nomenclature* (ISCN) [guidelines](http://doi.org/10.1159/isbn.978-3-318-06861-0).
 * [IndefiniteRange](IndefiniteRange.md) - A half-bounded range of numbers represented as a number bound and associated comparator. The bound operator is interpreted as follows: '>=' are all numbers greater than and including `value`, '<=' are all numbers less than and including `value`.
 * [LiteralSequenceExpression](LiteralSequenceExpression.md) - An explicit expression of a Sequence.
 * [Location](Location.md) - A contiguous segment of a biological sequence.
 * [MolecularVariation](MolecularVariation.md) - A variation on a contiguous molecule.
 * [Number](Number.md) - A simple integer value as a VRS class.
 * [RepeatedSequenceExpression](RepeatedSequenceExpression.md) - An expression of a sequence comprised of a tandem repeating subsequence.
 * [Residue](Residue.md) - A character representing a specific residue (i.e., molecular species) or groupings of these ("ambiguity codes"), using [one-letter IUPAC abbreviations](https://en.wikipedia.org/wiki/International_Union_of_Pure_and_Applied_Chemistry#Amino_acid_and_nucleotide_base_codes) for nucleic acids and amino acids.
 * [Sequence](Sequence.md) - A character string of Residues that represents a biological sequence using the conventional sequence order (5’-to-3’ for nucleic acid sequences, and amino-to-carboxyl for amino acid sequences). IUPAC ambiguity codes are permitted in Sequences.
 * [SequenceExpression](SequenceExpression.md) - An expression describing a Sequence.
 * [SequenceInterval](SequenceInterval.md) - A SequenceInterval represents a span on a Sequence. Positions are always represented by contiguous spans using interbase coordinates or coordinate ranges.
 * [SequenceLocation](SequenceLocation.md) - A Location defined by an interval on a referenced Sequence.
 * [SequenceState](SequenceState.md) - DEPRECATED. A Sequence as a State. This is the State class to use for representing "ref-alt" style variation, including SNVs, MNVs, del, ins, and delins. This class is deprecated. Use LiteralSequenceExpression instead.
 * [SimpleInterval](SimpleInterval.md) - DEPRECATED: A SimpleInterval represents a span of sequence. Positions are always represented by contiguous spans using interbase coordinates. This class is deprecated. Use SequenceInterval instead.
 * [SystemicVariation](SystemicVariation.md) - A Variation of multiple molecules in the context of a system, e.g. a genome, sample, or homologous chromosomes.
 * [Text](Text.md) - A free-text definition of variation.
 * [UtilityVariation](UtilityVariation.md) - A collection of Variation subclasses that cannot be constrained to a specific class of biological variation, but are necessary for some applications of VRS.
 * [Variation](Variation.md) - A representation of the state of one or more biomolecules.
 * [VariationSet](VariationSet.md) - An unconstrained set of Variation members.

### Mixins


### Slots

 * [_id](_id.md) - Location Id. MUST be unique within document.
     * [Allele➞_id](Allele__id.md) - Variation Id. MUST be unique within document.
     * [ChromosomeLocation➞_id](ChromosomeLocation__id.md)
     * [CopyNumber➞_id](CopyNumber__id.md) - Variation Id. MUST be unique within document.
     * [Haplotype➞_id](Haplotype__id.md) - Variation Id. MUST be unique within document.
     * [SequenceLocation➞_id](SequenceLocation__id.md)
     * [Text➞_id](Text__id.md) - Variation Id. MUST be unique within document.
     * [VariationSet➞_id](VariationSet__id.md) - Variation Id. MUST be unique within document.
 * [chr](chr.md) - The symbolic chromosome name. For humans, For humans, chromosome names MUST be one of 1..22, X, Y (case-sensitive)
     * [ChromosomeLocation➞chr](ChromosomeLocation_chr.md)
 * [comparator](comparator.md) - MUST be one of "<=" or ">=", indicating which direction the range is indefinite
     * [IndefiniteRange➞comparator](IndefiniteRange_comparator.md)
 * [components](components.md)
     * [ComposedSequenceExpression➞components](ComposedSequenceExpression_components.md)
 * [copies](copies.md) - The integral number of copies of the subject in a system
     * [CopyNumber➞copies](CopyNumber_copies.md)
 * [count](count.md) - The count of repeated units, as an integer or inclusive range
     * [RepeatedSequenceExpression➞count](RepeatedSequenceExpression_count.md)
 * [definition](definition.md) - A textual representation of variation not representable by other subclasses of Variation.
     * [Text➞definition](Text_definition.md)
 * [end](end.md) - The end coordinate
     * [CytobandInterval➞end](CytobandInterval_end.md) - The start cytoband region. MUST specify a region nearer the terminal end (telomere) of the chromosome q-arm than `start`.
     * [SequenceInterval➞end](SequenceInterval_end.md) - The end coordinate or range of the interval. The minimum value of this coordinate or range is 0. MUST represent a coordinate or range greater than the value of `start`.
     * [SimpleInterval➞end](SimpleInterval_end.md)
 * [gene_id](gene_id.md) - A CURIE reference to a Gene concept
     * [Gene➞gene_id](Gene_gene_id.md)
 * [interval](interval.md) - Reference sequence region defined by a SequenceInterval.
     * [ChromosomeLocation➞interval](ChromosomeLocation_interval.md) - The chromosome region defined by a CytobandInterval
     * [SequenceLocation➞interval](SequenceLocation_interval.md)
 * [location](location.md) - The location from which the approximate sequence is derived
     * [Allele➞location](Allele_location.md) - Where Allele is located
     * [DerivedSequenceExpression➞location](DerivedSequenceExpression_location.md)
 * [max](max.md) - The maximum value; inclusive
     * [DefiniteRange➞max](DefiniteRange_max.md)
 * [members](members.md)
     * [Haplotype➞members](Haplotype_members.md)
     * [VariationSet➞members](VariationSet_members.md)
 * [min](min.md) - The minimum value; inclusive
     * [DefiniteRange➞min](DefiniteRange_min.md)
 * [reverse_complement](reverse_complement.md) - A flag indicating if the expressed sequence is the reverse complement of the sequence referred to by `location`
     * [DerivedSequenceExpression➞reverse_complement](DerivedSequenceExpression_reverse_complement.md)
 * [seq_expr](seq_expr.md) - An expression of the repeating subsequence
     * [RepeatedSequenceExpression➞seq_expr](RepeatedSequenceExpression_seq_expr.md)
 * [sequence](sequence.md) - A string of Residues
     * [LiteralSequenceExpression➞sequence](LiteralSequenceExpression_sequence.md) - the literal Sequence expressed
     * [SequenceState➞sequence](SequenceState_sequence.md)
 * [sequence_id](sequence_id.md) - A VRS Computed Identifier for the reference Sequence.
     * [SequenceLocation➞sequence_id](SequenceLocation_sequence_id.md)
 * [species_id](species_id.md) - CURIE representing a species from the [NCBI species taxonomy](https://registry.identifiers.org/registry/taxonomy). Default: "taxonomy:9606" (human)
     * [ChromosomeLocation➞species_id](ChromosomeLocation_species_id.md)
 * [start](start.md) - The start coordinate
     * [CytobandInterval➞start](CytobandInterval_start.md) - The start cytoband region. MUST specify a region nearer the terminal end (telomere) of the chromosome p-arm than `end`.
     * [SequenceInterval➞start](SequenceInterval_start.md) - The start coordinate or range of the interval. The minimum value of this coordinate or range is 0. MUST represent a coordinate or range less than the value of `end`.
     * [SimpleInterval➞start](SimpleInterval_start.md)
 * [state](state.md) - An expression of the sequence state
     * [Allele➞state](Allele_state.md)
 * [subject](subject.md) - Subject of the Copy Number object
     * [CopyNumber➞subject](CopyNumber_subject.md)
 * [type](type.md) - MUST be "SimpleInterval"
     * [Allele➞type](Allele_type.md) - MUST be "Allele"
     * [ChromosomeLocation➞type](ChromosomeLocation_type.md) - MUST be "ChromosomeLocation"
     * [ComposedSequenceExpression➞type](ComposedSequenceExpression_type.md) - MUST be "ComposedSequenceExpression"
     * [CopyNumber➞type](CopyNumber_type.md) - MUST be "CopyNumber"
     * [CytobandInterval➞type](CytobandInterval_type.md) - MUST be "CytobandInterval"
     * [DefiniteRange➞type](DefiniteRange_type.md) - MUST be "DefiniteRange"
     * [DerivedSequenceExpression➞type](DerivedSequenceExpression_type.md) - MUST be "DerivedSequenceExpression"
     * [Gene➞type](Gene_type.md) - MUST be "Gene"
     * [Haplotype➞type](Haplotype_type.md) - MUST be "Haplotype"
     * [IndefiniteRange➞type](IndefiniteRange_type.md) - MUST be "IndefiniteRange"
     * [LiteralSequenceExpression➞type](LiteralSequenceExpression_type.md) - MUST be "LiteralSequenceExpression"
     * [Number➞type](Number_type.md) - MUST be "Number"
     * [RepeatedSequenceExpression➞type](RepeatedSequenceExpression_type.md) - MUST be "RepeatedSequenceExpression"
     * [SequenceInterval➞type](SequenceInterval_type.md) - MUST be "SequenceInterval"
     * [SequenceLocation➞type](SequenceLocation_type.md) - MUST be "SequenceLocation"
     * [SequenceState➞type](SequenceState_type.md) - MUST be "SequenceState"
     * [SimpleInterval➞type](SimpleInterval_type.md)
     * [Text➞type](Text_type.md) - MUST be "Text"
     * [VariationSet➞type](VariationSet_type.md) - MUST be "VariationSet"
 * [value](value.md) - The bounded value; inclusive
     * [IndefiniteRange➞value](IndefiniteRange_value.md)
     * [Number➞value](Number_value.md) - The value represented by Number

### Enums

 * [comparator_options](comparator_options.md)

### Subsets


### Types


#### Built in

 * **Bool**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
