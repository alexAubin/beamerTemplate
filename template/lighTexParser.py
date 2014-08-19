#! /usr/bin/env python2.6
 
"""
This program does something.
"""
 
import sys
import os
import re
import argparse
 
#############
# Open file #
#############

with open("../slides.ltex","r") as inputFile :
    inputText = inputFile.read()

#################
# Apply regexes #
#################

''' Underline, bold, italic '''
inputText = re.sub(r"_([a-zA-Z0-9\s]*)_", "\underline{\\1}",inputText)
inputText = re.sub(r"\*(.*?)\*", r"\\textbf{\1}",inputText)

''' Title and subtitle, author, date and institue '''

titleMatch     = re.search("\n===*\n(.*?)\n===*\n(.*?)\n---*\n",      inputText)
dateMatch      = re.search("\nDate      : (.*?) \((.*?)\)\n",         inputText)
authorMatch    = re.search("\nAuthor    : (.*?)\n",                   inputText)
instituteMatch = re.search("\nInstitute : (.*?) \((.*?)\)\n",         inputText)

inputText      = re.sub(   "\n===*\n(.*?)\n===*\n(.*?)\n---*\n",  "", inputText)
inputText      = re.sub(   "Date      : (.*?) \((.*?)\)\n",       "", inputText)
inputText      = re.sub(   "Author    : (.*?)\n",                 "", inputText)
inputText      = re.sub(   "Institute : (.*?) \((.*?)\)\n",       "", inputText)

''' Sections and subsections '''
inputText = re.sub(r"\[SlideOutline\]\n", "\n\printOutline\n",inputText)
inputText = re.sub(r"\n(.*?)\n===*\n", "\n\section{\\1}\n",inputText)
inputText = re.sub(r"\n(.*?)\n---*\n", "\n\subsection{\\1}\n",inputText)

''' Bracket -> Slides '''
inputText = re.sub(r"\n\[\n","\n\slide\n{\n",inputText)
inputText = re.sub(r"\n\]\n","\n}\n",inputText)

''' Math mode '''
inputText = re.sub(r"`(.*?)`", "$\\1$",inputText)

''' Images, plots and tables syntax '''
inputText = re.sub(r"\[Img\]\((.*?)\)\((.*?)\)",  "\imgw{\\1}{\\2}",inputText)
inputText = re.sub(r"\[Plot\]\((.*?)\)\((.*?)\)", "\pdfw{\\1}{\\2}", inputText)
inputText = re.sub(r"\[Tab\]\((.*?)\)",           "\input{../imgAndTables/\\1}",inputText)

''' Items '''
inputText = re.sub(r"    - (.*?)\n", "BEGINITEMIZE        \item \\1    ENDITEMIZE\n",inputText)
inputText = re.sub(r"\t- (.*?)\n"  , "BEGINITEMIZE        \item \\1    ENDITEMIZE\n",inputText)
inputText = re.sub(r"ENDITEMIZE\nBEGINITEMIZE"  , "\n",inputText)
inputText = re.sub(r"BEGINITEMIZE"  , r"    \\begin{itemize}\n",inputText)
inputText = re.sub(r"ENDITEMIZE"    , r"\n    \\end{itemize}",inputText)

''' Arrow '''
inputText = re.sub(r"=>", r"$\\Rightarrow$",inputText)

''' Bigksip when three empty lines '''
inputText = re.sub(r"\n\n\n\n", r"\n\n    \\bigskip\n\n",inputText)

print ""
print "\\title{"+titleMatch.group(1)+"}"
print "\\subtitle{"+titleMatch.group(2)+"}"
print ""
print "\\author{"+authorMatch.group(1)+"}"
print "\\date["+dateMatch.group(2)+"]{"+dateMatch.group(1)+"}"
print "\\institute["+instituteMatch.group(2)+"]{"+instituteMatch.group(1)+"}"
print ""
print "\\begin{document}"
print ""
print "\\printTitle"
print ""
print inputText
print ""
print "\\end{document}"

'''
// bold, italics, and code formatting
r = r.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
r = r.replace(new RegExp('//(((?!https?://).)*?)//', 'g'), '<em>$1</em>')
r = r.replace(/``(.*?)``/g, '<code>$1</code>')

// links
r = r.replace(/\[\[(http:[^\]|]*?)\]\]/g, '<a target="_blank" href="$1">$1</a>')
r = r.replace(/\[\[(http:[^|]*?)\|(.*?)\]\]/g, '<a target="_blank" href="$1">$2</a>')
r = r.replace(/\[\[([^\]|]*?)\]\]/g, '<a href="$1">$1</a>')
r = r.replace(/\[\[([^|]*?)\|(.*?)\]\]/g, '<a href="$1">$2</a>')

// video
r = r.replace(/<<(.*?)>>/g, '<embed class="video" src="$1" allowfullscreen="true" allowscriptaccess="never" type="application/x-shockwave/flash"></embed>')

// hard linebreak if there are 2 or more spaces at the end of a line
r = r.replace(new RegExp(' + ' + newline, 'g'), '<br>' + newline)
'''

