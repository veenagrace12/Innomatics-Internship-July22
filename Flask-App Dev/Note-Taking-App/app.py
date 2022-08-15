from flask import Flask, render_template, request,session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []
@app.route('/', methods=["GET","POST"])
def index():
    if request.method == 'POST':
        note = request.form["note"]
        notes.append(note)
        return render_template("home.html", notes=notes)
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)