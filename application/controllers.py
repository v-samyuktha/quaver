from flask import Flask, request, redirect, session
from flask import render_template
from flask import current_app as app
from application.models import User
from main import db
import requests

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
                    session["uname"] = username
                    return redirect("/dashboard")
            else:
                return render_template("welcome.html", message="Invalid username or password, please check")
        
        elif "signup" in request.form.keys():
            #return render_template("signup.html")
            return redirect("/new")
        else:
            print("ERROR: Neither login nor sign-up") 
    else:
        print("ERROR: Neither GET nor POST")

@app.route("/dashboard", methods = ["GET", "POST"])
def dashboard():

    if request.method == "GET":
        url = f'http://127.0.0.1:8080/api/songs'
        response = requests.get(url)
        song_list = response.json()
        print(song_list)
        return render_template('home.html', song_list=song_list, uname = session["uname"])

    if request.method == "POST":
        return redirect(f'search_song?name={request.form["search_text"]}')

@app.route("/search_song", methods=["GET", "POST"])
def search_results():
    if request.method=="GET":
        text = request.args.get("name")
        url = f'http://127.0.0.1:8080/api/songs?name={text}'
        response = requests.get(url)

        if response.status_code==200:
            results = response.json()
            return render_template("search_results.html", results = results, name=text, uname=session["uname"])
    
    if request.method == "POST":
            return redirect(f'search_song?name={request.form["search_text"]}')

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

@app.route("/lyrics", methods = ["GET", "POST"])
def display_lyrics():
    if request.method == "GET":
        return render_template("lyrics.html", name = request.args.get("name"), uname=session["uname"])
    if request.method == "POST":
        return redirect(f'search_song?name={request.form["search_text"]}')
    
@app.route("/profile", methods = ["GET", "POST"])
def display_profile():
    if request.method=="GET":
        return render_template("profile.html", name=request.args.get("name"), uname=session["uname"])
    if request.method == "POST":
        return redirect(f'search_song?name={request.form["search_text"]}')   