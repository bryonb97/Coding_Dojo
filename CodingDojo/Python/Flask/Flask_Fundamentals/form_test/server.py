from flask import Flask, render_template, request, redirect #added request
app = Flask(__name__)

# We will let the index page handle the form rendering
@app.route('/')
def index():
    return render_template('index.html')

# The users page handles sending the info entered in the form to the backend via a dictionary.
@app.route('/users', methods=['POST']) # GET is default
def create_user():
    print('Got Post Info')
    print(request.form)
    name_from_form = request.form['name']
    email_from_form = request.form['email']
    return render_template("show.html", name_on_template=name_from_form, email_on_template=email_from_form)

if __name__ == "__main__":
    app.run(debug = True)