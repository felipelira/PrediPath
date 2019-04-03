# PrediPath

  Currently, bacterial pathogenicity prediction relies on traditional microbiological methods which are time consuming and require specialists. Thus, comparative genomics emerges as a promising method which allows to check in silico the presence of genomics elements to distinguish pathogenic (P) from nonpathogenic (NP) organisms. In order to predict the potential pathogenicity of plant associated bacteria, we designed the PREDIPATH workflow to detect genomic markers associated to bacterial phenotypes.

    I – An a priori approach consisted in detecting potentially over-represented genes in pathogens. For that purpose, the PREDIPATH database, composed of genes collected from public repositories and involved in virulence [1], and antimicrobial, biocides and heavy metal resistance [2,3] was created. Biosynthetic gene clusters encoding the production of secondary metabolites were searched using antiSMASH 4 database [4]; 

    II – A without a priori approach aimed at deciphering group-specific DNA fragments. First, a genome-wide association study using an alignment-free method was used to detect differential kmers [5]. Second, the accessory genome was explored to search for group-specific orthologous genes [6].

    III – An additional strategy allowed to search plasmids to characterize P or NP groups.
