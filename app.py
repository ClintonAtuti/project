from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///root.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(255), nullable=False)
    lastName = db.Column(db.String(255), nullable=False)
    email= db.Column(db.String(255),unique=True, nullable=False)
    message= db.Column(db.Text(278), nullable=False)

    def __tsl__(self, firstName, lastName, email, message):
        self.firstName=firstName
        self.lastName=lastName
        self.email=email
        self.message=message


@app.route('/contact', methods = ['POST', 'GET'])
def contact ():
    if request.method == 'POST':
        firstName=request.form['firstName']
        lastName=request.form['lastName']
        email=request.form['email']
        message=request.form['message']
        
        insert = Task(firstName,lastName,email,message)
        db.session.add(insert)
        db.session.commit()

        flash("Message sent")

        return render_template("contact.html")


@app.route("/")
def home():
   return render_template("index.html")

@app.route("/index.html")
def homepage():
   return render_template("index.html")


@app.route("/contact.html")
def contact():
   return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=  True)