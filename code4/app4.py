from flask import Flask,render_template,request

app=Flask(__name__)
tasks=[]
@app.route('/')
def home():
    return render_template("tasks.html")
@app.route('/tasks',methods=['POST'])
def taskadd(methods=['POST']):
    t=request.form.get("task")
    tasks.append(t)
    return render_template("tasks.html",tasks=tasks)

if __name__=='__main__':
    app.run(debug=True)



