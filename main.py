from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/rush")
def rush():
    return render_template("rush.html")

@app.route("/rest")
def rest():
    return render_template("rest.html")

if __name__ == "__main__":
    app.run()
