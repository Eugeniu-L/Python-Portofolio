from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
from flask_bootstrap import Bootstrap
from sqlalchemy import desc

app = Flask(__name__)
app.app_context().push()

# app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///task.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)

temporary_task = []


# Define the DB Table for Task
class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key="True")
    task = db.Column(db.String(1000), nullable=False)
    handle = db.Column(db.String(30), nullable=False)
    date = db.Column(db.String(10))


@app.route("/", methods=["GET", "POST"])
def main():
    global temporary_task
    if request.method == "POST":
        temporary_task.append(request.form["task"])
        length = int(len(temporary_task))
        mode = 1
        return render_template("index.html", task=temporary_task, mode=mode, len=length)
    else:
        temporary_task = []

    mode = 0
    return render_template("index.html", mode=mode)


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

    
if __name__ == '__main__':
    app.run(debug=True)
