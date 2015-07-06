# from widediaper import R
from Bio.KEGG import REST as kegg

# @external(provides={"kegg", "entrez_gene"}, requires=["species"])
# needs human, mouse, rat
# hsa, rno, mmu

def get_pathways(species):

    pathways = kegg.get_list("pathway", species)

    return pathways

def get_pathways_genes(species):


    pathways = get_pathways(species)

    pathways_genes = 0

    return pathways_genes
