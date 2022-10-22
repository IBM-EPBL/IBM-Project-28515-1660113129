from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Homepage.html')

@app.route("/About")
def about():
    return render_template('About.html')

@app.route("/sign-in")
def signIn():
    return render_template('Sign-in.html')

@app.route("/sign-up")
def signUp():
    return render_template('Sign-up.html')

if __name__ == "__main__":
    app.run(debug=True)