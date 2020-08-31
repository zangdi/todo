from flask import render_template, request, redirect, url_for, jsonify
from app import app, models, db

Task = models.Task

@app.route('/')
def index():
    title = "My Personal Todo Application"
    tasks = Task.query.all()
    return render_template("index.html", title=title, tasks=tasks)

@app.route('/task/', methods=['POST'])
def add_item():
    # Get data from form fields taskName and taskDescription
    taskName = request.form.get('taskName')
    taskDescription = request.form.get('taskDescription')

    new_item = Task(name=taskName, description=taskDescription)

    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/task/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.filter_by(id=id).first()

    if (task != None):
        msg = {
            'message': 'Delete successful'
        }

        db.session.delete(task)
        db.session.commit()
        return jsonify(msg), 200
    
    msg = {
        'message': 'Task not found'
    }
    return jsonify(msg), 204

@app.route('/task/<int:id>', methods=['GET', 'POST'])
def view_task(id):
    if (request.method == "GET"):
        task = Task.query.filter_by(id=id).first()
        return render_template('view_task.html', taskName=task.name, taskDescription=task.description, taskId=task.id)
    elif (request.method == "POST"):
        taskId = request.form.get('taskId')
        taskName = request.form.get('taskName')
        taskDescription = request.form.get('taskDescription')
        
        task = Task.query.filter_by(id=id).first()
        if (task != None):
            task.name = taskName
            task.description = taskDescription
            db.session.add(task)
            db.session.commit()
        return redirect(url_for('index'))