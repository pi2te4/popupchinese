Popup Chinese New HSK Vocabulary List
Permission is warmly given to redistribute these materials provided a link is provided to Popup Chinese as the source.
http://popupchinese.com/hsk/test


Introduction
------------

Scripts for building a learner's dictionary from the Popup Chinese New HSK Vocabulary List.


Files
-----

NewHSKLevel*	Popup Chinese New HSK Vocabulary List
mkdict.py	Convert NewHSKLevel* into XML dictionary (Python program)
userdict.xsl 	Convert XML dictionary into Pleco user dictionary (XSLT program)
dict.xsd	XML dictionary schema


Usage examples
--------------

Build XML dictionary
	./mkdict.py > popupchinese.xml

Build Pleco user dictionary file
	xsltproc userdict.xsl popupchinese.xml > popupchinese.txt
