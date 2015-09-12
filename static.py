import markdown
import datetime
import os
'''
This file is to convert my markdown posts into the appropriate HTMl pages
author @James Reilly
'''

class ProjectPost:
	def __init__(self, date, html):
		self.date = date
		self.html = html

def convert_to_html(filename, path):
	input_file = open(path + "/" + filename, 'r')
	date = ""
	text = ""
	first = True
	for line in input_file:
		if(first):
			date = line.strip()
			first = False
		else:
			text += line
	html = markdown.markdown(text, ['markdown.extensions.extra', 'markdown.extensions.attr_list'])
	return ProjectPost(date, html)

def main():
	textPath = "markdownProjects"
	htmlPath = "projects"
	componentPath = "components"
	headerPath ="headers"
	prjNames = getProjectNames(textPath)
	for prj in prjNames:
		html = getPostsHtml(textPath, prj)
		addContent(componentPath, headerPath, htmlPath, prj, html)


def getPostsHtml(path, projectName):
	myhtml = ""
	curPath = "./" + path +'/'+ projectName;
	postList = []
	for fn in os.listdir(curPath):
		if(fn.endswith(".txt")):
			postList.append(convert_to_html(fn, path + "/" + projectName))
	#sort by date
	postList.sort(key=lambda post: datetime.datetime.strptime(post.date, '%Y-%m-%d'), reverse=True)
	for post in postList:
		myhtml += post.html
	return myhtml

def getProjectNames(path):
	projectNames = []
	for direct in os.listdir("./" + path):
		if(os.path.isdir("./" + path + "/" + direct)):
			projectNames.append(direct)
	return projectNames

def addContent(componentPath, headerPath, projectPath, projectName, html):
	#Open all the compnents needed to create a project page
	templateFile = open(componentPath + "/projectShell.html", 'r')
	navbarFile = open(componentPath + "/navbar.html", 'r')
	footerFile = open(componentPath + "/footer.html", 'r')
	headerFile = open(headerPath + "/" + projectName + "Header.html", 'r')
	#Read all the date from the files
	header = headerFile.read()
	navbar = navbarFile.read()
	footer = footerFile.read()
	data = templateFile.read()

	#replace tags with acutal content
	data = data.replace("[content]", html)
	data = data.replace("[navbar]", navbar)
	data = data.replace("[header]", header)
	data = data.replace("[footer]", footer)
	#write the data to the apporiate files
	outputFile = open(projectPath +"/"+ projectName + ".html", 'w')
	outputFile.write(data)

main()
