#!/usr/bin/env python

"""
using a table of equivalent code_table, the script changes search for your code and substitutes 
by the corresponding code that you desire in your table

it serves for any file that you wan to change names, code_table, strings.

User needs to redirect the output to a file

usage: rename_tree.py [matrix_file] [code_table] [code_table old_name] [code_table new_name] > [output_file]


# For example:
	If you have TableA and TableB, and want to substitute the accession number in TableB to their corresponding code in TableA.
	
Table_A - table with names to be changed:

	[col1]	[col2]	[col3]
	Name_1	0,005	Erwinia sp. st1
	Name_2	0,002	Erwinia sp. st2
	Name_3	0,001	Erwinia sp. st3
	Name_4	0,003	Erwinia sp. st4

Table_A' - table with names to be changed:

	[col1]	[col2]	[col3]
	P-Name_1	0,005	Erwinia sp. st1
	P-Name_2	0,002	Erwinia sp. st2
	P-Name_3	0,001	Erwinia sp. st3
	P-Name_4	0,003	Erwinia sp. st4


Table_B with names to be modified:

	[col1]	[col2]	[col3]
	P-Name_1	Name_1	GCF_1
	P-Name_2	Name_2	GCF_2
	P-Name_3	Name_3	GCF_3
	P-Name_4	Name_4	GCF_3

Outputs:

	For Table A, if you want to change the names in the first column, you need to identify them
	in the corresponding columns of Table B. In this case, the first column of Table A corresponds to column 2 of Table B.
	If I want to change the names from column 2 to names in column 1, the command would be:

		rename_names.py Table_A Table_B 2 1 > [output_file]

			P-Name_1	0,005	Erwinia sp. st1
			P-Name_2	0,002	Erwinia sp. st2
			P-Name_3	0,001	Erwinia sp. st3
			P-Name_4	0,003	Erwinia sp. st4

		rename_names.py Table_A Table_B 2 3 > [output_file]

			GCF_1	0,005	Erwinia sp. st1
			GCF_2	0,002	Erwinia sp. st2
			GCF_3	0,001	Erwinia sp. st3
			GCF_4	0,003	Erwinia sp. st4


"""

import string
import sys

# Checks if in proper number of arguments are passed gives instructions on proper use.
def argsCheck(numArgs):
	if len(sys.argv) < numArgs or len(sys.argv) > numArgs:
		#print "Developed by: Felipe Lira\n"
		print "\nUsage:\n\t" + sys.argv[0] + " [matrix_file] [code_table] [code_table old_name] [code_table new_name] > [output_file]\n"
		exit(1) # Aborts program. (exit(1) indicates that an error occurred)

argsCheck(5) # Checks if the number of arguments are correct.



input_tree = open(sys.argv[1], "r")

code_table = open(sys.argv[2], "r")

#tree = input_tree.read().replace('.gbff', '')
infile = input_tree.read()

# number of the column with the name you want to change
old_name = int(sys.argv[3])

# number of the column that contains the new name that you want to susbstitute
new_name = int(sys.argv[4])
print new_name

d = {}

for line in code_table:

	old = 0 # int(old_name - 1)
	new = int(new_name - 1)

	#print line.strip()

	k = line.strip().split("\t")[old]
	#print k
	v = line.strip().split("\t")[new] # .replace('_',' ')
	#print v
	#print k, v
	if k not in d:
		d[k] = str(v)
	else:
		continue

for k, v in d.iteritems():
	#for l in tree:
	infile = string.replace(infile, k, v)
	#tree = string.replace(tree, v, k)
print infile

