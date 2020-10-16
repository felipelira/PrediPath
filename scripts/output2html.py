### Script output2html.py

## this script builds a HTML5 page to interpret
## the results if the predipath_user_0.04.py script

import sys
import os
import re
import PyQt5
import pandas  as pd
import seaborn as sns

from output2html_inc import *

endif = None # to be more readable

# let's print the help text if no args arge given

if (len(sys.argv)==1) :

    aide = '''

    output2html.py: interpretation of the outputs of PREDIPATH script

    syntax:  python3 output2html.py FILE
    example: python3 output2html.py outputGenome45.txt
    '''
    print(aide)
    sys.exit()

endif # fin de si

# so now we are able to read the results file

resFile = sys.argv[1]

## let's begin the Web page

pageFileName = "output2html.html"

beginPage(pageFileName)

## let's print all the file, so it will be easier to understand how to interpret the results

nbc, genomeFile, genre, shortNames, longNames = writeFileInPage(resFile,pageFileName)

##  now, we have to detect and process all blocks such as
##
##  Search of specific k-mers
##    Classes,Kmers_per_class,Query_genome,Percent
##    PP,5167,5165,99.96%
##    NPP,1262,466,36.93%

# first read the file and transfer it into a list

with open(resFile) as fh :
     lines = fh.read().splitlines()
# fin de with open

# search for the beginning of the block
# when found, explain the block
# by the way, show file name and genus database name

idl = -1
nbl =  0 # block number
for line in lines :
  idl += 1
  if re.search("^Search of ",line) :
     nbl += 1
     explainBlock(nbc, lines[ idl : (idl+nbc+2) ],pageFileName,nbl,genre)
# fin de for idl

## finally, let's end the Web page

endPage(pageFileName)

### end of script
