from datetime import datetime
from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection

app = Flask(__name__)

@app.route("/")
def index():
    mysql = connectToMySQL('Pets')	        # call the function, passing in the name of our db
    pets = mysql.query_db('SELECT * FROM pets;')  # call the query_db function, pass in the query as a string
    print('=================================================')
    print(pets[0]['name'])
    return render_template("index.html", all_pets = pets)

@app.route("/create_pet", methods=["POST"])
def create_pet():
    mysql = connectToMySQL('Pets')

    query = 'INSERT INTO pets (name, type, created_at, updated_at) VALUES (%(name)s, %(type)s, NOW(), NOW());'

    data = {
        "name": request.form["nameBox"],
        "type": request.form["typeBox"]
    }
    new_pet_id = mysql.query_db(query, data)
    # print(new_pet_id)
    # print("=================================================")
    # print(f"Pet created{data}")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
