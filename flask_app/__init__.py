from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)
DATABASE = "dojo_and_ninjas_scheme"
app.secret_key= "sdlkgj"