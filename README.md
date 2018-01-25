# findmyface
A web app to find faces in a video stream and label the faces with the attributes of each person

# How to run the video app

1. Download enough libraries until you don't get an error with step 2
2. run 'python main.py' from within the video_app folder
3. create_pg.py creates a new person group
4. get_users.py get the users from a person group
5. add_to_pg.py add a person and face to a person group

# How to run the registration app

1. Start an Apache local server, or equivalent (sudo apachectl start on Mac)
2. Go to /Library/Webserver/Documents and put the contents of the registration app folder in there
3. Edit the https.conf file in three ways (sudo vi /etc/apache2/httpd.conf)
    a. Uncomment LoadModule cgi_module libexec/apache2/mod_cgi.so
    b. Uncomment AddHandler cgi-script .cgi
    c. Ensure the Options line reads 'Options Indexes FollowSymLinks Multiviews ExecCGI'
4. Go to http://localhost/NewUserForm.html to see the app
5. Ensure there is a photo in the img subfolder called <Lastname><FirstName>.jpg
6. Fill out the details in the form and click submit
7. This should hopefully create a new person in the personGroup 'users'
