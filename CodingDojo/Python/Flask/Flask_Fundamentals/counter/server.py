from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'X8zad82VwK782GPc'
app.count = 0

def set_session():
    session['count'] = 0

@app.route('/')
def index():
    session['count'] += 1
    return render_template('index.html', count = session['count'])

@app.route('/increment', methods=['POST'])
def increment_twice():
    session['count'] += 1
    #We only increment by 1 since reloading the page also increments
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    set_session()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)