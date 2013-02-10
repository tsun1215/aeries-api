#Finds assignments from calender at http://abi.ausdk12.org/abi/MainMenu.asp
#!/usr/bin/python
def run():
	from bs4 import BeautifulSoup
	import re
	file_name = raw_input("MainMenu Location: ")
	f = open(file_name, 'r')
	soup = BeautifulSoup(f.read())
	for link in soup.find_all("span"):
     		if (link.get("id") != None and re.search("CalEventLong", link.get("id")) != None):
			print "Full Text: " + link.get_text()
             		print "Date: " + getDate(link.get("id"))
             		print "Period: " + getPeriod(link.get_text())
             		print "Text: " + getText(link.get_text("|"))
			print "Link: " + getLink(link.get_text("|"))
def getDate(string):
     	return FromTo("_","_",string)
def getPeriod(string):
	return FromTo("d ","-",string)
def getText(string):
	return FromTo("- ","\n",FromTo("","|",FromTo("|","",string)))
def getLink(string):
	result = FromTo("|","",FromTo("|","",string))
	if (result != ""):
		return result
	else:
		return "None"
def FromTo(from_str,to_str,string):
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
run()
