from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import model_user

@app.route('/')
def index():
    users = model_user.User.get_all()
    print(users)
    return render_template("read_all.html", all_users = users)

@app.route('/read_one/<int:id>')
def read_one(id):
    user = model_user.User.get_one(id = id)
    return render_template("read_one.html", user = user)

@app.route('/user/<int:id>/edit')
def show_update_form(id):
    user = model_user.User.get_one(id = id)
    return render_template('update.html', user = user)

@app.route('/user/new')
def new_user():
    return render_template('create.html')

@app.route('/add_user', methods=["POST"])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    model_user.User.create(data)
    return redirect('/')

@app.route('/user/<int:id>/update', methods=["POST"])
def update_user(id):
    data_updates = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "id": id
    }
    model_user.User.update_one(data_updates)
    return redirect(f'/read_one/{id}')

@app.route('/user/<int:id>/delete')
def delete_user(id):
    model_user.User.delete_one(id = id)
    return redirect('/')

