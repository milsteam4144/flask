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

#The results from the form's POST method are shown on this page
@app.route("/results", methods=["POST"])
def results():
    user_name = request.form['name']
    user_pets = request.form.get('textarea')
    pets_string = user_pets.split(" ")
    pet_types = ['dog', 'dogs', 'cat', 'cats', 'bird', 'fish', 'snake']
    for item in pet_types:
        if item in pets_string:
                return render_template('results.html', name = user_name, your_pets = f"You have a pet {item}")
    return render_template('results.html', name = user_name, your_pets = "It doesn't look like you have any pets")


#The survey page that contains a form
#You need the GET and POST methods to submit the info the user gives in the form
@app.route('/survey', methods=('GET', 'POST'))
def survey():
    return render_template("survey.html")
            

#Run the code and flask with debugging on
if __name__ == '__main__':
    app.debug = True
    app.run()





