from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)
app.config.from_pyfile('config.py')

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/', methods=["GET", "POST"])
def lead():
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)
    return render_template("lead.html", notes = session["notes"])

@app.route('/more')
def more():
    foodlists = ['Efo riro', 'Fried rice', 'Goat stew']
    return render_template("more.html", foodlists = foodlists)
if __name__=='__main__':
    app.run()
