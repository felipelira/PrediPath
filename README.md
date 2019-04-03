# PrediPath

  Currently, bacterial pathogenicity prediction relies on traditional microbiological methods which are time consuming and require specialists. Thus, comparative genomics emerges as a promising method which allows to check in silico the presence of genomics elements to distinguish pathogenic (P) from nonpathogenic (NP) organisms. In order to predict the potential pathogenicity of plant associated bacteria, we designed the PREDIPATH workflow to detect genomic markers associated to bacterial phenotypes.

Three strategies are applied:

   I – An a priori approach consisted in detecting potentially over-represented genes in pathogens. For that purpose, the PREDIPATH database, composed of genes collected from public repositories and involved in virulence [1], and antimicrobial, biocides and heavy metal resistance [2,3] was created. Biosynthetic gene clusters encoding the production of secondary metabolites were searched using antiSMASH 4 database [4]; 

   II – A without a priori approach aimed at deciphering group-specific DNA fragments. First, a genome-wide association study using an alignment-free method was used to detect differential kmers [5]. Second, the accessory genome was explored to search for group-specific orthologous genes [6].

   III – An additional strategy allowed to search plasmids to characterize P or NP groups.

This workflow will allows the creation of exclusive datasets of markers that could be used as predictors to diagnostic the potential pathogenicity of plant associated bacteria.



References

[1] Chen LH, Yang J, Yu J, Yao ZJ, Sun LL, Shen Y and Jin Q, 2005. VFDB: a reference database for bacterial virulence factors. Nucleic Acids Res. 36 (Database issue):D539-D542.

[2] Jia B, Raphenya AR, Alcock B, et al. CARD 2017: expansion and model-centric curation of the comprehensive antibiotic resistance database. Nucleic Acids Res. 2016;45(D1):D566-D573.

[3] Pal, C., Bengtsson-Palme, J., Rensing, C., Kristiansson, E., Larsson, DGJ. (2014) BacMet: antibacterial biocide and metal resistance genes database, Nucleic Acids Res., 42, D737-D743.

[4] Blin K, Wolf T, Chevrette MG, et al. antiSMASH 4.0-improvements in chemistry prediction and gene cluster boundary identification. Nucleic Acids Res. 2017;45(W1):W36-W41.

[5] Jaillard M, Lima L, Tournoud M, Mahé P, et al. (2018) A fast and agnostic method for bacterial genome-wide association studies: Bridging the gap between kmers and genetic events. PLoS Genetics 14(11): e1007758.

[6] Contreras-Moreira B, Vinuesa P. GET_HOMOLOGUES, a versatile software package for scalable and robust microbial pangenome analysis. Appl Environ Microbiol. 2013;79(24):7696-701.
