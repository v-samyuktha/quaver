from flask import Flask, request, redirect
from flask import render_template
from flask import current_app as app
from application.models import User
from main import db


@app.route("/", methods = ["GET", "POST"])
def homepage():
    if request.method == "GET":
        return render_template("welcome.html")
    
    elif request.method == "POST":
        user_list = User.query.all()

        if "login" in request.form.keys():
            username = request.form["username"]
            password = request.form["password"]
            for user in user_list:
                print (user.username, user.password)
                if (username, password) == (user.username, user.password):
                    #return render_template("home.html", uname = username)
                    return redirect(username+"/dashboard")
            else:
                return render_template("welcome.html", message="Invalid username or password, please check")
        
        elif "signup" in request.form.keys():
            #return render_template("signup.html")
            return redirect("/new")
        else:
            print("ERROR: Neither login nor sign-up") 
    else:
        print("ERROR: Neither GET nor POST")

@app.route("/<username>/dashboard", methods = ["GET", "POST"])
def dashboard(username):

    if request.method == "GET":
        return render_template("home.html", uname=username)

@app.route("/new", methods = ["GET", "POST"])
def create_account():
    if request.method=="GET":
        return render_template("signup.html")

    elif request.method=="POST":
        user_list = User.query.all()

        if "create" in request.form.keys():
            username = request.form["username"]
            password = request.form["password"]
            password2 = request.form["password2"]
            print("input: ", username, password, password2)
            print("user list:")
            for user in user_list:
                print (user.username, user.password)
                if username == user.username:
                    #return render_template("home.html", uname = username)
                    return render_template("signup.html", message="Username already exists")
            if password != password2:
                    return render_template("signup.html", message="Password and Re-Typed passwords do not match")
            new_user = User(username=username, password=password)
            print("To create: ", new_user.username, new_user.password)
            db.session.add(new_user)
            db.session.commit()
            return render_template("new_user.html")
        else:
            return redirect("/")
    else:
        print("ERROR: Neither GET nor POST")