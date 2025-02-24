from flask import Flask, render_template, request, redirect, url_for
import os
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/issues')
def issues():
    return render_template("issues.html")


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/March2025')
def issue1():
    return render_template("issue1.html")
if __name__ == "__main__":
    app.run(debug=True)