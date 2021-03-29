from app import app, db
from flask import render_template, redirect, url_for, flash, get_flashed_messages
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
        flash('Task added to the database')
        return redirect(url_for('index')) # if success we redirect on index where all tasks are shown
    return render_template('add.html', form=form) # in the render we call it form

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id): # we now pass the task id used in the urls and in SQL queries
    task = models.Task.query.get(task_id)
    form = forms.AddTaskForm()
    if task:
        if form.validate_on_submit():
            task.title = form.title.data
            task.date = datetime.utcnow()
            db.session.commit()
            flash('Task has been updated')
            return redirect(url_for('index'))

        form.title.data = task.title # already filled with actual title
        return render_template('edit.html', form=form, task_id=task_id)
    else:
        flash('Task not found')
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['GET', 'POST'])
def delete(task_id):
    task = models.Task.query.get(task_id)
    form = forms.DeleteTaskForm()
    if task:
        if form.validate_on_submit():
            db.session.delete(task)
            db.session.commit()
            flash('Task has been deleted')
            return redirect(url_for('index'))

        return render_template('delete.html', form=form, task_id=task_id, title=task.title)
    else:
        flash('Task not found')
    return redirect(url_for('index'))
