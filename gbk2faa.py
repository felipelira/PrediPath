#!/usr/bin/env python
from Bio import GenBank
from Bio import SeqIO

from Bio.Alphabet import IUPAC
from Bio.Seq import Seq
 
#TODO include position and sense of gene

import sys

gbk_filename = sys.argv[1]
accession = ".".join(gbk_filename.split(".")[:-1])
print accession 
faa_filename = "%s_out.faa" % gbk_filename
faa_filename = sys.argv[1].replace(".gbk",".faa").replace(".gbff",".faa")

input_handle  = open(gbk_filename, "r")
output_handle = open(faa_filename, "w")

for seq_record in SeqIO.parse(input_handle, "genbank"):

	#print "Dealing with GenBank record %s" % seq_record.id

	for seq_feature in seq_record.features :
		if seq_feature.type=="source":
			source = seq_feature.qualifiers["organism"][0]
			try:
				strain = seq_feature.qualifiers["strain"][0]
			except:
				strain = "na"
			#print seq_feature.qualifiers["organism"], seq_feature.qualifiers["strain"]

		if seq_feature.type=="CDS":
			if seq_feature.qualifiers.has_key("translation"):
				#temp_seq = Seq(seq_feature.qualifiers["translation"][0], IUPAC.protein)
				protein_id = seq_feature.qualifiers["protein_id"][0]
				locus = seq_feature.qualifiers['locus_tag'][0]
				#output_handle.write(">ID:%s|%s|%s|%s\n%s\n" % (protein_id, locus, seq_feature.qualifiers['product'][0], seq_record.name, seq_feature.qualifiers['translation'][0]))

				output_handle.write(">ID:%s|%s|%s|%s|%s|%saa|%s\n%s\n" % (protein_id, source, strain, seq_feature.qualifiers['product'][0], seq_record.name,str(len(str(seq_feature.qualifiers['translation'][0]))), accession, seq_feature.qualifiers['translation'][0]))


output_handle.close()
input_handle.close()

#print "Done"
