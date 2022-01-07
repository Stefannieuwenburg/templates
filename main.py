from flask import Flask, render_template, redirect, url_for

__winc_id__ = "9263bbfddbeb4a0397de231a1e33240a"
__human_name__ = "templates"

app = Flask(__name__)


@app.route('/',methods=['GET'])
def index(title = "index"):
    return render_template("index.html", title=title)

@app.route("/home",methods=['GET'])
def home():
    return redirect(url_for("index"))

@app.route("/about",methods=['GET'])
def about(title = "About"):
    return render_template("about.html", title=title)

@app.route("/info",methods=['GET'])
def info(title = "Info"):
    return render_template("info.html", title=title)

if __name__ == "__main__":
    app.run(debug=True)