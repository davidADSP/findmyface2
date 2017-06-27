#!/Users/davidfoster/.virtualenvs/globalai/bin/python

import cgi
import pyodbc
import cognitive_face as CF
import json
import cgitb

cgitb.enable()

form=cgi.FieldStorage()

print ("content-type:text/html\r\n")

print("\r\n")
print("""
	<html>
	<link rel="stylesheet" href="test3.css">
	<div class="titleBar">
		<h1>Thank you!</h1>
	</div>
""")

firstName=form.getvalue('firstName')
lastName=form.getvalue('lastName')
jobRole=form.getvalue('role')
company=form.getvalue('company')
skills=form.getvalue('skills')
wants=form.getvalue('wants')
#photo = form.getvalue('photo')

"""
if photo.filename:
	photo.filename=(lastName+firstName+".jpg")
	fn = os.path.basename(photo.filename)
	open('img/'+fn, 'wb').write(photo.file.read())
"""
print "test"
#Add person to Person Group
KEY = '77abe08c92574606aa8aa15b3c987e7f'
CF.Key.set(KEY)

BASE_URL = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0/'
CF.BaseUrl.set(BASE_URL)

personGroupId = "users"
print "users"
newUser = CF.person.create(personGroupId, name=firstName+" "+lastName, user_data=json.dumps(
	{"First Name":firstName,
	 "Last Name":lastName,
	 "Role":jobRole,
	 "Company":company,
	 "Skills":skills,
	 "Wants":wants}
))
print "next"
imagelocation = "./img/"+lastName+firstName+".jpg"
print "imgloc"
CF.person.add_face(imagelocation, personGroupId, newUser['personId'])
print "scream"
CF.person_group.train(personGroupId)

print("""<div class="logo", style="padding-top: 75px">
		<img src="logo.png">
		</div>
	""")
print("</html>")