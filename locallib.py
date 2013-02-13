#Provides shared functions
#Finds section of string contained between the first occurence of from_str and the next occurence to_str, non inclusive
def fromTo(from_str,to_str,string):
	start = 0
	if (from_str != ""):
		while (string[start:start+len(from_str)] != from_str and start < len(string)):
			start += 1
		start = start+len(from_str)
	if (to_str != ""):
		end = start
		while (string[end:end+len(to_str)] != to_str and end < len(string)):
			end += 1
	else:
		end = len(string)
	return string[start:end]

#Returns BS object from html file named
def loadFile(file_name):
	from bs4 import BeautifulSoup
	f = open(file_name, 'r')
	soup = BeautifulSoup(f.read())
	return soup

#Print items from an array of dictionaries
def printDictionaries(dictionaries):
	for item1 in dictionaries:
		for item2 in item1:
			print item2 + ": " + item1[item2]

#Checks whether an elements attribute contains the given phrase
def attrContains(tag, attribute, phrase):
	import re
	if (attribute in tag):
		if (type(tag[attribute]) == list):
			tag_value = tag[attribute][0]
		else:
			tag_value = str(tag[attribute])
	else:
		tag_value = "None"
	return (str(re.search(phrase, tag_value)) != "None")

#Returns a 3-dimensional list of table elements, position 0 of all is occupied by a dictionary of attributes (see below)
#(list) table: (dict) attributes
#              (list) rows      : (dict) attributes
#                                 (list) cells     : (dict) attributes
#                                                    (str)  text
#                                                    (list) links     : (dict) attributes
#                                                                       (str) link	
def getTable(html_table):
	table = {"attributes": html_table.attrs, "rows": []}
	i = 0
	for row in html_table.find_all("tr"):
		table["rows"].append({"attributes": row.attrs, "cells": []})
		j = 0
		for item in row.find_all("td"):
			table["rows"][i]["cells"].append({"attributes": item.attrs, "text": item.get_text(), "links": []})
			for link in item.find_all("a"):
				table["rows"][i]["cells"][j]["links"].append({"attributes": link.attrs, "link": link.get("href")})
			j += 1
		i += 1
	return table
