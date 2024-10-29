from flask import Flask, render_template

app = Flask(__name__)

@app.route('/bio')
def bio():
    user_info = {
        'name': 'Mirudhula',
        'age': 21,
        'hobbies': ['Gardening', 'Baking Cakes', 'Coding']
    }
    return render_template('bio.html', user=user_info)

if __name__ == '__main__':
    app.run(debug=True)
