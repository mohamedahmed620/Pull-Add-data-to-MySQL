from flask_app import app
from flask import render_template, redirect, session ,request,flash
from flask_app.models.dojo_model import dojo_model

@app.route("/")
def index():
    dojos_list = dojo_model.get_all()
    return render_template("index.html", data = dojos_list)

@app.route("/add_dojo")
def add_user():
    return render_template("create_dojo.html")

@app.route("/create_dojo", methods = ["post"])

def create_dojo():

    if not dojo_model.validate_data(request.form):
        return redirect("/")
    
    results = dojo_model.create_dojo(request.form)
    print(request.form)
    return redirect("/add_ninja")

@app.route("/show_dojo_info/<int:id>")
def show_dojo(id):
    # data = {"id":id}
    
    one_user = dojo_model.one_dojo_function(id)
    print(one_user)
    # if len(one_user) == 0:
    #     print(len(one_user))
    #     flash("this dojo has no ninjas")
    #     return redirect("/")

    return render_template("one_dojo_page.html", data = one_user)



