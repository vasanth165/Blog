from flask import Flask, render_template
import requests


app = Flask(__name__)


response = requests.get("https://api.jsonbin.io/v3/b/660d4bddacd3cb34a832bbb3")
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
