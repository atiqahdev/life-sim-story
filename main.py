from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Life Sim Story</h1>
    <p>You wake up late for the day.</p>
    <a href='/rush'>Rush out immediately</a><br><br>
    <a href='/rest'>Stay in bed a little longer</a>
    """

@app.route("/rush")
def rush():
    return """
    <p>You rush out. You're tired but on time.</p>
    <p>Energy: 40</p>
    <p>Mood: stressed</p>
    <a href='/'>Start over</a>
    """

@app.route("/rest")
def rest():
    return """
    <p>You rest a bit more. You feel calmer, but you're late.</p>
    <p>Energy: 55</p>
    <p>Mood: calm</p>
    <a href='/'>Start over</a>
    """

if __name__ == "__main__":
    app.run(debug=True)

