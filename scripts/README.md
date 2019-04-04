# README
Suplementary scripts used to standarize the input files used by PrediPath and post-process the output files.

## Scripts description:

    # gbk2faa.py
        Extract the proteomes from .gbk (.gbff) files. Resulting file is used by PrediPath.
        
    # multifasta2fasta.py
        Convert a multifasta file to single .fasta files.
        
            multi.fasta
            >seq1
            AGTCGTACGTATACTGA
            >seq2
            ACGTGCTGATGCATCCATCG
            >seq3
            AATCTCGCTGATCGTCAGTAGC
            
            seq1.fasta
            >seq1
            AGTCGTACGTATACTGA
            
            seq2.fasta
            >seq1
            ACGTGCTGATGCATCCATCG
