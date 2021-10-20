from flask import Flask

app = Flask(__name__)

@app.route('/')
def do():
    return 'Something is up!'

@app.route('/next')
def do2():
    return 'Now something is really up!!'

app.run()
