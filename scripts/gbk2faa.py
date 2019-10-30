# usr/bin/env python

from Bio import SeqIO
import sys

gbk_filename = sys.argv[1]

faa_filename = gbk_filename.replace(".gbk", ".faa").replace(".gbff",".faa")

infile  = open(gbk_filename, "r")
outfile = open(faa_filename, "w")

for record in SeqIO.parse(infile, "genbank"):

    for seq_feature in record.features:
		if seq_feature.type=="source":
			source = seq_feature.qualifiers["organism"][0]
			try:
				strain = seq_feature.qualifiers["strain"][0]
			except:
				strain = "na"


		if seq_feature.type=="CDS":

            #assert len(seq_feature.qualifiers['translation'])==1
			if seq_feature.qualifiers.has_key("translation"):

				protein_id = seq_feature.qualifiers["protein_id"][0]

				locus = seq_feature.qualifiers['locus_tag'][0]

				outfile.write(">ID:%s|%s|%s|%s|%saa|%s\n%s\n" % (protein_id, source, strain, seq_feature.qualifiers['product'][0], record.name,str(len(str(seq_feature.qualifiers['translation'][0]))), seq_feature.qualifiers['translation'][0]))

            #outfile.write(">%s from %s\n%s\n" % (seq_feature.qualifiers['locus_tag'][0], record.name, seq_feature.qualifiers['translation'][0]))

outfile.close()
infile.close()
