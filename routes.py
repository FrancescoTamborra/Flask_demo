from app import app
from flask import render_template

import forms # we nned to import our form

@app.route('/') # we use a decorator for the next function applied to the route /
@app.route('/index') # we can apply the same function index to multiple routes
def index():
    return render_template('index.html', current_title='Custom Title') # Flask has Jinja tamplate engine which allows to render much more than plain html (dynamic)

@app.route('/about', methods=['GET', 'POST']) # by default it accept GET requests. We have to specify the POST
def about():
    form = forms.AddTaskForm() # instance of our form class
    if form.validate_on_submit(): # when post is a success we do stuff
        print('Submitted_title', form.title.data) # print in terminal (logs)
        return render_template('about.html', form=form, title=form.title.data) # we pass it to the render via title variable (see about.html)
    return render_template('about.html', current_title='Custom Title', form=form) # in the render we call it form
