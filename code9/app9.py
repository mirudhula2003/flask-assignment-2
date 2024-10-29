from flask import Flask, render_template

app = Flask(__name__)

users = [
    {"name": "Aarav", "age": 30, "city": "Mumbai"},
    {"name": "Vihaan", "age": 25, "city": "Bengaluru"},
    {"name": "Saanvi", "age": 28, "city": "Delhi"},
    {"name": "Diya", "age": 22, "city": "Kolkata"},
]


@app.route('/')
def home():
    return render_template("users.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)
