from flask import Blueprint, request, jsonify
from app import db
from models import User, Task

# Defining Blueprints
api_blueprint = Blueprint('api', __name__)
task_routes = Blueprint('tasks', __name__)

# User registration route
@api_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400
    
    # Create and save new user
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

# Task creation route (for the API blueprint)
@api_blueprint.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    
    if not title:
        return jsonify({"error": "Title is required"}), 400
    
    # Creating and saving new task
    task = Task(title=title, description=description)
    db.session.add(task)
    db.session.commit()
    
    return jsonify({"message": "Task created successfully"}), 201

# Defining task routes
@task_routes.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    
    if not title:
        return jsonify({"error": "Title is required"}), 400
    
    new_task = Task(title=title, description=description)
    db.session.add(new_task)
    db.session.commit()
    
    return jsonify({'id': new_task.id}), 201

@task_routes.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks]), 200

@task_routes.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get_or_404(task_id)
    return jsonify(task.to_dict()), 200

@task_routes.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = Task.query.get_or_404(task_id)
    
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    db.session.commit()
    
    return jsonify(task.to_dict()), 200

@task_routes.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    
    return jsonify({'message': 'Task deleted'}), 200
