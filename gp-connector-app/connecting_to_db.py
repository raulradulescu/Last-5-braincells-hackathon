# import required modules
import firebase_admin
from firebase_admin import db, credentials
cred = credentials.Certificate("hackathon-itfest-firebase-adminsdk-r5qx1-066b0ed658.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://hackathon-itfest-default-rtdb.europe-west1.firebasedatabase.app/"})
ref = db.reference("/")
# retrieving data from root node
ref.get()