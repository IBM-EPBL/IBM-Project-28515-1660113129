from flask import Flask, render_template;

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Homepage.html')

#Render Signup Page
@app.route('/sign-in')
def SignIn():
    return render_template('Signin.html')

@app.route('/sign-up')
def SignUp():
    return render_template('Signup.html')

@app.route('/about')
def About():
    return render_template('About.html')

if __name__ == "__main__":
    app.run(debug=True)