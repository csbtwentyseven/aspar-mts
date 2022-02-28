import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import pyrebase

class FirebaseKurulum():

  firebaseConfig = {

    "apiKey": "AIzaSyCJRh_1Y6dWs8vBg8Bx68DUroiDbTTEpO4",
    "authDomain": "aspar-mts.firebaseapp.com",
    "projectId": "aspar-mts",
    "storageBucket": "aspar-mts.appspot.com",
    "messagingSenderId": "1081592971525",
    "appId": "1:1081592971525:web:8cdb7ac5dc40c0d5a6b76c",
    "measurementId": "G-CFY6P2W34Y",
    "databaseURL":"", #REALTIME DATABASE ILE CALISIRKEN BURAYI DOLDURMAN GEREKIR
  }

  firebase = pyrebase.initialize_app(firebaseConfig)
  auth = firebase.auth() #auth erisim key


  def firestore_erisim(self):
    cred = credentials.Certificate("serviceaccountKey.json")
    firebase_admin.initialize_app(cred)

    db = firestore.client()
    return db