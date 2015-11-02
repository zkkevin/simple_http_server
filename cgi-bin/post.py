__author__ = 'z00152000'

import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()

print("Content-Type: text/html")

print("\r\n")

print("<p>Hello baby girl %s.</p>" %form.getvalue("firstname"))

