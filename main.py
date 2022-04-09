from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "hellow this is ghurrahu singh <h1>Ghurrahu Singh<h1>"

@app.route("/contact")
def contact():
    return "<h2>This is the contact section<h2>";

if __name__ == "__main__":
    app.run()