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
            curr = {
                "details": str(row["cells"][0]["links"][0]["link"]),
                "gradebook": row["cells"][1]["text"],
                "term": row["cells"][2]["text"],
                "period": row["cells"][3]["text"],
                "teacher": row["cells"][4]["text"],
                "grade_percent": row["cells"][5]["text"].encode('ascii', 'ignore'),
                "letter_grade": row["cells"][6]["text"].encode('ascii', 'ignore'),
                "missing_assignments": row["cells"][7]["text"],
                "updated_date": row["cells"][8]["text"],
                "status": row["cells"][9]["text"],
                "prior_term": prior_term,
            }
            grades.append(curr)
            i += 1
    return grades


def getGradesTable(html):
    return html.find("table", bordercolor="White")
