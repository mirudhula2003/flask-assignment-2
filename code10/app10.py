from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def convert_temperature():
    fahrenheit = None
    if request.method == 'POST':
        celsius = request.form.get("celsius")
        if celsius:
            celsius = float(celsius)
            fahrenheit = (celsius * 9/5) + 32  # Celsius to Fahrenheit conversion

    return render_template("temp.html", fahrenheit=fahrenheit)

if __name__ == "__main__":
    app.run(debug=True)
