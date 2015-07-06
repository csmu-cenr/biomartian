from Bio.KEGG import REST
import pandas as pd

import re


def get_pathways_genes(species):

    all_but_digits = re.compile(r"\D+:")

    gene_pathway_rowdicts = []
    for gene_pathway in REST.kegg_conv(species, "ncbi-gi"):
        entrez, kegg = re.split(all_but_digits, gene_pathway)
        gene_pathway_rowdicts.append({"entrez_gene": entrez, "kegg": kegg})

    pathway_genes = pd.DataFrame.from_dict(gene_pathway_rowdicts)

    return pathway_genes
