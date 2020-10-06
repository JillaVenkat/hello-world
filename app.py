from flask import Flask

app = Flask(__name__)

@app.route('/')
def display_msg():
    return 'Hello child, welcome to ur new world'

@app.route('/<name>')
def welcome_msg(name):
    return 'Hi {}!'.format(name)

if __name__=='__main__':
    app.run()