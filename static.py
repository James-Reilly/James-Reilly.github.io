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
	tempPath = "templates"
	prjNames = getProjectNames(textPath)
	for prj in prjNames:
		html = getPostsHtml(textPath, prj)
		addContent(tempPath, htmlPath, prj, html)


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

def addContent(templatePath, projectPath, projectName, html):
	templateFile = open(templatePath +"/"+ projectName + "Template.html", 'r')
	data = templateFile.read()
	data = data.replace("[content]", html)
	outputFile = open(projectPath +"/"+ projectName + ".html", 'w')
	outputFile.write(data)

main()
