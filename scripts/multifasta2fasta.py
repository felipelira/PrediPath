#!/usr/bin/env python
from Bio import SeqIO
import sys
import os
import zipfile
import shutil, random, string

"""
Description

multifasta2fasta.py converts a multi.fasta file to single.fasta files.


"""
# usage: multifasta2fasta.py [multifasta_file] [output_name]


# define KEY_LEN
KEY_LEN = 10

strings = string.letters + string.digits
code_list = [random.choice(strings) for i in range(KEY_LEN)]
code = "".join(code_list)
# uses the name of the input file to create the output folder where the files will be stored

in_file = sys.argv[1] 
out_dir = './' + in_file + '_output_dir'

os.mkdir(out_dir)

zip_file = sys.argv[2]

# read the multifasta file
fasta_sequences = SeqIO.parse(open(sys.argv[1]),'fasta')

for rec in fasta_sequences:
	id = rec.id
	seq = rec.seq
	id_file = open(os.path.join(out_dir,id + '.fasta' ), "w") 
	new_sequence = ">"+str(rec.description)+"\n"+str(seq)
	id_file.write(new_sequence)
	id_file.close()
fasta_sequences.close()

# zip files
zf = zipfile.ZipFile( zip_file + code + ".zip" , "w")
for dirname, subdirs, files in os.walk(out_dir):
    zf.write(dirname)
    for filename in files:
        zf.write(os.path.join(dirname, filename))
zf.close()

shutil.rmtree(out_dir)

