__version__="0.1.0"

import sys
import os

# class awesome_module():

def awesome_module():
    print("Executing pip_module version %s." % __version__)
    print("List of argument strings: %s" % sys.argv[1:])
    print "this is new as well"


    project_name = raw_input('What is your project going to be called? ')
    print project_name + ", it's gonna be awesome!"
    folder_location_decision = raw_input('So where\'s it going? Press 1 for current folder or hit enter to specify: ')

    if folder_location_decision == "1":
        os.system('mkdir ' + project_name )
    else:
        folder_location = raw_input('Ok, where do you want to put the new project? ')
        os.system('mkdir ' + folder_location + "/" + project_name)

    project_contents = raw_input('Would you like me to create static and template folders? Type 1 for yes and just hit enter for no: ')
    if project_contents == "1" and folder_location_decision != "1":
        os.system('mkdir '+ folder_location +"/"+ project_name +"/static && mkdir "+ folder_location +"/"+ project_name +"/templates")

    elif project_contents == "1":
        os.system('mkdir '+ project_name +"/static && mkdir "+ project_name +"/templates")

    project_template = raw_input('How about a server.py file with standard libraries? Type 1 for yes and hit enter for no: ')
    if project_template == "1" and folder_location_decision != "1":
        server_file = "server.py"
        # os.system('touch '+ folder_location + "/" + project_name + "/" + server_file )
        new_file = open(folder_location + "/" + project_name + "/" + server_file, 'w')
        new_file.write('from flask import Flask, render_template, request, redirect, session')

    elif project_template == "1" and folder_location_decision == "1":
        server_file = "server.py"
        new_file = open(project_name + "/" + server_file, 'w')
        new_file.write('from flask import Flask, render_template, request, redirect, session\napp = Flask(__name__)\napp.secret.key =\n@app.route("/")\ndef index():')

    index_file = raw_input("would you like an index.html file in your templates folder? Type 1 for yes and hit enter for no: ")
    if index_file == "1" and folder_location_decision == "1":
        index = "index.html"
        new_index = open(project_name + "/" + "templates" + "/" + index, 'w')
        new_index.write("<!DOCTYPE HTML>\n<html>\n<meta>\n<body>\n</body>\n</html>")

    elif index_file == "1" and folder_location_decision != "1":
        index = "index.html"
        new_index = open(folder_location + "/" + project_name + "/" + "templates" + "/" + index, 'w')
        new_index.write("<!DOCTYPE HTML>\n<html>\n<meta>\n<body>\n</body>\n</html>")


    # if project_template == "1" and folder_location_decision == "1"

    # else:
    #     os.system
