```
 _     _                            _   _
| |__ (_) ___  _ __ ___   __ _ _ __| |_(_) __ _ _ __
| '_ \| |/ _ \| '_ ` _ \ / _` | '__| __| |/ _` | '_ \
| |_) | | (_) | | | | | | (_| | |  | |_| | (_| | | | |
|_.__/|_|\___/|_| |_| |_|\__,_|_|   \__|_|\__,_|_| |_|
                   Query biomart from the command line
```

biomartian enables querying BioMart from the command line.

biomartian greatly simplifies extracting data from BioMart.

Instead of having to

1. open an R session
2. load biomaRt
3. load a mart and dataset
4. write the code required to extract the data you need
5. merge the new data into a dataset

you can simply call a single simple biomartian command!

Furthermore, biomartian is all Python, so all the required dependencies are installed with a simple `pip install biomartian`.

biomartian also aids BioMart discoverability since you can use standard tools like `grep` to search BioMart results instead of having to use Rs clunky and verbose ersatz implementation.

Lastly, biomartian caches all queries across sessions (in `~/.biomartian`), so that subsequent queries are instantaneous.

# Examples

#### Find the name of mrna ids in BioMart for the common rat

```
biomartian -d rnorvegicus_gene_ensembl --list-attributes | grep -i mrna
refseq_mrna	RefSeq mRNA [e.g. NM_001195597]
refseq_mrna_predicted	RefSeq mRNA predicted [e.g. XM_001125684]
```

Note that we did not need to write the name of the mart since `ensembl` is the default.

#### Get the refseq mrna id for all regular gene names and attach them to an input file

```
$ head simple.txt
"logFC"	"AveExpr"
"Ipcef1"	-2.70987558746701	4.80047582653889
"Sema3b"	2.00143465979322	3.82969788437155
"Rab26"	-2.40250648553797	5.57320249609294
"Arhgap25"	-1.84668909768998	3.66617832656769
"Ociad2"	-1.99052684394044	5.26213130909702
"Mmp17"	-2.01026790614161	4.88012776225311
"C4a"	2.22003976804983	3.52842041243544
"Gna14"	-2.42391191670209	1.56313048066253
"Kcna6"	-1.74168813159872	6.54586068659631

$ biomartian -d rnorvegicus_gene_ensembl -c 0 -i external_gene_name -o refseq_mrna simple.txt
index	logFC	AveExpr	refseq_mrna
Ipcef1	-2.70987558746701	4.80047582653889	NM_001170799
Sema3b	2.00143465979322	3.82969788437155	NM_001079942
Rab26	-2.40250648553797	5.57320249609294	NM_133580
Arhgap25	-1.84668909768998	3.66617832656769	NM_001109247
Ociad2	-1.99052684394044	5.26213130909702	NM_001271181
Mmp17	-2.01026790614161	4.88012776225311	NM_001105925
C4a	2.22003976804983	3.52842041243544	NM_031504
C4a	2.22003976804983	3.52842041243544	NA
Gna14	-2.42391191670209	1.56313048066253	NM_001013151
Kcna6	-1.74168813159872	6.54586068659631	NM_023954
```

# Install

```
pip install biomartian
```

#### Usage

```
biomartian

Query biomart from the command line.
For help and examples, visit github.com/endrebak/biomartian

Usage:
    biomartian [--mart=MART] [--dataset=DATA] --mergecol=COL... --intype=IN... --outtype=OUT... [--noheader] FILE
    biomartian [--mart=MART] [--dataset=DATA] --intype=IN --outtype=OUT
    biomartian --list-marts
    biomartian [--mart=MART] --list-datasets
    biomartian [--mart=MART] [--dataset=DATASET] --list-attributes

Arguments:
    FILE                   file with COL(s) to join mart data on (- for STDIN)
    -i IN --intype=IN      the datatype in the column to merge on
    -o OUT --outtype=OUT   the datatype to get (joining on value COL)
    -c COL --mergecol=COL  name or number of the column to join on in FILE

Note:
    Required args --intype, --outtype and --mergecol must be equal in number.

Options:
    -h      --help          show this message
    -m MART --mart=MART     which mart to use [default: ensembl]
    -d DATA --dataset=DATA  which dataset to use [default: hsapiens_gene_ensembl]
    -n --noheader           the input data does not contain a header (must
                            use integers to denote COL)

Lists:
    --list-marts       show all available marts
    --list-datasets    show all available datasets for MART
    --list-attributes  show all kinds of data available for MART and DATASET
```

# TODO

* enable viewing dates of cached data
* enable removing one single dataset from the cache

# Issues

Please use the biomartian [issues page](https://github.com/endrebak/biomartian/issues) for issues, suggestions, feature-requests and troubleshooting.

# Requirements

Python, either version 2.7 or 3.x.

* `bioservices`, `pandas`, `docopt`, `joblib`, `ebs` (all installed automatically when using pip)

# Thanks

Thomas Cokelaer for his [bioservices package](https://github.com/cokelaer/bioservices).

See his page for citation info.
