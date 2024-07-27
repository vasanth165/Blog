from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

response = requests.get(os.environ.get("URL"))
data = response.json()
blogs = data["record"]

@app.route('/')
def home():
    return render_template("index.html", data=blogs)

@app.route("/post/<id>")
def post(id):
    data = blogs[int(id )- 1]
    return render_template("post.html",data=data)


if __name__ == "__main__":
    app.run(debug=True)
