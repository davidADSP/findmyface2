import pyodbc
#SQL DB Access Info
server = 'findmyface.database.windows.net'
database = 'FaceDB'
username = 'findmyface'
password = "Theyfinallyfedus!"
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)

#Order to be entered in DB
#    PhotoID
#    First Name
#    Last Name
#    Job/Role
#    Company
#    Skills
#    Wants

def registerNewUser():
    fn = input("First Name: ")
    ln = input("Last Name: ")
    role = input("Role: ")
    comp = input("Company: ")
    skills = input("Skills: ")
    #wants = input("Wants: ")
    print("Now we'll need a picture. Press any button when you're in front of the camera")
    keyPressed = input()
    photoid = '111111111111111'
    if (keyPressed):
        #photoid = getNewPhotoID()
        keyPressed = 0
    #Now we enter this info into the SQL database.

    cursor = cnxn.cursor()
    insertvalues = "INSERT INTO Users VALUES ('{0}','{1}','{2}','{3}','{4}','{5}');"
    insertvalues = insertvalues.format(photoid,fn,ln,role,comp,skills)
    print(insertvalues)
    cursor.execute(insertvalues)
    cnxn.commit()
                   
