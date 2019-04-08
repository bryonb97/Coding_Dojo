from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods = ['POST'])
def submit():
    return render_template('results.html', name = request.form["name"], location = request.form["select_location"],
                            fav_language = request.form["select_language"], comment = request.form["comment"],
                            check1 = request.form["check1"], rbYes = request.form["rbYes"],
                            rbNo = request.form["rbNo"])

if __name__ == "__main__":
    app.run(debug = True)