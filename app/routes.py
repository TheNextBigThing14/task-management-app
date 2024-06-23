# app/routes.py
from flask import request, jsonify, current_app as app
from app.models import Task
from app import db

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.as_dict() for task in tasks])

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.query.get_or_404(id)
    return jsonify(task.as_dict())

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = Task(
        title=data['title'],
        description=data['description'],
        due_date=data['due_date']
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.as_dict()), 201

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()
    task = Task.query.get_or_404(id)
    task.title = data['title']
    task.description = data['description']
    task.due_date = data['due_date']
    db.session.commit()
    return jsonify(task.as_dict())

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return '', 204
