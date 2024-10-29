from flask import Flask,render_template,request
app=Flask(__name__)

credentials = {
    "user1": "password123",
    "user2": "mypassword",
    "admin": "adminpass",
    "testuser": "test1234"
}


@app.route('/')
def home():
    return render_template("creds.html")

@app.route('/creds',methods=['POST'])
def cred_check():
    user=request.form.get("username")
    passs=request.form.get("password")

    if credentials.get(user)==passs:
        res="SUCCESSFULL  LOGIN!!!"
    else:
        res="INCORRECT USERNAME-PASSWORD"

    return render_template("creds.html",res=res)
if __name__=='__main__':
    app.run(debug=True)