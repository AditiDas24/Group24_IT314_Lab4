from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
import pyrebase
from Scraper.Scraper import *


tfvect = TfidfVectorizer(stop_words='english', max_df=0.7)
loaded_model = pickle.load(open('model.pkl', 'rb'))
dataframe = pd.read_csv('news.csv')
x = dataframe['text']
y = dataframe['label']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

def fake_news_det(news):
    tfid_x_train = tfvect.fit_transform(x_train)
    tfid_x_test = tfvect.transform(x_test)
    input_data = [news]
    vectorized_input_data = tfvect.transform(input_data)
    prediction = loaded_model.predict(vectorized_input_data)
    return prediction



app = Flask(__name__)       #Initialze flask constructor

#Add your own details
config = {
  "apiKey" : "AIzaSyDwU9M-A9KrdDNIbo6D_qi8wQdKE3RVTHg",
  "authDomain": "mypro-ce6df.firebaseapp.com",
  "projectId": "mypro-ce6df",
  "storageBucket": "mypro-ce6df.appspot.com",
  "messagingSenderId": "604651206875",
  "appId": "1:604651206875:web:eee1c4de5b8b4367fb34fe",
  "measurementId": "G-N5HDZTBFPH",
   "databaseURL" : ""
}



#initialize firebase
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

#Initialze person as dictionary
person = {"is_logged_in": False, "name": "", "email": "", "uid": ""}


#Login
@app.route("/")
def login():
    return render_template("news_detection.html")

@app.route("/result",methods = ["POST"])
def result():
    inputm = request.form['input-method']
    inputd = request.form['input-data']
    try:
        newsl = request.form['select-newsletter']
        if newsl == 'TimesofIndia':
            data = timesOfIndiaScraper(inputd)
        elif newsl == 'TheHindu':
            data = theHinduscraper(inputd)
        elif newsl == 'TheGuardian':
            data = theguardianscraper(inputd)
        else:
            return render_template("result.html", result = "Error")
        return render_template("result.html", result = fake_news_det(data))    
    except:
        newsl = 0
        return render_template("result.html", result = fake_news_det(inputd))


# #Sign up/ Register
# @app.route("/signup")
# def signup():
#     return render_template("signup.html")

# #Welcome page
# @app.route("/welcome")
# def welcome():
#     if person["is_logged_in"] == True:
#         return render_template("welcome.html", email = person["email"], name = person["name"])
#     else:
#         return redirect(url_for('login'))

# #If someone clicks on login, they are redirected to /result
# @app.route("/result", methods = ["POST", "GET"])
# def result():
#     unsuccessful = 'Please check your credentials'
#     successsful = 'Login successful'
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['pass']
#         try:
#             auth.sign_in_with_email_and_password(email, password)
#             return render_template('welcome.html', s=successsful)
#         except:
#             return render_template('register.html', us=unsuccessful)
#     return render_template('login.html') 

# #If someone clicks on register, they are redirected to /register
# @app.route("/register", methods = ["POST", "GET"])
# def register():
#     if request.method == "POST":        #Only listen to POST
#         result = request.form           #Get the data submitted
#         email = result["email"]
#         password = result["pass"]
#         name = result["name"]
#         try:
#             #Try creating the user account using the provided data
#             auth.create_user_with_email_and_password(email, password)
#             #Login the user
#             user = auth.sign_in_with_email_and_password(email, password)
#             #Add data to global person
#             global person
#             person["is_logged_in"] = True
#             person["email"] = user["email"]
#             person["uid"] = user["localId"]
#             person["name"] = name
#             #Append data to the firebase realtime database
#             data = {"name": name, "email": email}
#             db.child("users").child(person["uid"]).set(data)
#             #Go to welcome page
#             return redirect(url_for('welcome'))
#         except:
#             #If there is any error, redirect to register
#             return redirect(url_for('register'))

#     else:
#         if person["is_logged_in"] == True:
#             return redirect(url_for('welcome'))
#         else:
#             return redirect(url_for('register'))

if __name__ == "__main__":
    app.run(debug = True)
