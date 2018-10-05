'''
Write a program that generates a HTML webpage. 
Prompt the user for webpage title and webpage body contents. 
The webpage body should contain 
 - one main header, 
 - one sub header, and 
 - at least 2 paragraphs.
'''

template = '''
			Webpage.html
<html>
	<head>
		<title>
			{MyWebpagetitle}
		</title>
	</head>
	
	<body>
		<h1>Webpage Banner</h1>
		
		<p>This is a sample story
		   for my first webpage
		</p>
		
		<p>This is a how my sample
		   story ends
		</p>
	</body>
</html>'''

MyWebpagetitle = input("Enter webpage title:\n")
htmlwebpage = template.format(**locals())
print(htmlwebpage)
#print(f"{template}")
