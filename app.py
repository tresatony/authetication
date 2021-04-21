from flask import Flask, render_template, redirect, url_for, request

# Create the application.
app = Flask(__name__)
# Route for handling the login page logic
@app.route('/')
def index():
    return render_template('login.html')

# @app.route('/', methods=['GET'])
# def index():
#     # Main page
#     return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Login failed due to incorrect username and password.Please try again.'
        else:
            return render_template('index.html')
#return redirect(url_for('home'))

    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.debug=True
    app.run()
