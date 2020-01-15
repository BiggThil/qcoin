from flask import Flask, escape, request, render_template
from tesst import hello_world

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    result = hello_world()
    return render_template('index.html', title='Random bits', result=result)
# def hello():
#     name = hello_world()
#     return f'Hello, {escape(name)}!'
        
# @app.route('/')
# def hello2():
#     test = hello_world()
#     return f'hello_world says: "{escape(test)}".'