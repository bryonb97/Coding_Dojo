from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<word>')
def say(word):
    return f"Hi {str(word)}!"

@app.route('/repeat/<word>/<amount>')
def repeat(word, amount):
    return f' {str(word)}' * int(amount)

if(__name__ == "__main__"):  # Ensure this file is being run directly and not from a different module
    app.run(debug = True)   # Run the app in debug mode.