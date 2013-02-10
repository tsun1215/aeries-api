#Puts grade information from http://abi.ausdk12.org/abi/GradebookSummary.asp into dictionaries and prints it
#!/usr/bin/python
#Library containing functions fromTo and loadFile (see file for descriptions)
import locallib
#Regular expression library
import re
def run():
	#BS object for saved page
	grades_html = locallib.loadFile("GradebookSummary.asp")
	#List for grades
	grades = ["Unused"]
	#Initializes grades being from a prior term to false
	prior_term = "False"
	#Iterates through each tr in file
	for row in grades_html.find_all("tr"):
		#Finds start of prior term grades
		if (str(row.get("class")) != "None" and row.get("class")[0] == "HeaderRowBold" and row.get_text() == "Prior Terms"):
			prior_term = "True"
		#Pulls grade information from each td with grade information
		if (str(row.get("onclick")) != "None" and str(re.search("window.location = 'GradebookStuScores.asp", row.get("onclick")[0])) == "None"):
			grades.append({})
			#Table entries in order left to right
			table_entries = ["Details", "Gradebook", "Term", "Period", "Teacher", "Grade Percentage", "Grade", "Missing Assignments", "Last Updated", "Status"]
			i = 0
			#Iterates over each td in assignments, adding them by table_entries name to a dictionary in grades
			for entry in row.find_all("td"):
				if (table_entries[i] == "Details"):
					grades[len(grades)-1][table_entries[i]] = entry.find("a").get("href")
				else:
					grades[len(grades)-1][table_entries[i]] = entry.get_text()
				i += 1
			grades[len(grades)-1]["Prior Term"] = prior_term
	#Prints contents of grades (for testing purposes)
	for item1 in grades:
		if (item1 == "Unused"):
			continue
		for item2 in item1:
			print item2 + ": " + item1[item2]
run()
