import locallib
import re
#Returns grades in a list of dictionaries
def getGrades(grades_file):
	html = locallib.loadFile(grades_file)
	html_table = getGradesTable(html)
	table = locallib.getTable(html_table)
	grades = []
	prior_term = "False"
	i = 0
	for row in table["rows"]:
		if (len(row["cells"]) != 0 and "text" in row["cells"][0] and row["cells"][0]["text"] == "Prior Terms"):
			prior_term = "True"
		elif (locallib.attrContains(row["attributes"], "class", "NormalClickableRow")):
			grades.append({})
			grades[i]["Details"] = row["cells"][0]["links"][0]["link"]
			grades[i]["Gradebook"] = row["cells"][1]["text"]
			grades[i]["Term"] = row["cells"][2]["text"]
			grades[i]["Period"] = row["cells"][3]["text"]
			grades[i]["Teacher"] = row["cells"][4]["text"]
			grades[i]["Grade Percentage"] = row["cells"][5]["text"]
			grades[i]["Grade"] = row["cells"][6]["text"]
			grades[i]["Missing Assignments"] = row["cells"][7]["text"]
			grades[i]["Last Updated"] = row["cells"][8]["text"]
			grades[i]["Status"] = row["cells"][9]["text"]
			grades[i]["Prior Term"] = prior_term
			i += 1
	return grades

def getGradesTable(html):
	return html.find("table", bordercolor="White")
