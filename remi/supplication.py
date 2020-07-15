# from flask import Flask, render_template, request, session
# from flask_session import Session

# sup = Flask(__name__)
# sup.config.from_pyfile('supconfig.py')

# sup.config["SESSION_PERMANENT"] = False
# sup.config["SESSION_TYPE"] = "filesystem"
# Session(sup)

# @sup.route('/', methods=["GET", "POST"])
# def more():
#     if session.get("notes") is None:
#         session["notes"] = []
#     if request.method == "POST":
#         note = request.form.get("note")
#         session["notes"].append(note)
#     return render_template("more.html", note = session["notes"])
