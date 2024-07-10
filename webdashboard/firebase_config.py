import pyrebase
import io

firebase_config = {
  'apiKey': "AIzaSyCgoz33SSJnA1Qu2Ah3FOYJbe6-48wkwzo",
    'authDomain': "andavarcon.firebaseapp.com",
    'databaseURL': "https://andavarcon-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "andavarcon",
    'storageBucket': "andavarcon.appspot.com",
    'messagingSenderId': "345505940170",
    'appId': "1:345505940170:web:5f4d99483f4b0ff9ca2a33",
    'measurementId': "G-S11Y6KNMT4"
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()
