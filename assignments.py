#Puts assignment information from http://abi.ausdk12.org/abi/GradebookActive.asp into dictionaries and prints it
#!/usr/bin/python
#Library containing functions fromTo and loadFile (see file for descriptions)
import locallib
#Regular expression library
import re
def run():
	#BS object for saved page
	assignments_html = locallib.loadFile("GradebookActive.asp")
	#List for assignments
	assignments = ["Unused"]
	#Initially set due date for assignments to nothing
	current_due_date = ""
	#Iterates through each tr in file
	for row in assignments_html.find_all("tr"):
		if (str(row.get("class")) != "None"):
			#Finds due date for the next group of assignments
			if (row.get("class")[0] == "NormalRow"):
				current_due_date = locallib.fromTo("Assignments Due: ","",row.get_text())
			#Pulls assignment information from each td with assignment information (some assignments seperated into two tr)
			elif (row.get("class")[0] == "NormalRowEven" and str(row.get("id")) != "None"):
				#A rows
				if (str(re.search("b", row.get("id"))) == "None"):
					#Assignment Number (from tr id)
					ass_num = int(locallib.fromTo("Row","",row.get("id")))
					#Table entries in order left to right
					table_entries = ["Period","Subject","Assigment Number","Description","Attachment","Type","Assigned","Due Time","Max Points"]
					assignments.insert(ass_num, {})
					i = 0
					#Iterates over each td in assignments, adding them by table_entries name to a dictionary in assignments
					for entry in row.find_all("td"):
						assignments[ass_num][table_entries[i]] = entry.get_text()
						i += 1
					assignments[ass_num]["Due Date"] = current_due_date
					assignments[ass_num]["Long Description"] = "None"
				#B rows (long descriptions)
				else:
					ass_num = int(locallib.fromTo("Row","b",row.get("id")))
					assignments[ass_num]["Long Description"] = row.get_text()
	#Prints contents of assignments (for testing purposes)
	for item1 in assignments:
		if (item1 == "Unused"):
			continue
		for item2 in item1:
			print item2 + ": " + item1[item2]
run()
