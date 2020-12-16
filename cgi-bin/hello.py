#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
first_name = form.getvalue('first_name')
last_name  = form.getvalue('last_name')

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello</title>")
print ("</head>")
print ("<body>")
print ("<h2>%s %s,welcome! this is a python cgi example.haha</h2>" % (first_name, last_name))
print ("</body>")
print ("</html>")

