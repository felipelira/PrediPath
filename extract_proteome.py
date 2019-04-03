#!/usr/bin/env python

"""
directory = directory used to calculate the core and pangenome clusters

		usage: extract_proteome.py [directory]
"""

import sys, os, errno
import subprocess
import argparse
from Bio import SeqIO
from optparse import OptionParser

species = set()

#############  FUNCTIONS  #############
# EXTRACT PROTEOMES #
# read the names of clusters in 'intersection_t0.cluster_list'
def pipeline(directory):

	proteomes_list = []
	clusters_list = os.path.join(directory, "intersection_t0.cluster_list") # path for the file containing the names of clusters of homologues
	core = open(os.path.join(clusters_list), "r") # open and read the file containing the list of clusters
	proteomes = directory + "_proteomes" # name of output folder to store the core proteomes

	try:
		os.mkdir(proteomes)
	except:
		pass

	for line in core: # read each line of the text list
		if line.startswith('#'):
			next
		else:
			faa = line.strip() # faa = multifasta file with core proteins
			cluster = os.path.join(directory, faa) # create the path for the cluster file
			proteomes_list.append(cluster)	# add path to the cluster (fasta file) to the list 'proteomes'

	for faa_file in proteomes_list:
		sequences = []
		if os.path.isfile(faa_file):
			parse = SeqIO.parse(faa_file, "fasta")
			for record in parse:
				sequences.append(record.id)	# store the name of the sequence in the list (sequences)
				description = record.description
				split_desc = description.strip().replace(" |", "|").replace(" ", "_").split("|")
				spcs = "|".join([split_desc[1].replace("[", "").replace("]", ""),split_desc[2]])# define the species name
				species.add(spcs)

	# create file to save the species/strain proteomes in fasta format
	for sp in species:

		outfl = ( sp.split("/")[0] + "_proteome.faa" ).replace(" ","_") # outfile names for separated core proteomes
		proteome_core = open(os.path.join(proteomes,outfl), "w") # write proteome files

		for faa in proteomes_list:
			f = open( os.path.join(faa) , "r")	# read file in list proteomes
			parse = SeqIO.parse(faa, "fasta")

			for record in parse:
				d = record.description
				split_d = d.strip().replace(" |", "|").replace(" ", "_").replace("[", "").replace("]", "").split('|') #.replace("_^^", "") # .split("|")[0:3]
				ID = "|".join([split_d[1], split_d[2]])
				s = split_d[1].replace("[", "").replace("]", "")

				if sp in ID:
					#print sp, ID
					seq = ">" + "|".join(split_d).split('_^^')[0] + "\n" + str(record.seq) + "\n"

					proteome_core.write(seq)
		proteome_core.close()

# correct the name and path of the directory to be analyzed removing the '/' character if the path contains it.
def mode(folder):	
	if os.path.isdir(folder):

		if folder.endswith("/"):
			directory = "/".join(folder.strip().split("/")[0:])
			pipeline(directory)
		else:
			directory = "/".join(folder.strip().split("/")[0:])
			pipeline(directory)

#############  CODE  #############
if __name__ == '__main__':
	if len(sys.argv) == 2: # script.py [directory] [list_of_groups]
		mode(sys.argv[1])

	elif len(sys.argv) != 2:
		print len(sys.argv)

