from flask import Blueprint, request, jsonify

# Defining the blueprint
api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    # Placeholder for user registration logic
    return jsonify({"message": "User registered successfully"}), 201


@api_blueprint.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    from app import db
    from models import Task
    new_task = Task(title=data['title'], description=data.get('description'))
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'id': new_task.id}), 201


@api_blueprint.route('/tasks', methods=['GET'])
def get_tasks():
    from app import db
    from models import Task
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks]), 200


@api_blueprint.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    from app import db
    from models import Task
    task = Task.query.get_or_404(task_id)
    return jsonify(task.to_dict()), 200


@api_blueprint.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    from app import db
    from models import Task
    task = Task.query.get_or_404(task_id)
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    db.session.commit()
    return jsonify(task.to_dict()), 200


@api_blueprint.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    from app import db
    from models import Task
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted'}), 200
