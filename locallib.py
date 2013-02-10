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
#Returns BS object from file_name file
def loadFile(file_name):
	from bs4 import BeautifulSoup
	f = open(file_name, 'r')
	soup = BeautifulSoup(f.read())
	return soup
