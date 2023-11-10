#---------- NOT IN USE----------------
from flask_restful import Resource, fields, marshal_with, reqparse
from flask import render_template, redirect, request, make_response
from application.models import User

resource_fields ={
    'username': fields.String,
    'password': fields.String
}

login_form_parser = reqparse.RequestParser()
login_form_parser.add_argument('username')
login_form_parser.add_argument('password')

class HomeAPI(Resource):
    def get(self):
        print("GET in HomeAPI")
        return make_response(render_template("welcome.html"))

    def put(self, username):
        pass

    def delete(self, username):
        pass

    @marshal_with(resource_fields)
    def post(self):

        print("POST in HomeAPI")
        user_list = User.query.all()

        args = login_form_parser.parse_args()
        username = args.get("username", None)
        password = args.get("password", None)

        #cut lines from here

        if username is None:
            #return render_template("signup.html")
            return make_response(redirect("/new"))
        
        #For handling direct api calls
        else:
            #username= request.form['username']
            #password= request.form['password']
            
            print("Recieved: ", username, password)

            for user in user_list:
                print (user.username, user.password)
                if (username, password) == (user.username, user.password):
                    #return render_template("home.html", uname = username)
                    return make_response(redirect("/user/"+username))
            return make_response(render_template("welcome.html", message="Invalid username or password, please check"), 200)
        
        
            '''
        if "login" in request.json.keys(): #it was "request.form.keys earlier
            username = request.form["username"]
            password = request.form["password"]
            for user in user_list:
                print (user.username, user.password)
                if (username, password) == (user.username, user.password):
                    #return render_template("home.html", uname = username)
                    return redirect("/user/"+username)
            
                return make_response(render_template("welcome.html", message="Invalid username or password, please check"))'''