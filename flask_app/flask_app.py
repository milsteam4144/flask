from flask import Flask, render_template

#This creates a new Flask object (application) named app
app = Flask(__name__)

#Routes(aka views) go here

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", name = "CSC 221 Students", title = "My Fluffy Ragdolls")



#Run the code and flask
if __name__ == '__main__':
    app.debug = True
    app.run()





