# Auto generated from vrs-linkml.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-05-16T13:34:34
# Schema: GA4GHVRSDefinitions
#
# id: GA4GHVRSDefinitions
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Float, Integer, String
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
GA4GHVRSDEFINITIONS = CurieNamespace('GA4GHVRSDefinitions', 'GA4GHVRSDefinitions')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = GA4GHVRSDEFINITIONS


# Types

# Class references



class Variation(YAMLRoot):
    """
    A representation of the state of one or more biomolecules.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.Variation
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:Variation"
    class_name: ClassVar[str] = "Variation"
    class_model_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.Variation


class MolecularVariation(YAMLRoot):
    """
    A variation on a contiguous molecule.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.MolecularVariation
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:MolecularVariation"
    class_name: ClassVar[str] = "MolecularVariation"
    class_model_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.MolecularVariation


class UtilityVariation(YAMLRoot):
    """
    A collection of Variation subclasses that cannot be constrained to a specific class of biological variation, but
    are necessary for some applications of VRS.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.UtilityVariation
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:UtilityVariation"
    class_name: ClassVar[str] = "UtilityVariation"
    class_model_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.UtilityVariation


class SystemicVariation(YAMLRoot):
    """
    A Variation of multiple molecules in the context of a system, e.g. a genome, sample, or homologous chromosomes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.SystemicVariation
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:SystemicVariation"
    class_name: ClassVar[str] = "SystemicVariation"
    class_model_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.SystemicVariation


@dataclass
class Allele(YAMLRoot):
    """
    The state of a molecule at a Location.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.Allele
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:Allele"
    class_name: ClassVar[str] = "Allele"
    class_model_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.Allele

    type: str = None
    location: Union[dict, "SequenceLocation"] = None
    state: str = None
    _id: Optional[Union[dict, "CURIE"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.location):
            self.MissingRequiredField("location")
        if not isinstance(self.location, SequenceLocation):
            self.location = SequenceLocation(**as_dict(self.location))

        if self._is_empty(self.state):
            self.MissingRequiredField("state")
        if not isinstance(self.state, str):
            self.state = str(self.state)

        if self._id is not None and not isinstance(self._id, CURIE):
            self._id = CURIE()

        super().__post_init__(**kwargs)


@dataclass
class Haplotype(YAMLRoot):
    """
    A set of non-overlapping Allele members that co-occur on the same molecule.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.Haplotype
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:Haplotype"
    class_name: ClassVar[str] = "Haplotype"
    class_model_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.Haplotype

    type: str = None
    members: Union[str, List[str]] = None
    _id: Optional[Union[dict, "CURIE"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.members):
            self.MissingRequiredField("members")
        if not isinstance(self.members, list):
            self.members = [self.members] if self.members is not None else []
        self.members = [v if isinstance(v, str) else str(v) for v in self.members]

        if self._id is not None and not isinstance(self._id, CURIE):
            self._id = CURIE()

        super().__post_init__(**kwargs)


@dataclass
class Text(YAMLRoot):
    """
    A free-text definition of variation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.Text
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:Text"
    class_name: ClassVar[str] = "Text"
    class_model_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.Text

    type: str = None
    definition: str = None
    _id: Optional[Union[dict, "CURIE"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.definition):
            self.MissingRequiredField("definition")
        if not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self._id is not None and not isinstance(self._id, CURIE):
            self._id = CURIE()

        super().__post_init__(**kwargs)


@dataclass
class VariationSet(YAMLRoot):
    """
    An unconstrained set of Variation members.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.VariationSet
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:VariationSet"
    class_name: ClassVar[str] = "VariationSet"
    class_model_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.VariationSet

    type: str = None
    members: Union[str, List[str]] = None
    _id: Optional[Union[dict, "CURIE"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.members):
            self.MissingRequiredField("members")
        if not isinstance(self.members, list):
            self.members = [self.members] if self.members is not None else []
        self.members = [v if isinstance(v, str) else str(v) for v in self.members]

        if self._id is not None and not isinstance(self._id, CURIE):
            self._id = CURIE()

        super().__post_init__(**kwargs)


@dataclass
class CopyNumber(YAMLRoot):
    """
    The absolute count of discrete copies of a MolecularVariation, Feature, SequenceExpression, or a CURIE reference
    within a system (e.g. genome, cell, etc.).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.CopyNumber
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:CopyNumber"
    class_name: ClassVar[str] = "CopyNumber"
    class_model_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.CopyNumber

    type: str = None
    subject: str = None
    copies: str = None
    _id: Optional[Union[dict, "CURIE"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, str):
            self.subject = str(self.subject)

        if self._is_empty(self.copies):
            self.MissingRequiredField("copies")
        if not isinstance(self.copies, str):
            self.copies = str(self.copies)

        if self._id is not None and not isinstance(self._id, CURIE):
            self._id = CURIE()

        super().__post_init__(**kwargs)


class Location(YAMLRoot):
    """
    A contiguous segment of a biological sequence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.Location
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:Location"
    class_name: ClassVar[str] = "Location"
    class_model_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.Location


@dataclass
class ChromosomeLocation(YAMLRoot):
    """
    A Location on a chromosome defined by a species and chromosome name.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.ChromosomeLocation
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:ChromosomeLocation"
    class_name: ClassVar[str] = "ChromosomeLocation"
    class_model_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.ChromosomeLocation

    type: str = None
    species_id: Union[dict, "CURIE"] = None
    chr: str = None
    interval: Union[dict, "CytobandInterval"] = None
    _id: Optional[Union[dict, "CURIE"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.species_id):
            self.MissingRequiredField("species_id")
        if not isinstance(self.species_id, CURIE):
            self.species_id = CURIE()

        if self._is_empty(self.chr):
            self.MissingRequiredField("chr")
        if not isinstance(self.chr, str):
            self.chr = str(self.chr)

        if self._is_empty(self.interval):
            self.MissingRequiredField("interval")
        if not isinstance(self.interval, CytobandInterval):
            self.interval = CytobandInterval(**as_dict(self.interval))

        if self._id is not None and not isinstance(self._id, CURIE):
            self._id = CURIE()

        super().__post_init__(**kwargs)


@dataclass
class SequenceLocation(YAMLRoot):
    """
    A Location defined by an interval on a referenced Sequence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.SequenceLocation
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:SequenceLocation"
    class_name: ClassVar[str] = "SequenceLocation"
    class_model_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.SequenceLocation

    type: str = None
    sequence_id: Union[dict, "CURIE"] = None
    interval: str = None
    _id: Optional[Union[dict, "CURIE"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.sequence_id):
            self.MissingRequiredField("sequence_id")
        if not isinstance(self.sequence_id, CURIE):
            self.sequence_id = CURIE()

        if self._is_empty(self.interval):
            self.MissingRequiredField("interval")
        if not isinstance(self.interval, str):
            self.interval = str(self.interval)

        if self._id is not None and not isinstance(self._id, CURIE):
            self._id = CURIE()

        super().__post_init__(**kwargs)


@dataclass
class SequenceInterval(YAMLRoot):
    """
    A SequenceInterval represents a span on a Sequence. Positions are always represented by contiguous spans using
    interbase coordinates or coordinate ranges.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.SequenceInterval
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:SequenceInterval"
    class_name: ClassVar[str] = "SequenceInterval"
    class_model_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.SequenceInterval

    type: str = None
    start: int = None
    end: int = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.start):
            self.MissingRequiredField("start")
        if not isinstance(self.start, int):
            self.start = int(self.start)

        if self._is_empty(self.end):
            self.MissingRequiredField("end")
        if not isinstance(self.end, int):
            self.end = int(self.end)

        super().__post_init__(**kwargs)


@dataclass
class CytobandInterval(YAMLRoot):
    """
    A contiguous span on a chromosome defined by cytoband features. The span includes the constituent regions
    described by the start and end cytobands, as well as any intervening regions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.CytobandInterval
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:CytobandInterval"
    class_name: ClassVar[str] = "CytobandInterval"
    class_model_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.CytobandInterval

    type: str = None
    start: Union[dict, "HumanCytoband"] = None
    end: Union[dict, "HumanCytoband"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.start):
            self.MissingRequiredField("start")
        if not isinstance(self.start, HumanCytoband):
            self.start = HumanCytoband()

        if self._is_empty(self.end):
            self.MissingRequiredField("end")
        if not isinstance(self.end, HumanCytoband):
            self.end = HumanCytoband()

        super().__post_init__(**kwargs)


class SequenceExpression(YAMLRoot):
    """
    An expression describing a Sequence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.SequenceExpression
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:SequenceExpression"
    class_name: ClassVar[str] = "SequenceExpression"
    class_model_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.SequenceExpression


@dataclass
class LiteralSequenceExpression(YAMLRoot):
    """
    An explicit expression of a Sequence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.LiteralSequenceExpression
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:LiteralSequenceExpression"
    class_name: ClassVar[str] = "LiteralSequenceExpression"
    class_model_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.LiteralSequenceExpression

    type: str = None
    sequence: Union[dict, "Sequence"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.sequence):
            self.MissingRequiredField("sequence")
        if not isinstance(self.sequence, Sequence):
            self.sequence = Sequence()

        super().__post_init__(**kwargs)


@dataclass
class DerivedSequenceExpression(YAMLRoot):
    """
    An approximate expression of a sequence that is derived from a referenced sequence location. Use of this class
    indicates that the derived sequence is *approximately equivalent* to the reference indicated, and is typically
    used for describing large regions in contexts where the use of an approximate sequence is inconsequential.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.DerivedSequenceExpression
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:DerivedSequenceExpression"
    class_name: ClassVar[str] = "DerivedSequenceExpression"
    class_model_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.DerivedSequenceExpression

    type: str = None
    location: Union[dict, SequenceLocation] = None
    reverse_complement: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.location):
            self.MissingRequiredField("location")
        if not isinstance(self.location, SequenceLocation):
            self.location = SequenceLocation(**as_dict(self.location))

        if self._is_empty(self.reverse_complement):
            self.MissingRequiredField("reverse_complement")
        if not isinstance(self.reverse_complement, Bool):
            self.reverse_complement = Bool(self.reverse_complement)

        super().__post_init__(**kwargs)


@dataclass
class RepeatedSequenceExpression(YAMLRoot):
    """
    An expression of a sequence comprised of a tandem repeating subsequence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.RepeatedSequenceExpression
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:RepeatedSequenceExpression"
    class_name: ClassVar[str] = "RepeatedSequenceExpression"
    class_model_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.RepeatedSequenceExpression

    type: str = None
    seq_expr: str = None
    count: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.seq_expr):
            self.MissingRequiredField("seq_expr")
        if not isinstance(self.seq_expr, str):
            self.seq_expr = str(self.seq_expr)

        if self._is_empty(self.count):
            self.MissingRequiredField("count")
        if not isinstance(self.count, str):
            self.count = str(self.count)

        super().__post_init__(**kwargs)


@dataclass
class ComposedSequenceExpression(YAMLRoot):
    """
    An expression of a sequence composed from multiple other Sequence Expressions objects. MUST have at least one
    component that is not a ref:`LiteralSequenceExpression`. CANNOT be composed from nested composed sequence
    expressions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.ComposedSequenceExpression
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:ComposedSequenceExpression"
    class_name: ClassVar[str] = "ComposedSequenceExpression"
    class_model_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.ComposedSequenceExpression

    type: str = None
    components: Union[str, List[str]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.components):
            self.MissingRequiredField("components")
        if not isinstance(self.components, list):
            self.components = [self.components] if self.components is not None else []
        self.components = [v if isinstance(v, str) else str(v) for v in self.components]

        super().__post_init__(**kwargs)


class Feature(YAMLRoot):
    """
    A named entity that can be mapped to a Location. Genes, protein domains, exons, and chromosomes are some examples
    of common biological entities that may be Features.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.Feature
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:Feature"
    class_name: ClassVar[str] = "Feature"
    class_model_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.Feature


@dataclass
class Gene(YAMLRoot):
    """
    A reference to a Gene as defined by an authority. For human genes, the use of
    [hgnc](https://registry.identifiers.org/registry/hgnc) as the gene authority is RECOMMENDED.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.Gene
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:Gene"
    class_name: ClassVar[str] = "Gene"
    class_model_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.Gene

    type: str = None
    gene_id: Union[dict, "CURIE"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.gene_id):
            self.MissingRequiredField("gene_id")
        if not isinstance(self.gene_id, CURIE):
            self.gene_id = CURIE()

        super().__post_init__(**kwargs)


@dataclass
class Number(YAMLRoot):
    """
    A simple integer value as a VRS class.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.Number
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:Number"
    class_name: ClassVar[str] = "Number"
    class_model_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.Number

    type: str = None
    value: int = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, int):
            self.value = int(self.value)

        super().__post_init__(**kwargs)


@dataclass
class DefiniteRange(YAMLRoot):
    """
    A bounded, inclusive range of numbers.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.DefiniteRange
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:DefiniteRange"
    class_name: ClassVar[str] = "DefiniteRange"
    class_model_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.DefiniteRange

    type: str = None
    min: float = None
    max: float = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.min):
            self.MissingRequiredField("min")
        if not isinstance(self.min, float):
            self.min = float(self.min)

        if self._is_empty(self.max):
            self.MissingRequiredField("max")
        if not isinstance(self.max, float):
            self.max = float(self.max)

        super().__post_init__(**kwargs)


@dataclass
class IndefiniteRange(YAMLRoot):
    """
    A half-bounded range of numbers represented as a number bound and associated comparator. The bound operator is
    interpreted as follows: '>=' are all numbers greater than and including `value`, '<=' are all numbers less than
    and including `value`.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.IndefiniteRange
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:IndefiniteRange"
    class_name: ClassVar[str] = "IndefiniteRange"
    class_model_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.IndefiniteRange

    type: str = None
    value: float = None
    comparator: Union[str, "ComparatorOptions"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, float):
            self.value = float(self.value)

        if self._is_empty(self.comparator):
            self.MissingRequiredField("comparator")
        if not isinstance(self.comparator, ComparatorOptions):
            self.comparator = ComparatorOptions(self.comparator)

        super().__post_init__(**kwargs)


class CURIE(YAMLRoot):
    """
    A [W3C Compact URI](https://www.w3.org/TR/curie/) formatted string. A CURIE string has the structure
    ``prefix``:``reference``, as defined by the W3C syntax.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.CURIE
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:CURIE"
    class_name: ClassVar[str] = "CURIE"
    class_model_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.CURIE


class HumanCytoband(YAMLRoot):
    """
    A character string representing cytobands derived from the *International System for Human Cytogenomic
    Nomenclature* (ISCN) [guidelines](http://doi.org/10.1159/isbn.978-3-318-06861-0).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.HumanCytoband
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:HumanCytoband"
    class_name: ClassVar[str] = "HumanCytoband"
    class_model_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.HumanCytoband


class Residue(YAMLRoot):
    """
    A character representing a specific residue (i.e., molecular species) or groupings of these ("ambiguity codes"),
    using [one-letter IUPAC
    abbreviations](https://en.wikipedia.org/wiki/International_Union_of_Pure_and_Applied_Chemistry#Amino_acid_and_nucleotide_base_codes)
    for nucleic acids and amino acids.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.Residue
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:Residue"
    class_name: ClassVar[str] = "Residue"
    class_model_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.Residue


class Sequence(YAMLRoot):
    """
    A character string of Residues that represents a biological sequence using the conventional sequence order
    (5’-to-3’ for nucleic acid sequences, and amino-to-carboxyl for amino acid sequences). IUPAC ambiguity codes are
    permitted in Sequences.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.Sequence
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:Sequence"
    class_name: ClassVar[str] = "Sequence"
    class_model_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.Sequence


@dataclass
class SequenceState(YAMLRoot):
    """
    DEPRECATED. A Sequence as a State. This is the State class to use for representing "ref-alt" style variation,
    including SNVs, MNVs, del, ins, and delins. This class is deprecated. Use LiteralSequenceExpression instead.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.SequenceState
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:SequenceState"
    class_name: ClassVar[str] = "SequenceState"
    class_model_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.SequenceState

    type: str = None
    sequence: Union[dict, Sequence] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.sequence):
            self.MissingRequiredField("sequence")
        if not isinstance(self.sequence, Sequence):
            self.sequence = Sequence()

        super().__post_init__(**kwargs)


@dataclass
class SimpleInterval(YAMLRoot):
    """
    DEPRECATED: A SimpleInterval represents a span of sequence. Positions are always represented by contiguous spans
    using interbase coordinates. This class is deprecated. Use SequenceInterval instead.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.SimpleInterval
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:SimpleInterval"
    class_name: ClassVar[str] = "SimpleInterval"
    class_model_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.SimpleInterval

    type: str = None
    start: int = None
    end: int = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.start):
            self.MissingRequiredField("start")
        if not isinstance(self.start, int):
            self.start = int(self.start)

        if self._is_empty(self.end):
            self.MissingRequiredField("end")
        if not isinstance(self.end, int):
            self.end = int(self.end)

        super().__post_init__(**kwargs)


# Enumerations
class ComparatorOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="ComparatorOptions",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "<=",
                PermissibleValue(text="<=") )
        setattr(cls, ">=",
                PermissibleValue(text=">=") )

# Slots
class slots:
    pass

slots._id = Slot(uri=GA4GHVRSDEFINITIONS._id, name="_id", curie=GA4GHVRSDEFINITIONS.curie('_id'),
                   model_uri=GA4GHVRSDEFINITIONS._id, domain=None, range=Optional[Union[dict, CURIE]])

slots.type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=GA4GHVRSDEFINITIONS.type, domain=None, range=str)

slots.location = Slot(uri=GA4GHVRSDEFINITIONS.location, name="location", curie=GA4GHVRSDEFINITIONS.curie('location'),
                   model_uri=GA4GHVRSDEFINITIONS.location, domain=None, range=Union[dict, SequenceLocation])

slots.state = Slot(uri=GA4GHVRSDEFINITIONS.state, name="state", curie=GA4GHVRSDEFINITIONS.curie('state'),
                   model_uri=GA4GHVRSDEFINITIONS.state, domain=None, range=str)

slots.members = Slot(uri=GA4GHVRSDEFINITIONS.members, name="members", curie=GA4GHVRSDEFINITIONS.curie('members'),
                   model_uri=GA4GHVRSDEFINITIONS.members, domain=None, range=Union[str, List[str]])

slots.definition = Slot(uri=GA4GHVRSDEFINITIONS.definition, name="definition", curie=GA4GHVRSDEFINITIONS.curie('definition'),
                   model_uri=GA4GHVRSDEFINITIONS.definition, domain=None, range=str)

slots.subject = Slot(uri=GA4GHVRSDEFINITIONS.subject, name="subject", curie=GA4GHVRSDEFINITIONS.curie('subject'),
                   model_uri=GA4GHVRSDEFINITIONS.subject, domain=None, range=str)

slots.copies = Slot(uri=GA4GHVRSDEFINITIONS.copies, name="copies", curie=GA4GHVRSDEFINITIONS.curie('copies'),
                   model_uri=GA4GHVRSDEFINITIONS.copies, domain=None, range=str)

slots.species_id = Slot(uri=GA4GHVRSDEFINITIONS.species_id, name="species_id", curie=GA4GHVRSDEFINITIONS.curie('species_id'),
                   model_uri=GA4GHVRSDEFINITIONS.species_id, domain=None, range=Union[dict, CURIE])

slots.chr = Slot(uri=GA4GHVRSDEFINITIONS.chr, name="chr", curie=GA4GHVRSDEFINITIONS.curie('chr'),
                   model_uri=GA4GHVRSDEFINITIONS.chr, domain=None, range=str)

slots.interval = Slot(uri=GA4GHVRSDEFINITIONS.interval, name="interval", curie=GA4GHVRSDEFINITIONS.curie('interval'),
                   model_uri=GA4GHVRSDEFINITIONS.interval, domain=None, range=str)

slots.sequence_id = Slot(uri=GA4GHVRSDEFINITIONS.sequence_id, name="sequence_id", curie=GA4GHVRSDEFINITIONS.curie('sequence_id'),
                   model_uri=GA4GHVRSDEFINITIONS.sequence_id, domain=None, range=Union[dict, CURIE])

slots.start = Slot(uri=GA4GHVRSDEFINITIONS.start, name="start", curie=GA4GHVRSDEFINITIONS.curie('start'),
                   model_uri=GA4GHVRSDEFINITIONS.start, domain=None, range=int)

slots.end = Slot(uri=GA4GHVRSDEFINITIONS.end, name="end", curie=GA4GHVRSDEFINITIONS.curie('end'),
                   model_uri=GA4GHVRSDEFINITIONS.end, domain=None, range=int)

slots.sequence = Slot(uri=GA4GHVRSDEFINITIONS.sequence, name="sequence", curie=GA4GHVRSDEFINITIONS.curie('sequence'),
                   model_uri=GA4GHVRSDEFINITIONS.sequence, domain=None, range=Union[dict, Sequence])

slots.reverse_complement = Slot(uri=GA4GHVRSDEFINITIONS.reverse_complement, name="reverse_complement", curie=GA4GHVRSDEFINITIONS.curie('reverse_complement'),
                   model_uri=GA4GHVRSDEFINITIONS.reverse_complement, domain=None, range=Union[bool, Bool])

slots.seq_expr = Slot(uri=GA4GHVRSDEFINITIONS.seq_expr, name="seq_expr", curie=GA4GHVRSDEFINITIONS.curie('seq_expr'),
                   model_uri=GA4GHVRSDEFINITIONS.seq_expr, domain=None, range=str)

slots.count = Slot(uri=GA4GHVRSDEFINITIONS.count, name="count", curie=GA4GHVRSDEFINITIONS.curie('count'),
                   model_uri=GA4GHVRSDEFINITIONS.count, domain=None, range=str)

slots.components = Slot(uri=GA4GHVRSDEFINITIONS.components, name="components", curie=GA4GHVRSDEFINITIONS.curie('components'),
                   model_uri=GA4GHVRSDEFINITIONS.components, domain=None, range=Union[str, List[str]])

slots.gene_id = Slot(uri=GA4GHVRSDEFINITIONS.gene_id, name="gene_id", curie=GA4GHVRSDEFINITIONS.curie('gene_id'),
                   model_uri=GA4GHVRSDEFINITIONS.gene_id, domain=None, range=Union[dict, CURIE])

slots.value = Slot(uri=GA4GHVRSDEFINITIONS.value, name="value", curie=GA4GHVRSDEFINITIONS.curie('value'),
                   model_uri=GA4GHVRSDEFINITIONS.value, domain=None, range=float)

slots.min = Slot(uri=GA4GHVRSDEFINITIONS.min, name="min", curie=GA4GHVRSDEFINITIONS.curie('min'),
                   model_uri=GA4GHVRSDEFINITIONS.min, domain=None, range=float)

slots.max = Slot(uri=GA4GHVRSDEFINITIONS.max, name="max", curie=GA4GHVRSDEFINITIONS.curie('max'),
                   model_uri=GA4GHVRSDEFINITIONS.max, domain=None, range=float)

slots.comparator = Slot(uri=GA4GHVRSDEFINITIONS.comparator, name="comparator", curie=GA4GHVRSDEFINITIONS.curie('comparator'),
                   model_uri=GA4GHVRSDEFINITIONS.comparator, domain=None, range=Union[str, "ComparatorOptions"])

slots.Allele__id = Slot(uri=GA4GHVRSDEFINITIONS._id, name="Allele__id", curie=GA4GHVRSDEFINITIONS.curie('_id'),
                   model_uri=GA4GHVRSDEFINITIONS.Allele__id, domain=Allele, range=Optional[Union[dict, "CURIE"]])

slots.Allele_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="Allele_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=GA4GHVRSDEFINITIONS.Allele_type, domain=Allele, range=str)

slots.Allele_location = Slot(uri=GA4GHVRSDEFINITIONS.location, name="Allele_location", curie=GA4GHVRSDEFINITIONS.curie('location'),
                   model_uri=GA4GHVRSDEFINITIONS.Allele_location, domain=Allele, range=Union[dict, "SequenceLocation"])

slots.Allele_state = Slot(uri=GA4GHVRSDEFINITIONS.state, name="Allele_state", curie=GA4GHVRSDEFINITIONS.curie('state'),
                   model_uri=GA4GHVRSDEFINITIONS.Allele_state, domain=Allele, range=str)

slots.Haplotype__id = Slot(uri=GA4GHVRSDEFINITIONS._id, name="Haplotype__id", curie=GA4GHVRSDEFINITIONS.curie('_id'),
                   model_uri=GA4GHVRSDEFINITIONS.Haplotype__id, domain=Haplotype, range=Optional[Union[dict, "CURIE"]])

slots.Haplotype_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="Haplotype_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=GA4GHVRSDEFINITIONS.Haplotype_type, domain=Haplotype, range=str)

slots.Haplotype_members = Slot(uri=GA4GHVRSDEFINITIONS.members, name="Haplotype_members", curie=GA4GHVRSDEFINITIONS.curie('members'),
                   model_uri=GA4GHVRSDEFINITIONS.Haplotype_members, domain=Haplotype, range=Union[str, List[str]])

slots.Text__id = Slot(uri=GA4GHVRSDEFINITIONS._id, name="Text__id", curie=GA4GHVRSDEFINITIONS.curie('_id'),
                   model_uri=GA4GHVRSDEFINITIONS.Text__id, domain=Text, range=Optional[Union[dict, "CURIE"]])

slots.Text_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="Text_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=GA4GHVRSDEFINITIONS.Text_type, domain=Text, range=str)

slots.Text_definition = Slot(uri=GA4GHVRSDEFINITIONS.definition, name="Text_definition", curie=GA4GHVRSDEFINITIONS.curie('definition'),
                   model_uri=GA4GHVRSDEFINITIONS.Text_definition, domain=Text, range=str)

slots.VariationSet__id = Slot(uri=GA4GHVRSDEFINITIONS._id, name="VariationSet__id", curie=GA4GHVRSDEFINITIONS.curie('_id'),
                   model_uri=GA4GHVRSDEFINITIONS.VariationSet__id, domain=VariationSet, range=Optional[Union[dict, "CURIE"]])

slots.VariationSet_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="VariationSet_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=GA4GHVRSDEFINITIONS.VariationSet_type, domain=VariationSet, range=str)

slots.VariationSet_members = Slot(uri=GA4GHVRSDEFINITIONS.members, name="VariationSet_members", curie=GA4GHVRSDEFINITIONS.curie('members'),
                   model_uri=GA4GHVRSDEFINITIONS.VariationSet_members, domain=VariationSet, range=Union[str, List[str]])

slots.CopyNumber__id = Slot(uri=GA4GHVRSDEFINITIONS._id, name="CopyNumber__id", curie=GA4GHVRSDEFINITIONS.curie('_id'),
                   model_uri=GA4GHVRSDEFINITIONS.CopyNumber__id, domain=CopyNumber, range=Optional[Union[dict, "CURIE"]])

slots.CopyNumber_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="CopyNumber_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=GA4GHVRSDEFINITIONS.CopyNumber_type, domain=CopyNumber, range=str)

slots.CopyNumber_subject = Slot(uri=GA4GHVRSDEFINITIONS.subject, name="CopyNumber_subject", curie=GA4GHVRSDEFINITIONS.curie('subject'),
                   model_uri=GA4GHVRSDEFINITIONS.CopyNumber_subject, domain=CopyNumber, range=str)

slots.CopyNumber_copies = Slot(uri=GA4GHVRSDEFINITIONS.copies, name="CopyNumber_copies", curie=GA4GHVRSDEFINITIONS.curie('copies'),
                   model_uri=GA4GHVRSDEFINITIONS.CopyNumber_copies, domain=CopyNumber, range=str)

slots.ChromosomeLocation__id = Slot(uri=GA4GHVRSDEFINITIONS._id, name="ChromosomeLocation__id", curie=GA4GHVRSDEFINITIONS.curie('_id'),
                   model_uri=GA4GHVRSDEFINITIONS.ChromosomeLocation__id, domain=ChromosomeLocation, range=Optional[Union[dict, "CURIE"]])

slots.ChromosomeLocation_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="ChromosomeLocation_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=GA4GHVRSDEFINITIONS.ChromosomeLocation_type, domain=ChromosomeLocation, range=str)

slots.ChromosomeLocation_species_id = Slot(uri=GA4GHVRSDEFINITIONS.species_id, name="ChromosomeLocation_species_id", curie=GA4GHVRSDEFINITIONS.curie('species_id'),
                   model_uri=GA4GHVRSDEFINITIONS.ChromosomeLocation_species_id, domain=ChromosomeLocation, range=Union[dict, "CURIE"])

slots.ChromosomeLocation_chr = Slot(uri=GA4GHVRSDEFINITIONS.chr, name="ChromosomeLocation_chr", curie=GA4GHVRSDEFINITIONS.curie('chr'),
                   model_uri=GA4GHVRSDEFINITIONS.ChromosomeLocation_chr, domain=ChromosomeLocation, range=str)

slots.ChromosomeLocation_interval = Slot(uri=GA4GHVRSDEFINITIONS.interval, name="ChromosomeLocation_interval", curie=GA4GHVRSDEFINITIONS.curie('interval'),
                   model_uri=GA4GHVRSDEFINITIONS.ChromosomeLocation_interval, domain=ChromosomeLocation, range=Union[dict, "CytobandInterval"])

slots.SequenceLocation__id = Slot(uri=GA4GHVRSDEFINITIONS._id, name="SequenceLocation__id", curie=GA4GHVRSDEFINITIONS.curie('_id'),
                   model_uri=GA4GHVRSDEFINITIONS.SequenceLocation__id, domain=SequenceLocation, range=Optional[Union[dict, "CURIE"]])

slots.SequenceLocation_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="SequenceLocation_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=GA4GHVRSDEFINITIONS.SequenceLocation_type, domain=SequenceLocation, range=str)

slots.SequenceLocation_sequence_id = Slot(uri=GA4GHVRSDEFINITIONS.sequence_id, name="SequenceLocation_sequence_id", curie=GA4GHVRSDEFINITIONS.curie('sequence_id'),
                   model_uri=GA4GHVRSDEFINITIONS.SequenceLocation_sequence_id, domain=SequenceLocation, range=Union[dict, "CURIE"])

slots.SequenceLocation_interval = Slot(uri=GA4GHVRSDEFINITIONS.interval, name="SequenceLocation_interval", curie=GA4GHVRSDEFINITIONS.curie('interval'),
                   model_uri=GA4GHVRSDEFINITIONS.SequenceLocation_interval, domain=SequenceLocation, range=str)

slots.SequenceInterval_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="SequenceInterval_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=GA4GHVRSDEFINITIONS.SequenceInterval_type, domain=SequenceInterval, range=str)

slots.SequenceInterval_start = Slot(uri=GA4GHVRSDEFINITIONS.start, name="SequenceInterval_start", curie=GA4GHVRSDEFINITIONS.curie('start'),
                   model_uri=GA4GHVRSDEFINITIONS.SequenceInterval_start, domain=SequenceInterval, range=int)

slots.SequenceInterval_end = Slot(uri=GA4GHVRSDEFINITIONS.end, name="SequenceInterval_end", curie=GA4GHVRSDEFINITIONS.curie('end'),
                   model_uri=GA4GHVRSDEFINITIONS.SequenceInterval_end, domain=SequenceInterval, range=int)

slots.CytobandInterval_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="CytobandInterval_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=GA4GHVRSDEFINITIONS.CytobandInterval_type, domain=CytobandInterval, range=str)

slots.CytobandInterval_start = Slot(uri=GA4GHVRSDEFINITIONS.start, name="CytobandInterval_start", curie=GA4GHVRSDEFINITIONS.curie('start'),
                   model_uri=GA4GHVRSDEFINITIONS.CytobandInterval_start, domain=CytobandInterval, range=Union[dict, "HumanCytoband"])

slots.CytobandInterval_end = Slot(uri=GA4GHVRSDEFINITIONS.end, name="CytobandInterval_end", curie=GA4GHVRSDEFINITIONS.curie('end'),
                   model_uri=GA4GHVRSDEFINITIONS.CytobandInterval_end, domain=CytobandInterval, range=Union[dict, "HumanCytoband"])

slots.LiteralSequenceExpression_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="LiteralSequenceExpression_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=GA4GHVRSDEFINITIONS.LiteralSequenceExpression_type, domain=LiteralSequenceExpression, range=str)

slots.LiteralSequenceExpression_sequence = Slot(uri=GA4GHVRSDEFINITIONS.sequence, name="LiteralSequenceExpression_sequence", curie=GA4GHVRSDEFINITIONS.curie('sequence'),
                   model_uri=GA4GHVRSDEFINITIONS.LiteralSequenceExpression_sequence, domain=LiteralSequenceExpression, range=Union[dict, "Sequence"])

slots.DerivedSequenceExpression_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="DerivedSequenceExpression_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=GA4GHVRSDEFINITIONS.DerivedSequenceExpression_type, domain=DerivedSequenceExpression, range=str)

slots.DerivedSequenceExpression_location = Slot(uri=GA4GHVRSDEFINITIONS.location, name="DerivedSequenceExpression_location", curie=GA4GHVRSDEFINITIONS.curie('location'),
                   model_uri=GA4GHVRSDEFINITIONS.DerivedSequenceExpression_location, domain=DerivedSequenceExpression, range=Union[dict, SequenceLocation])

slots.DerivedSequenceExpression_reverse_complement = Slot(uri=GA4GHVRSDEFINITIONS.reverse_complement, name="DerivedSequenceExpression_reverse_complement", curie=GA4GHVRSDEFINITIONS.curie('reverse_complement'),
                   model_uri=GA4GHVRSDEFINITIONS.DerivedSequenceExpression_reverse_complement, domain=DerivedSequenceExpression, range=Union[bool, Bool])

slots.RepeatedSequenceExpression_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="RepeatedSequenceExpression_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=GA4GHVRSDEFINITIONS.RepeatedSequenceExpression_type, domain=RepeatedSequenceExpression, range=str)

slots.RepeatedSequenceExpression_seq_expr = Slot(uri=GA4GHVRSDEFINITIONS.seq_expr, name="RepeatedSequenceExpression_seq_expr", curie=GA4GHVRSDEFINITIONS.curie('seq_expr'),
                   model_uri=GA4GHVRSDEFINITIONS.RepeatedSequenceExpression_seq_expr, domain=RepeatedSequenceExpression, range=str)

slots.RepeatedSequenceExpression_count = Slot(uri=GA4GHVRSDEFINITIONS.count, name="RepeatedSequenceExpression_count", curie=GA4GHVRSDEFINITIONS.curie('count'),
                   model_uri=GA4GHVRSDEFINITIONS.RepeatedSequenceExpression_count, domain=RepeatedSequenceExpression, range=str)

slots.ComposedSequenceExpression_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="ComposedSequenceExpression_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=GA4GHVRSDEFINITIONS.ComposedSequenceExpression_type, domain=ComposedSequenceExpression, range=str)

slots.ComposedSequenceExpression_components = Slot(uri=GA4GHVRSDEFINITIONS.components, name="ComposedSequenceExpression_components", curie=GA4GHVRSDEFINITIONS.curie('components'),
                   model_uri=GA4GHVRSDEFINITIONS.ComposedSequenceExpression_components, domain=ComposedSequenceExpression, range=Union[str, List[str]])

slots.Gene_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="Gene_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=GA4GHVRSDEFINITIONS.Gene_type, domain=Gene, range=str)

slots.Gene_gene_id = Slot(uri=GA4GHVRSDEFINITIONS.gene_id, name="Gene_gene_id", curie=GA4GHVRSDEFINITIONS.curie('gene_id'),
                   model_uri=GA4GHVRSDEFINITIONS.Gene_gene_id, domain=Gene, range=Union[dict, "CURIE"])

slots.Number_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="Number_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=GA4GHVRSDEFINITIONS.Number_type, domain=Number, range=str)

slots.Number_value = Slot(uri=GA4GHVRSDEFINITIONS.value, name="Number_value", curie=GA4GHVRSDEFINITIONS.curie('value'),
                   model_uri=GA4GHVRSDEFINITIONS.Number_value, domain=Number, range=int)

slots.DefiniteRange_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="DefiniteRange_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=GA4GHVRSDEFINITIONS.DefiniteRange_type, domain=DefiniteRange, range=str)

slots.DefiniteRange_min = Slot(uri=GA4GHVRSDEFINITIONS.min, name="DefiniteRange_min", curie=GA4GHVRSDEFINITIONS.curie('min'),
                   model_uri=GA4GHVRSDEFINITIONS.DefiniteRange_min, domain=DefiniteRange, range=float)

slots.DefiniteRange_max = Slot(uri=GA4GHVRSDEFINITIONS.max, name="DefiniteRange_max", curie=GA4GHVRSDEFINITIONS.curie('max'),
                   model_uri=GA4GHVRSDEFINITIONS.DefiniteRange_max, domain=DefiniteRange, range=float)

slots.IndefiniteRange_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="IndefiniteRange_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=GA4GHVRSDEFINITIONS.IndefiniteRange_type, domain=IndefiniteRange, range=str)

slots.IndefiniteRange_value = Slot(uri=GA4GHVRSDEFINITIONS.value, name="IndefiniteRange_value", curie=GA4GHVRSDEFINITIONS.curie('value'),
                   model_uri=GA4GHVRSDEFINITIONS.IndefiniteRange_value, domain=IndefiniteRange, range=float)

slots.IndefiniteRange_comparator = Slot(uri=GA4GHVRSDEFINITIONS.comparator, name="IndefiniteRange_comparator", curie=GA4GHVRSDEFINITIONS.curie('comparator'),
                   model_uri=GA4GHVRSDEFINITIONS.IndefiniteRange_comparator, domain=IndefiniteRange, range=Union[str, "ComparatorOptions"])

slots.SequenceState_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="SequenceState_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=GA4GHVRSDEFINITIONS.SequenceState_type, domain=SequenceState, range=str)

slots.SequenceState_sequence = Slot(uri=GA4GHVRSDEFINITIONS.sequence, name="SequenceState_sequence", curie=GA4GHVRSDEFINITIONS.curie('sequence'),
                   model_uri=GA4GHVRSDEFINITIONS.SequenceState_sequence, domain=SequenceState, range=Union[dict, Sequence])

slots.SimpleInterval_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="SimpleInterval_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=GA4GHVRSDEFINITIONS.SimpleInterval_type, domain=SimpleInterval, range=str)

slots.SimpleInterval_start = Slot(uri=GA4GHVRSDEFINITIONS.start, name="SimpleInterval_start", curie=GA4GHVRSDEFINITIONS.curie('start'),
                   model_uri=GA4GHVRSDEFINITIONS.SimpleInterval_start, domain=SimpleInterval, range=int)

slots.SimpleInterval_end = Slot(uri=GA4GHVRSDEFINITIONS.end, name="SimpleInterval_end", curie=GA4GHVRSDEFINITIONS.curie('end'),
                   model_uri=GA4GHVRSDEFINITIONS.SimpleInterval_end, domain=SimpleInterval, range=int)