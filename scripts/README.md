# README
Suplementary scripts used to standarize the input files used by PrediPath and post-process the output files.

## Scripts description:
### gbk2faa.py
        Extract the proteomes from .gbk (.gbff) files. Resulting file is used by PrediPath.
### multifasta2fasta.py
        Convert a multifasta file to single .fasta files and save it in a .zip file
```
               multi.fasta                    |            seq1.fasta
               >seq1                          |            >seq1
               AGTCGTACGTATACTGA              |            AGTCGTACGTATACTGA
               >seq2                          |----> 
               ACGTGCTGATGCATCCATCG           |            seq2.fasta
               >seq3                          |            >seq2
               AATCTCGCTGATCGTCAGTAGC         |            ACGTGCTGATGCATCCATCG
                           
                                                           seq3.fasta
                                                           >seq3
                                                           AATCTCGCTGATCGTCAGTAGC
```
                                              

