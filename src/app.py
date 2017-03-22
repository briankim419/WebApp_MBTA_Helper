"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request

from mbta_helper import find_stop_near
app = Flask(__name__)

app.config['DEBUG'] = True
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def location():
    place_name = str(request.form[''])
    if request.method == 'POST':
        find_stop_near(place_name):
    else:
        show_the_login_form()




if __name__ == '__main__':
    app.run()
