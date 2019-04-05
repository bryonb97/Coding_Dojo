from flask import Flask, render_template # Import Flask to allow us to create our app and import render_template
app = Flask(__name__)   # Create a new instance of Flask class called "app"

@app.route('/')
def index():
    return render_template("index.html", phrase="hello", times=5)	# notice the 2 new named arguments!
if __name__=="__main__":
    app.run(debug=True)

@app.route('/')         # The "@" decorator associates this route with the function immediately following
def hello_world1():  
    return 'Hello World!'

@app.route('/')                           
def hello_world():
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('/templates/index.html')  

@app.route('/success')
def success():
    return "success"

@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

if __name__ == "__main__":  # Ensure this file is being run directly and not from a different module
    app.run(debug = True)   # Run the app in debug mode.