from flask_app import app
from flask import render_template, redirect, session ,request
from flask_app.models.ninja_model import ninja_model
from flask_app.models.dojo_model import dojo_model

@app.route("/")
def index_dojo():
    dojos_list = dojo_model.get_all()
    return render_template("index.html", data = dojos_list)

@app.route("/add_ninja")
def add_new_ninja():
    dojos_list = dojo_model.get_all()
    return render_template("create_ninja.html", data = dojos_list)

@app.route("/create_ninja", methods = ["post"])
def create_ninja():
    if not ninja_model.validate_data(request.form):
        return redirect("/")
    
    results = ninja_model.create_ninja(request.form)
    print(request.form)
    return redirect("/")

@app.route("/show_user_info/<int:id>")
def show_ninja(id):
    data = {"id":id}
    one_user = ninja_model.one_ninja_function(data)
    return render_template("one_user_page.html", data=one_user)

@app.route("/transit_edit_user_info/<int:id>")
def transit_edit_user(id):
    data = {"id":id}
    one_user = ninja_model.one_ninja_function(data)
    print(id)
    return render_template("edit_user.html", data=one_user)

@app.route("/edit_user_info", methods = ["post"])
def edit_user():
    edit_one_user = ninja_model.edit_user_info(request.form)
    print(request.form)
    return redirect("/")

@app.route("/delete_user/<int:id>")
def delete_user(id):
    data = {"id":id}
    delete_one_user = ninja_model.delete_user_info(data)
    return redirect("/")
    