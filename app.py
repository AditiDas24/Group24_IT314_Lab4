import pyrebase
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for

app = Flask(__name__)       #Initialze flask constructor

#Add your own details
config = {
  "apiKey": "AIzaSyDBYVCt74OEEt5nS_Tcf_2iHzm4gXaMRKs",
  "authDomain": "fakenews-6c069.firebaseapp.com",
  "databaseURL": "https://fakenews-6c069-default-rtdb.firebaseio.com",
  "projectId": "fakenews-6c069",
  "storageBucket": "fakenews-6c069.appspot.com",
  "messagingSenderId": "285735704642",
  "appId": "1:285735704642:web:948dac0293ee50e12935db",
  "measurementId": "G-JREKP78MM9",
   "databaseURL" : ""
}

#initialize firebase
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

#Initialze person as dictionary
person = {"is_logged_in": False, "name": "", "email": "", "uid": ""}

#Home
@app.route("/")
def home():
    return render_template("home_page.html")

@app.route("/home")
def home_():
    return render_template("home_page.html")

#Login
@app.route("/login")
def login():
    return render_template("login.html")

#Sign up/ Register
@app.route("/signup")
def signup():
    return render_template("signup.html")


if __name__ == "__main__":
    app.run(port=3000)
