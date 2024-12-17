from flask import Flask
import json

app = Flask(__name__)

@app.get("/")
def home():
    return "hello from flask"

@app.get("/test")
def test():
    return "hello fromm the test page"

@app.get("/about")
def about():
    return "adrian Aguinaga"

@app.get("/hello")
def hello():
    message = {"message":"hello there!"}
    return json.dumps(message)



app.run(debug=True) #that when i save the code the changes are applied i n to the server.