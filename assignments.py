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
                current_due_date = locallib.fromTo("Assignments Due: ", "", row["cells"][0]["text"])
            elif (locallib.attrContains(row["attributes"],  "class",  "NormalRowEven") and str(row["attributes"]["id"]) != "None"):
                #B rows (long descriptions)
                if (locallib.attrContains(row["attributes"],  "id",  "b")):
                    ass_num = int(locallib.fromTo("Row", "b", row["attributes"]["id"])) - 1
                    assignments[ass_num]["Long Description"] = row["cells"][0]["text"]
                #A rows
                else:
                    ass_num = int(locallib.fromTo("Row", "", row["attributes"]["id"])) - 1
                    curr = {
                        "period": row["cells"][0]["text"],
                        "subject": row["cells"][1]["text"],
                        "a_num": row["cells"][2]["text"],
                        "descip": row["cells"][3]["text"],
                        "attachements": row["cells"][4]["text"],
                        "type": row["cells"][5]["text"],
                        "date_assigned": row["cells"][6]["text"],
                        "due_time": row["cells"][7]["text"].encode('ascii', 'ignore'),
                        "max_points": row["cells"][8]["text"].encode('ascii', 'ignore'),
                        "due_date": current_due_date,
                        "long_descip": "",
                    }
                    assignments.append(curr)
    return assignments


def getAssignmentsTable(html):
    return html.find("table",  bordercolor="White")
