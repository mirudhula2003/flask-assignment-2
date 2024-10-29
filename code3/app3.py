from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def cal():
    return render_template("calc.html")

@app.route('/calculate',methods=['POST'])
def calc():
    num1=request.form.get("num1")
    num2=request.form.get("num2")
    result=int(num1)+int(num2)
    return render_template("calc.html",result=result)

if __name__=='__main__':
    app.run(debug=True)
