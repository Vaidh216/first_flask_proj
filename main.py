from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "hellow this is ghurrahu singh <h1>Ghurrahu Singh<h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}"
 
@app.route("/contact")
def contact():
    return "<h2>This is the contact section<h2>";

@app.route("/admin")
def admin():
    return redirect(url_for("contact"))

if __name__ == "__main__":
    app.run()