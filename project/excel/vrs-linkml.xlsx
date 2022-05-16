

CREATE TABLE "Allele" (
	_id TEXT, 
	type TEXT NOT NULL, 
	location TEXT NOT NULL, 
	state TEXT NOT NULL, 
	PRIMARY KEY (_id, type, location, state)
);

CREATE TABLE "ChromosomeLocation" (
	_id TEXT, 
	type TEXT NOT NULL, 
	species_id TEXT NOT NULL, 
	chr TEXT NOT NULL, 
	interval TEXT NOT NULL, 
	PRIMARY KEY (_id, type, species_id, chr, interval)
);

CREATE TABLE "ComposedSequenceExpression" (
	type TEXT NOT NULL, 
	components TEXT NOT NULL, 
	PRIMARY KEY (type, components)
);

CREATE TABLE "CopyNumber" (
	_id TEXT, 
	type TEXT NOT NULL, 
	subject TEXT NOT NULL, 
	copies TEXT NOT NULL, 
	PRIMARY KEY (_id, type, subject, copies)
);

CREATE TABLE "CytobandInterval" (
	type TEXT NOT NULL, 
	start TEXT NOT NULL, 
	"end" TEXT NOT NULL, 
	PRIMARY KEY (type, start, "end")
);

CREATE TABLE "DefiniteRange" (
	type TEXT NOT NULL, 
	min FLOAT NOT NULL, 
	max FLOAT NOT NULL, 
	PRIMARY KEY (type, min, max)
);

CREATE TABLE "DerivedSequenceExpression" (
	type TEXT NOT NULL, 
	location TEXT NOT NULL, 
	reverse_complement BOOLEAN NOT NULL, 
	PRIMARY KEY (type, location, reverse_complement)
);

CREATE TABLE "Gene" (
	type TEXT NOT NULL, 
	gene_id TEXT NOT NULL, 
	PRIMARY KEY (type, gene_id)
);

CREATE TABLE "Haplotype" (
	_id TEXT, 
	type TEXT NOT NULL, 
	members TEXT NOT NULL, 
	PRIMARY KEY (_id, type, members)
);

CREATE TABLE "IndefiniteRange" (
	type TEXT NOT NULL, 
	value FLOAT NOT NULL, 
	comparator VARCHAR(2) NOT NULL, 
	PRIMARY KEY (type, value, comparator)
);

CREATE TABLE "LiteralSequenceExpression" (
	type TEXT NOT NULL, 
	sequence TEXT NOT NULL, 
	PRIMARY KEY (type, sequence)
);

CREATE TABLE "Number" (
	type TEXT NOT NULL, 
	value INTEGER NOT NULL, 
	PRIMARY KEY (type, value)
);

CREATE TABLE "RepeatedSequenceExpression" (
	type TEXT NOT NULL, 
	seq_expr TEXT NOT NULL, 
	count TEXT NOT NULL, 
	PRIMARY KEY (type, seq_expr, count)
);

CREATE TABLE "SequenceInterval" (
	type TEXT NOT NULL, 
	start INTEGER NOT NULL, 
	"end" INTEGER NOT NULL, 
	PRIMARY KEY (type, start, "end")
);

CREATE TABLE "SequenceLocation" (
	_id TEXT, 
	type TEXT NOT NULL, 
	sequence_id TEXT NOT NULL, 
	interval TEXT NOT NULL, 
	PRIMARY KEY (_id, type, sequence_id, interval)
);

CREATE TABLE "SequenceState" (
	type TEXT NOT NULL, 
	sequence TEXT NOT NULL, 
	PRIMARY KEY (type, sequence)
);

CREATE TABLE "SimpleInterval" (
	type TEXT NOT NULL, 
	start INTEGER NOT NULL, 
	"end" INTEGER NOT NULL, 
	PRIMARY KEY (type, start, "end")
);

CREATE TABLE "Text" (
	_id TEXT, 
	type TEXT NOT NULL, 
	definition TEXT NOT NULL, 
	PRIMARY KEY (_id, type, definition)
);

CREATE TABLE "VariationSet" (
	_id TEXT, 
	type TEXT NOT NULL, 
	members TEXT NOT NULL, 
	PRIMARY KEY (_id, type, members)
);
