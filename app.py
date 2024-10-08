from flask import request, jsonify
from .models import Task
from . import create_app, db  

app = create_app()  

# Get tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks]) 

# Add task
@app.route('/tasks', methods=['POST'])
def add_tasks():
    data = request.json
    new_task = Task(title=data['title'],description=data['description'], completed=False)  
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict())

# Update task by id
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    task = Task.query.get_or_404(task_id)
    task.title = data['title']
    task.completed = data['completed']
    task.description=data['description']
    db.session.commit()
    return jsonify(task.to_dict())

# Delete task by id
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return 'Task deleted successfully!'

if __name__ == '__main__':
    app.run(debug=True)