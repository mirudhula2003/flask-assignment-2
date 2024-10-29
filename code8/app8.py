from flask import Flask, render_template, request

app = Flask(__name__)

feeddict = {}

@app.route('/')
def home():
    return render_template("feedback.html", feedbacks=feeddict)

@app.route('/feedbacks', methods=['POST'])
def feeds():
    name = request.form.get("name")
    feedback = request.form.get("feedback")
    feeddict.setdefault(name, []).append(feedback)
    return render_template("feedback.html", feedbacks=feeddict)

if __name__ == "__main__":
    app.run(debug=True)
