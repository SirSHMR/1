from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# صفحة التسجيل
@app.route('/')
def login_page():
    return render_template('login.html')

# معالجة POST لتسجيل الدخول
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # تحقق من اسم المستخدم وكلمة المرور
    if username == "admin" and password == "password":
        return "Welcome, admin!"
    else:
        return "Invalid username or password!"

if __name__ == '__main__':
    app.run(debug=True)
