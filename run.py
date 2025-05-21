from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", title="with title")

@app.route("/css")
def css():
    return render_template("css.html", title="with title")

@app.route("/django")
def django():
    return render_template("django.html", title="with title")

@app.route("/flask")
def flask():
    return render_template("flask.html", title="with title")

@app.route("/html")
def html():
    return render_template("html.html", title="with title")

@app.route("/java_script")
def java_script():
    return render_template("java_script.html", title="with title")

@app.route("/python")
def python():
    return render_template("python.html", title="with title")

if __name__ == "__main__":
    app.run(debug=True)