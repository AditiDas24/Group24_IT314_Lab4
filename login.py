import pyrebase
config = {
  "apiKey": "AIzaSyDwU9M-A9KrdDNIbo6D_qi8wQdKE3RVTHg",
  "authDomain": "mypro-ce6df.firebaseapp.com",
  "projectId": "mypro-ce6df",
  "storageBucket": "mypro-ce6df.appspot.com",
  "messagingSenderId": "604651206875",
  "appId": "1:604651206875:web:eee1c4de5b8b4367fb34fe",
  "measurementId": "G-N5HDZTBFPH",
  "databaseURL" : ""
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

email = input('Please enter your email\n')
password = input('Please enter your password\n')

user = auth.sign_in_with_email_and_password(email , password)
auth.send_email_verification(user['idToken'])