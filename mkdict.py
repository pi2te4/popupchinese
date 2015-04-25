#!/usr/bin/python
# -*- coding: utf-8 -*-

import unicodedata
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

level_table = {
	1:'一',
	2:'二',
	3:'三',
	4:'四',
	5:'五',
	6:'六'
	}

pos_table = {
	'noun':'名',
	'verb':'动', 'noun (verb)':'动',
	'auxiliary':'助',
	'adjective':'形', 'noun (adjective)':'形',
	'numeral':'数',
	'measure word':'量', 'classifier':'量', 'noun (measure word)':'量',
	'interjection':'叹', 'int':'叹',
	'pronoun':'代', 'pronouns':'代',
	'adverb':'副',
	'preposition':'介',
	'conjunction':'连',
	'phrase':'固定词组',
	'other':'？'
	}

print '<?xml version="1.0" encoding="utf-8"?>'
print '<dict>'
print '<!--Popup Chinese New HSK Vocabulary List-->'
print '<!--Permission is warmly given to redistribute these materials provided a link is provided to Popup Chinese as the source.-->'
print '<!--http://popupchinese.com/hsk/test-->'
for level in range(1,7):
	with open('NewHSKLevel%i.txt'%level) as fp:
		fp.readline()
		fp.readline()
		for line in fp:
			n, simplified, traditional, pinyin, english, pos = line.decode('utf-8').rstrip().split("\t")
			if (pos == 'other') and len(simplified) == 4:
				pos = 'phrase'
			if (not(pos_table.has_key(pos))):
				print 'pos "%s" missing'%pos
				exit()
			print '<entry level="%s" simplified="%s" traditional="%s" pinyin="%s">'%(level_table[level], simplified, traditional, pinyin)
			print '\t<def type="%s">%s</def>'%(pos_table[pos], english)
			print '</entry>'
print '</dict>'
