from flask import Flask, render_template, request, url_for, redirect

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






#Run the code and flask
if __name__ == '__main__':
    app.debug = True
    app.run()





