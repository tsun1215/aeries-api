import grades
import assignments
import login
import locallib
def main(user_name, password):
	login.login(user_name, password)
	grades_py = grades.getGrades("GradebookSummary.asp")
	assignments_py = assignments.getAssignments("GradebookActive.asp")
	grades_json = locallib.toJSON(grades_py)
	assignments_json = locallib.toJSON(assignments_py)
	return {"grades": grades_json, "assignments": assignments_json}
user_name = raw_input("User Name: ")
password = raw_input("Password: ")
json = main(user_name, password)
for page in json:
	print page + ":\n" + json[page]
