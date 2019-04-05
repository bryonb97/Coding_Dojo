from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def play():
    return render_template('index.html', times=0)

@app.route('/play/<x>')
def play_x(x):
    return render_template('index.html', times=int(x))

@app.route('/play/<x>/<color>')
def play_x_color(x, color):
    return render_template('index_colors.html', times=int(x), color=color)

if __name__ == "__main__":
    app.run(debug = True)