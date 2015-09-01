import markdown
import os
'''
This file is to convert my markdown posts into the appropriate HTMl pages
author @James Reilly
'''


def convert_to_html(filename, path):
	input_file = open(path + "/" + filename, 'r')
	text = input_file.read()
	html = markdown.markdown(text, ['markdown.extensions.extra', 'markdown.extensions.attr_list'])
	return html

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
	for fn in os.listdir("./" + path +'/'+ projectName):
		if(fn.endswith(".txt")):
			myhtml += convert_to_html(fn, path + "/" + projectName)
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

	data = data.replace("[content]", html)
	data = data.replace("[navbar]", navbar)
	data = data.replace("[header]", header)
	data = data.replace("[footer]", footer)
	outputFile = open(projectPath +"/"+ projectName + ".html", 'w')
	outputFile.write(data)

main()
