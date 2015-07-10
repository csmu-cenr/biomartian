# biomartian
Convert gene names via the command line

# Undergoing massive rewrite atm. Check back in a week :)

# TODO

* decorator with to/from in header

# Example

#### Input data
Any tab-delimited file will do.
(Obviously, non-data columns and headers do not need to be surrounded with "".)

```bash
endrebak@havpryd ~/C/biomartian> head examples/MedIIvsD.txt
"Gene"	"logFC"	"AveExpr"
"Brinp3"	-1.92040698516041	6.33733039821208
"Tle4"	-1.68336568459123	6.88285301682597
"Rab26"	-1.83060602348488	5.57320249551508
"Ipcef1"	-1.97594838378759	4.80047582596103
"Rassf2"	1.08094275753519	5.89304511598244
"Nxph3"	-3.27998684674834	4.6844454153822
"Sstr2"	-1.81121949561318	4.21103179776388
"Lrrtm2"	-1.3944222489979	6.54430209960799
"Slc12a4"	1.15991299670081	4.67930875026887
```

#### Usage

`python biomartian.py <name_of_column_to_convert> <input_type> <output_type> <species> <input_file>`

```bash
endrebak@havpryd ~/C/biomartian> python biomartian.py Gene external_gene_name \
refseq_mrna rnorvegicus_gene_ensembl examples/MedIIvsD.txt  | head
Gene	logFC	AveExpr	refseq_mrna
Brinp3	-1.9204069851604098	6.33733039821208	NM_173121
Tle4	-1.68336568459123	6.882853016825969	NM_019141
Rab26	-1.83060602348488	5.57320249551508	NM_133580
Ipcef1	-1.97594838378759	4.80047582596103	NM_001170799
Rassf2	1.08094275753519	5.89304511598244	NM_001037096
Nxph3	-3.27998684674834	4.684445415382201	NM_021679
Sstr2	-1.8112194956131797	4.21103179776388	NM_019348
Lrrtm2	-1.3944222489979	6.5443020996079895	NM_001109469
Slc12a4	1.15991299670081	4.67930875026887	NM_019229
```

#### Logging

To show script progress info on stderr add logging as final argument

```bash
endrebak@havpryd ~/C/biomartian> python biomartian.py Gene external_gene_name \
           refseq_mrna rnorvegicus_gene_ensembl examples/MedIIvsD.txt logging
Reading input table from file: examples/MedIIvsD.txt (Time: Wed, 03 Jun 2015 12:48:58)
Loading biomaRt for species: rnorvegicus_gene_ensembl (Time: Wed, 03 Jun 2015 12:48:58)
Converting 4537 gene names in file examples/MedIIvsD.txt to refseq_mrna (Time: Wed, 03 Jun 2015 12:49:04)
Creating new dataframe with additional gene names. (Time: Wed, 03 Jun 2015 12:49:06)
...
```

# TODO

* Add options to list possible species and possible gene types per species
* Allow files without header for index column (how?)
* Add input separator argument; infer by default
* Add argument to tell whether file includes header or not.
* Allow both header name and column number to indicate column to convert

# Issues

Please use the biomartian [issues page](https://github.com/endrebak/biomartian/issues) for issues, suggestions, feature-requests and troubleshooting.

# Requirements

* python: `pyper`, `pandas`
* R: `biomart`
