##  script file : output2html_inc.py
##  it containes functions to simplify the work of the script output2html.py

endif = None

####################################################################

def beginPage(pageFileName) :

####################################################################

   import time

   fileObj      = open(pageFileName,"w")

   fileObj.write('''<!doctype html>
   <html lang='fr'>

   <head>
      <meta charset="UTF-8" />
      <title> interpretation of the outputs of PREDIPATH script </title>
      <link rel="stylesheet" type="text/css" href="std.css" title="gh" />
   </head>

   <body>
   <blockquote><!-- global -->

   <h1> Interpretation of the outputs of PREDIPATH script</h1>
   ''')

   fileObj.write('<p>Date: '+time.strftime('%d/%m/%y',time.localtime())+'; time: '+time.strftime('%H:%I',time.localtime())+'.</p>\n')

   fileObj.write('<h2>Your text results:</h2>\n')

   fileObj.close()

# fin de fonction beginPage

####################################################################

def endPage(pageFileName) :

####################################################################

   fileObj      = open(pageFileName,"a")

   fileObj.write('''
   </blockquote><!-- global -->
   </body>
   </html>
   ''')

   fileObj.close()

# fin de fonction endPage

####################################################################

def writeFileInPage(fileToInclude,pageFileName) :

####################################################################

   import os
   import re

   fileObj      = open(pageFileName,"a")
   fileObj.write('<pre class="cadre">\n')

   if (not os.path.isfile(fileToInclude)) :
      fileObj.write('\n FILE " + fileToInclude + " NOT FOUND \n')
   else :
      with open(fileToInclude) as fd :
        defClasses = 0
        classes    = {}
        short      = {}
        long       = {}
        nbClasses  = 0
        for line in fd.readlines() :

           fileObj.write( "    " + line )

           rep = re.search("^Input file:(?P<name>.*)",line)
           if rep :
               genomeFile = rep.group('name').strip()

           rep = re.search("^Genus:(?P<genre>.*)",line)
           if rep :
               genusDb = rep.group('genre').strip()

           if defClasses==1 :
              if line.strip()=="" :
                 defClasses = 0
              else :
                 nbClasses  += 1
                 classes[ nbClasses ] = line
                 short[ nbClasses ], long[ nbClasses ] = line.split("=")

           if re.search("^Classes:",line) :
               defClasses = 1

        fileObj.write( "\n\n" )
   endif # fin de si

   fileObj.write('</pre>\n')

   fileObj.write('<h2>Informations</h2>\n')
   fileObj.write('<blockquote>\n')
   fileObj.write('<p>Your genome was read in the file: '+bleu(genomeFile)+'</p>\n')
   fileObj.write('<p>You are working with genus: '+bleu(genusDb)+'</p>\n')
   fileObj.write('<p>'+rouge(str(nbClasses))+' classes are defined:</p>\n')
   for icl in classes :
       fileObj.write('<p> - class ' +bleu(str(icl)) + ' short name: ' + rouge(short[icl]) + ' long name: ' + vert(long[icl]) + '</p>\n')
   fileObj.write('</blockquote>\n')

   fileObj.close()

   return([nbClasses,genomeFile,genusDb,short,long])

# fin de fonction writeFileInPage

####################################################################

def writeHtml(pageFileName,htmlText) :

####################################################################

   fileObj      = open(pageFileName,"a")
   fileObj.write(htmlText)
   fileObj.close()

# fin de fonction writeHtml

####################################################################

def bleu(htmlText) :

####################################################################

  return("<span class='gbleuf'>" + htmlText + "</span>")

# fin de fonction bleu

####################################################################

def rouge(htmlText) :

####################################################################

  return("<span class='grougef'>" + htmlText + "</span>")

# fin de fonction rouge

####################################################################

def vert(htmlText) :

####################################################################

  return("<span class='gvertf'>" + htmlText + "</span>")

# fin de fonction vert

####################################################################

def explainBlock(nClasses,theBlock,pageFileName,number,leGenre) :

####################################################################

  import PyQt5
  import pandas  as pd
  import seaborn as sns
  import os
  import os.path

  hText   = "<h2>Explanation of results for the block: " + theBlock[0] + "</h2>\n "
  hText  += "<blockquote>\n"

  # the text

  class1, pct1, hText1 = describeClass(theBlock[1],theBlock[2])
  class2, pct2, hText2 = describeClass(theBlock[1],theBlock[3])
  pcts    = [pct1,pct2]
  classes = [class1,class2]
  hText  += hText1
  hText  += hText2
  if nClasses==2 :
     hText  += therefore2(pct1,pct2,[class1,class2],leGenre)
  else :
     class3, pct3, hText3 = describeClass(theBlock[1],theBlock[4])
     pcts    = [pct1,pct2,pct3]
     classes = [class1,class2,class3]
     hText  += hText3

  # the image

  sns.set(style="white")
  clasRes = pd.DataFrame(data={'Classes':classes,'Percentages':pcts})
  bp = sns.barplot(x="Classes",y="Percentages",data=clasRes)
  bp.set_title("Percentages of markers per class\n")
  bp.set(ylim=(0,105))
  fig = bp.get_figure()
  figName = "barplot" + str(number) + ".png"
  if os.path.isfile(figName):
     os.remove(figName)
  fig.savefig( figName, dpi=600)
  fig.clear()
  del fig
  del bp
  del clasRes

  hText  += "\n<img src='" + figName +"' alt='" + figName + "' width='800' />\n"
  hText  += "</blockquote>\n"

  writeHtml(pageFileName,hText)

# fin de fonction explainBlock

####################################################################

def describeClass(headers,values) :

####################################################################

  headersList = headers.split(',')
  valuesList  = values.split(',')
  classe      = valuesList[0]
  pct         = valuesList[3]

  explainTxt  = "<p>\n"
  explainTxt += " Class " + bleu(classe) + " is defined by " +  vert(valuesList[1]) + " markers.\n"
  explainTxt += " Your query genome has " + rouge(valuesList[2]) + " of these makers, which represents " + rouge(pct) + " of the markers.\n"
  explainTxt += "</p>\n"

  if (pct[len(pct)-1]=="%") :
     pct = pct[0:len(pct)-1]

  pct = float(pct)

  return([classe,pct,explainTxt])

# fin de fonction describeClass

####################################################################

def therefore2(p1,p2,classes,leGenre) :

####################################################################

  probably  = [10,90]
  likely    = [20,80]
  notEnough = 30
  c1 = rouge(classes[0])
  c2 = rouge(classes[1])

  interpretationTxt  = "<p><em>\n"
  interpretationTxt += "Therefore, "

  phraseInter = " it is not clear whether your genome belongs to class " + c1 + " or " + c2

  if (p1>=likely[1]) and (p2<=likely[0]) :
      phraseInter = " your genome belongs more likely to class " + c1
  if (p2>=likely[1]) and (p1<=likely[0]) :
      phraseInter = " your genome belongs more likely to class " + c2

  if (p1>=probably[1]) and (p2<=probably[0]) :
      phraseInter = " your genome belongs probably to class " + c1
  if (p2>=probably[1]) and (p1<=probably[0]) :
      phraseInter = " your genome belongs probably to class " + c2

  if (p1<=notEnough) and (p2<=notEnough) :
      phraseInter  = " your genome is difficult to classify as belonging to class " + c1 + " or " + c2 + "."
      phraseInter += " We suggest to check if your genome really belongs to the genus " + bleu(leGenre) + "."

  interpretationTxt += phraseInter
  interpretationTxt += ".</em></p>\n"

  return(interpretationTxt)

# fin de fonction therefore2

