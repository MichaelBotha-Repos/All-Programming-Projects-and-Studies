from flask import Flask, render_template

my_app = Flask(__name__)

@my_app.route('/home')
def home():
    
    return render_template('home.html')

my_app.run()
