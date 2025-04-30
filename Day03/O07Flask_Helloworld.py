
from flask import Flask, redirect, url_for

app = Flask(__name__)           # name of the current module __main__

@app.route("/")                 # home page
def home():
    return "<h1> Hello World </h1>"

@app.route("/<username>")
def user(username):
    return f"<h3> Greetings Mr.{username}, Welcome to the event."

@app.route("/admin")
def admin():
    return redirect(url_for("user", username="Richard"))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

