# biomartyr
Convert gene names via the command line

# Example

```bash
endrebak@havpryd ~/C/biomartyr> head -3 examples/MedIIvsD.txt
NM_001001799
NM_001002288
NM_001002807

# Usage: python biomartyr.py <output_folder> <input_files>
endrebak@havpryd ~/C/biomartyr> python biomartyr.py examples/output_data examples/MedIIvsD.txt
Output folder: examples/output_data (Module: biomartyr, Time: Wed, 03 Jun 2015 10:00:28)
Input files: examples/MedIIvsD.txt (Module: biomartyr, Time: Wed, 03 Jun 2015 10:00:28)
Loading biomaRt. (Module: biomartyr, Time: Wed, 03 Jun 2015 10:00:29)
Converting 1793 gene names in file examples/MedIIvsD.txt to entrez gene ID (Module: biomartyr, Time: Wed, 03 Jun 2015 10:00:34)

# Notice gene missing; no suitable value for it was found.
endrebak@havpryd ~/C/biomartyr> head -3 examples/output_data/MedIIvsD.txt
Tmem35	NM_001001799
Clic1	NM_001002807
Rasl11b	NM_001002830
```

# TODO

* Make more general; currently the species and conversion to/from values are hardcoded.
* Accept all kinds of tabular data (instead of merely one-column lists) and output the input file with an additional column for the converted values.

# Issues

Please use the biomartyr [issues page](https://github.com/endrebak/biomartyr/issues) for issues, suggestions, feature-requests and troubleshooting.
