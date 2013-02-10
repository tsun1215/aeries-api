#Logs in as user and downloads relevant pages
#!/usr/bin/python
import mechanize
#Input to be replaced with function call (for testing)
UserName = raw_input("User Name: ")
Password = raw_input("Password: ")
BaseAddress = "http://abi.ausdk12.org/abi/"
Login = "LoginHome.asp"
#Relevant pages
Pages = ["GradebookActive.asp","GradebookSummary.asp"]
br = mechanize.Browser()
br.open(BaseAddress+Login)
br.select_form("frmLogin")
br["UserName"] = UserName
br["Password"] = Password
Home = br.submit()
#Saves pages in current directory
for item in Pages:
	response = br.open(BaseAddress+item)
	f1 = open(item, 'w')
	f1.write(response.read())
	f1.close
