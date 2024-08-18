from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/submit', methods=['POST'])
def submit():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    email = request.form['email']
    password = request.form['password']
    print(f"firstname: {firstname}, lastname: {lastname}, with email: {email}, password: {password}")
    return f"Registration successful for {firstname} {lastname} with email {email} password {password}."

if __name__ == '__main__':
    app.run(debug=True)
