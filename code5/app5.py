from flask import Flask,render_template
import random
app=Flask(__name__)
quoteslist = [
    "Out of suffering have emerged the strongest souls.",
    "Beauty is not in the face; beauty is a light in the heart.",
    "Your pain is the breaking of the shell that encloses your understanding.",
    "In the sweetness of friendship let there be laughter.",
    "Let there be spaces in your togetherness.",
    "Trust in dreams, for in them is hidden the gate to eternity.",
    "Love knows not its own depth until the hour of separation.",
    "A friend who is far away is sometimes much nearer than one who is at hand.",
    "Work is love made visible.",
    "Progress lies not in enhancing what is, but in advancing toward what will be."
]
@app.route('/')
def home():
    welcome_message = "Welcome to the Motivational Quote Generator!"
    return render_template("quotes.html", message=welcome_message)

@app.route('/quotes')
def quotes():
    quo=random.choice(quoteslist)
    return render_template("quotes.html",quote=quo)

if __name__=='__main__':
    app.run(debug=True)