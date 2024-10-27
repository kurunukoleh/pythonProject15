from flask import Flask , render_template

app = Flask("my firs program")

@app.route("/pg")
def page():
    return "nigga"

@app.route("/")
def index():
    return render_template("index.html")

app.run()