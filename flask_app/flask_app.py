from flask import Flask, render_template, request, url_for, redirect, flash

#This creates a new Flask object (application) named app
app = Flask(__name__)

#Routes(aka views) go here

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", name = "CSC 221 Students", title = "My Fluffy Ragdolls")

@app.route("/william")
def william():
    return render_template("william.html", name = "William", title = "My Fluffy Ragdolls")

@app.route("/betty")
def betty():
    return render_template("betty.html", name = "Betty Boo", title = "My Fluffy Ragdolls", adjective = "Sweet", \
                           gender = "Girl")


#The survey page that contains a form
#You need the GET and POST methods to submit the info the user gives in the form
#YouTube video explaining GET vs POST

@app.route('/survey', methods=('GET', 'POST'))
def survey():
    #If the user clicks Submit to send info to the server
    if request.method == 'POST':
        #Grab the data from the form and save in variables
        user_name = request.form['name']
        user_pets = request.form['my_pets']

        #Split the user's input into a list of words
        user_string = user_pets.split(" ")
        print(user_string)
        return redirect(url_for("results", display_info = user_name))
        
    else:
        return render_template("survey.html")
            
    





#Run the code and flask
if __name__ == '__main__':
    app.debug = True
    app.run()





