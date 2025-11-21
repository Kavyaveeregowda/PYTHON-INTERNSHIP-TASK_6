from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        return render_template("thankyou.html", name=name)

    portfolio = {
        "name": "Kavya V",
        "role": "CSE Student | Python Developer",
        "about": "I am passionate about Python, Flask and building projects.",
        "skills": ["Python", "Flask", "HTML", "CSS", "SQL"],
        "projects": [
            {"title": "Student Management System", "desc": "A CRUD app using Python and SQL."},
            {"title": "Weather App", "desc": "Shows real-time weather using API."}
        ]
    }

    return render_template("index.html", portfolio=portfolio)

if __name__ == "__main__":
    app.run(debug=True)
