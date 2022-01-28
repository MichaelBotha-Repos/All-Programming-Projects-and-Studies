"""
    Below is code relating to an API for a distributed system.
    Relevant exercise questions follow.
"""

from flask import Flask
from flask_restful import Api, Resource, reqparse
 
app = Flask(__name__)
api = Api(app)
 
users = [
    {
        "name": "James",
        "age": 30,
        "occupation": "Network Engineer"
    },
    {
        "name": "Ann",
        "age": 32,
        "occupation": "Doctor"
    },
    {
        "name": "Jason",
        "age": 22,
        "occupation": "Web Developer"
    }
]
 
class User(Resource):
    def get(self, name):
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 404
 
    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()
 
        for user in users:
            if(name == user["name"]):
                return "User with name {} already exists".format(name), 400
 
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201
 
    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()
 
        for user in users:
            if(name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200
        
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201
 
    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200
      
api.add_resource(User, "/user/<string:name>")
 
app.run(debug=True)

"""
Question 1
Run the API.py code. Take a screenshot of the terminal output.
What command did you use to compile and run the code?

The relevant dependencies had be installed first. The source
code was then copied and pasted into my local IDE and run
from there. One can also just execute the .py file by double clicking
the application file.

A normal Flask webserver CLI is shown, with various related information
displayed.

Question 2
Run the following command at the terminal prompt: w3m http://127.0.0.1:5000/user/Ann

What happens when this command is run, and why?

When entering the URL in my browser a dictionary is returned containing the
name requested with the associated age and occupation. This is returned because
the program has an API in the Flask webserver, where the various HTTP
methods of get, post, put, and delete have been defined for a specific URL via
the "User" class once inheriting the "Resource" class. Each defined method takes
the name submitted in the URL, and uses it when parsingthe global "users" dictionary.
After parsing the dictionary a new dictionary is formed and returned as a JSON object
by FLask to the original requester along with the relevant HTTP response code.


Question 3
Run the following command at the terminal prompt: w3m http://127.0.0.1:5000/user/Adam
What happens when this command is run, and why?

The output says: "User not found", beacuse there is no such name as Adam stored in the
global "users" dictionary. Furthermore, the HTTP method submitted to the server would
have been a "GET", and hence the appropriate code for searching for the submitted name
was executed.

Question 4
What capability is achieved by the flask library?

The library has provided a facility to access specific user data stored within
an object in a process, by using HTTP URLs. 

"""
