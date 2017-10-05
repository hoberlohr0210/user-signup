from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/username", methods=['POST'])
def userName():
    username = request.form['username']
    password = request.form['password']
    confirmpass = request.form['verify']
    email_address = request.form['email']

    u_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if len(username) < 3 or len(username) > 20 or " " in username:
        u_error = "Not a valid username."

    if len(password) < 3 or len(password) > 20 or " " in password:
        password_error = "Not a valid password."
        password = ''

    if confirmpass == "":
        verify_error = "Not a valid password."

    elif password != confirmpass:
        verify_error = 'Passwords do not match.'
        verify = ''

    if email_address != "" and len(email_address) < 3 or len(email_address) > 20:
        email_error = 'Not a valid email.'
    elif email_address != "" and ("." not in email_address or "@" not in email_address):
        email_error = 'Not a valid email.'

    if not u_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username)
    else:
        return render_template('signup.html', username_error=u_error, password_error=password_error, 
        verify_error=verify_error, email_error=email_error )


@app.route("/")
def index():
    return render_template('signup.html')

app.run()



