from flask import Flask, render_template, redirect, request, url_for
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection

app = Flask(__name__)

# @app.route('/')
# def home():
#     return redirect("/users")

@app.route("/users")
def index():
    mysql = connectToMySQL('Users')	        # call the function, passing in the name of our db
    users = mysql.query_db('SELECT * FROM users;')  # call the query_db function, pass in the query as a string
    if(len(users) == 0):
        return render_template("register.html")
    print('=================================================')
    print(users[0]['first_name'])
    return render_template("index.html", all_users = users)

@app.route("/users/new", methods=["GET"])
def register():
    return render_template("register.html")

@app.route("/users/create", methods=["POST"])
def create_user():
    mysql = connectToMySQL('Users')

    query = 'INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());'

    data = {
        "first_name": request.form["firstNameBox"],
        "last_name": request.form["lastNameBox"],
        "email": request.form["emailBox"]
    }
    id = mysql.query_db(query, data)
    print(id)
    print("=================================================")
    print(f"User created{data}")
    return redirect("/users")

@app.route("/users/<id>", methods=["GET", "POST"])
def get_info(id):
    mysql = connectToMySQL('Users')
    print("Inside Users<id>")
    query = f"SELECT * FROM users WHERE id = {id} LIMIT 1;"
    users = mysql.query_db(query)
    print("=================================")
    print(users)
    print("=================================")

    return render_template("user_info.html", all_users = users)

@app.route("/users/<id>/edit", methods=["GET"])
def edit_user(id):
    mysql = connectToMySQL('Users')
    print("-------Connected to DB in edit Route--------")
    query = f"SELECT * FROM users WHERE id = {id} LIMIT 1;"
    users = mysql.query_db(query)

    return render_template("edit_user.html", all_users = users)

@app.route("/users/<id>/update", methods=["POST"])
def update_user(id):  
    mysql = connectToMySQL('Users')   
    print("-------Connected to DB in Updated Route--------")
    data = {
        "first_name": request.form["firstNameBox"],
        "last_name": request.form["lastNameBox"],
        "email": request.form["emailBox"]
    }

    query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = (" + id + ");"
    
    

    users = mysql.query_db(query, data)

    print(f"Updated User------------------------------------{users}")

    return redirect(f"/users/{id}")
    
@app.route("/users/<id>/delete", methods=["GET"])
def delete_user(id):
    mysql = connectToMySQL('Users')

    query = f"DELETE FROM users WHERE id = {id} LIMIT 1"
    mysql.query_db(query)

    print(query)
    return redirect("/users")

if __name__ == "__main__":
    app.run(debug=True) 