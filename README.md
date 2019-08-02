<img align="left" width="15%" src="fig_predipath.png"> 

# PREDIPATH
# PREDIcting the bacterial PATHogenicity on plants
# A Plant Pathogenicity Predictor Pipeline 


This repository is used to Predipath scripts and databases.
## Introduction

Make sure you have `git` installed in your computer:
```
sudo apt install python-setuptools python-dev build-essential # Ubuntu
```
Download the `PrediPath` folder from Github:

```download
git clone https://github.com/felipelira/PrediPath
cd PrediPath
chmod +x predipath_pipeline.py
ln -s predipath_pipeline.py /usr/local/bin/predipath
```
## Pipeline
Download the files in https://github.com/felipelira/PrediPath/tree/master/databases/general and move them to your desired PATH.

  The basic command is:
  
    blastp -db Predipath_DB_aa_nr_raw -query [your_proteome.faa]


## Development
PrediPath development was started by the collaboration between the **Institut de Recheche Agronomic - INRA** and the **Université Bretagne Loire - UBL**.

## Fundings
This project, performed at the **Institut de Recherche en Horticulture et Semences (IRHS)**, is supported by fundings from:

1. People Programme Marie Curie Actions of the European Union’s Seventh Framework Programme (FP7/2007-2013) under REA grant agreement n. PCOFUND-GA-2013-609102, through the PRESTIGE Programme coordinated by Campus France;
2. University Bretagne Loire, Programme d’Attractivité Post-Doctorale;
3. Regional program “Objectif Végétal, Research, Education and Innovation in Pays de la Loire”, supported by the French Region Pays de la Loire and Angers Loire Métropole.

## PrediPath Project
* [Felipe Lira](https://github.com/felipelira)
* [Martial Briand]
* [Perrine Portier]
* [Gilles Hunault]
* [Claudine Landes]
* [Marion Fischer-Le Saux]


This directory is created to store the databases used by PrediPath.

For each genus, you will retrieve a specific database containing specific marquers to detect the potential bacterial pathogenicity.

## Development of PREDIPATH Database

PREDIPATH-DB is compose by the compilation of five public datasets of sequences related to antimicrobial and heavy metal resistance, and to virulence [1-5]
```
  1. Liu, B., Zheng D., Jin Q., Chen L. and Yang J.: VFDB 2019: a comparative pathogenomic platform with an interactive web interface. Nucleic Acids Research, Vol. 47, Database issue D687–D692 (2019). doi: 10.1093/nar/gky1080
  2. Pal C., Bengtsson-Palme J., Rensing C., Kristiansson E. and Larsson D.G.J.: BacMet: antibacterial biocide and metal resistance genes database. Nucleic Acids Research, Vol. 42, D737–D743 (2014). doi:10.1093/nar/gkt1252
  3. McArthur A.G., Waglechner N., Nizam F., Yan A., Azad M.A., Baylay A.J., Bhullar K., Canova M.J., De Pascale G., Ejim L., Kalan L., King A.M., Koteva K., Morar M., Mulvey M.R., O’Brien J.S., Pawlowski A.C., Piddock L.J.V., Spanogiannopoulos P., Sutherland A.D., Tang I., Taylor P.L., Thaker M., Wang W., Yan M., Yu T., Wright G.D.: The Comprehensive Antibiotic Resistance Database. Antimicrobial Agents and Chemotherapy, Vol. 57, Number 7, p. 3348–3357 (2013). doi:10.1128/AAC.00419-13
  4. Liu B., Pop M.: ARDB—Antibiotic Resistance Genes Database. Nucleic Acids Research, 2009, Vol. 37, Database issue D443–D447 (2009). doi:10.1093/nar/gkn656
  5. Gupta, S.K., Padmanabhan, B.R., Diene, S.M., Lopez-Rojas, R., Kempf, M., Landraud, L., Rolain, Jean-Marc. ARG-ANNOT, a New Bioinformatic Tool To Discover Antibiotic Resistance Genes in Bacterial Genomes. Antimicrobial Agents and Chemotherapy, Vol. 58 Number 1, p. 212–220 (2014). doi:10.1128/AAC.01310-13
```
