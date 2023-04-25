

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

#Welcome page
@app.route("/welcome")
def welcome():
    if person["is_logged_in"] == True:
        return render_template("welcome.html", email = person["email"], name = person["name"])
    else:
        return redirect(url_for('login'))
    
#News detection page
@app.route("/news_detection")
def news_detection():
    if person["is_logged_in"] == True:
        return render_template("news_detection.html")
    else:
        return redirect(url_for('login'))

#If someone clicks on login, they are redirected to /result
@app.route("/result", methods = ["POST", "GET"])
def result():
    unsuccessful = 'Please check your credentials'
    successsful = 'Login successful'
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pass']
        try:
            auth.sign_in_with_email_and_password(email, password)
            return render_template('news_detection.html', s=successsful)
        except:
            return render_template('login.html', us=unsuccessful)
    return render_template('login.html') 

#If someone clicks on register, they are redirected to /register
@app.route("/register", methods = ["POST", "GET"])
def register():
    if request.method == "POST":        #Only listen to POST
        result = request.form           #Get the data submitted
        email = result["email"]
        password = result["pass"]
        name = result["name"]
        try:
            #Try creating the user account using the provided data
            auth.create_user_with_email_and_password(email, password)
            #Login the user
            user = auth.sign_in_with_email_and_password(email, password)
            #Add data to global person
            global person
            person["is_logged_in"] = True
            person["email"] = user["email"]
            person["uid"] = user["localId"]
            person["name"] = name
            #Append data to the firebase realtime database
            data = {"name": name, "email": email}
            db.child("users").child(person["uid"]).set(data)
            #Go to welcome page
            return redirect(url_for('welcome'))
        except:
            #If there is any error, redirect to register
            return redirect(url_for('register'))

    else:
        if person["is_logged_in"] == True:
            return redirect(url_for('news_detection'))
        else:
            return redirect(url_for('register'))

if __name__ == "__main__":
    app.run(port=3000)
