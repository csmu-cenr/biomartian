print("library('biomaRt')")
library('biomaRt')

print('mart <- useMart("ensembl", dataset = "rnorvegicus_gene_ensembl")')
mart <- useMart("ensembl", dataset = "rnorvegicus_gene_ensembl")

print("input_output_map_df <- getBM(attributes=c('entrezgene', 'external_gene_name'), mart = mart, values = '*')")
input_output_map_df <- getBM(attributes=c('entrezgene', 'external_gene_name'), mart = mart, values = '*')

print("write.table(input_output_map_df, '/local/home/endrebak/Code/biomartian/testing/from_r_input_output_map_df.csv', sep='\t', quote=F, na='NA')")
write.table(input_output_map_df, '/local/home/endrebak/Code/biomartian/testing/from_r_input_output_map_df.csv', sep='\t', quote=F, na='NA')

