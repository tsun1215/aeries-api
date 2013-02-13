import locallib
def getAssignments(assignments_file):
	html = locallib.loadFile(assignments_file)
	html_table = getAssignmentsTable(html)
	table = locallib.getTable(html_table)
	assignments = []
	current_due_date = ""
	for row in table["rows"]:
		if ("class" in row["attributes"] and str(row["attributes"]["class"]) != "None"):
			if (row["attributes"]["class"][0] == "NormalRow"):
				current_due_date = locallib.fromTo("Assignments Due: ","",row["cells"][0]["text"])
			elif (locallib.attrContains(row["attributes"], "class", "NormalRowEven") and str(row["attributes"]["id"]) != "None"):
				#B rows (long descriptions)
				if (locallib.attrContains(row["attributes"], "id", "b")):
					ass_num = int(locallib.fromTo("Row","b",row["attributes"]["id"])) - 1
					assignments[ass_num]["Long Description"] = row["cells"][0]["text"]
				#A rows
				else:
					#Assignment Number (from tr id)
					ass_num = int(locallib.fromTo("Row","",row["attributes"]["id"])) - 1
					assignments.append({})
					assignments[ass_num]["Period"] = row["cells"][0]["text"]
					assignments[ass_num]["Subject"] = row["cells"][1]["text"]
					assignments[ass_num]["Assignment Number"] = row["cells"][2]["text"]
					assignments[ass_num]["Description"] = row["cells"][3]["text"]
					assignments[ass_num]["Attachment"] = row["cells"][4]["text"]
					assignments[ass_num]["Type"] = row["cells"][5]["text"]
					assignments[ass_num]["Assigned"] = row["cells"][6]["text"]
					assignments[ass_num]["Due Time"] = row["cells"][7]["text"]
					assignments[ass_num]["Max Points"] = row["cells"][8]["text"]
					assignments[ass_num]["Due Date"] = current_due_date
					assignments[ass_num]["Long Description"] = ""
	return assignments

def getAssignmentsTable(html):
	return html.find("table", bordercolor="White")
