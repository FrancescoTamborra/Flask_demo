from app import app, db
from flask import render_template, redirect, url_for
from datetime import datetime

import models
import forms

@app.route('/') # we use a decorator for the next function applied to the route /
@app.route('/index') # we can apply the same function index to multiple routes
def index():
    tasks = models.Task.query.all() # we query all tasks in the database and we give them to index
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST']) # by default it accept GET requests. We have to specify the POST
def add():
    form = forms.AddTaskForm() # instance of our form class
    if form.validate_on_submit(): # when post is a success we do stuff
        t = models.Task(title=form.title.data, date=datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('index')) # if success we redirect on index where all tasks are shown
    return render_template('add.html', form=form) # in the render we call it form
