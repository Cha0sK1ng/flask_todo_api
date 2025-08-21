from flask import Flask, jsonify, request

app = Flask(__name__)

idx = 1
tasks = []

class Task:
    def __init__(self, id, title, completed):
        self.id = id
        self.title = title
        self.completed = completed

@app.route('/tasks/<int:id>', methods=['PUT'])
def put_value():
    json = request.get_json()
    to_update = None

    for task in tasks:
        if task.id == id:
            to_update = task
            break
    if to_update is None:
        return jsonify({"msg": "PUT FAILED"}), 404
    if json is None:
        return jsonify({"msg": "PUT FAILED"}), 400
    if 'title' in json and type(json['title']) is str and len(json['title']) > 0:
        to_update.title = json['title']
    if 'completed' in json and type(json['completed']) is bool:
        to_update.completed = json['completed']
    return jsonify({"msg": "PUT OK"}), 200

@app.route('/tasks', methods=['POST'])
def set_value():
    global idx
    json = request.get_json()
    if json is None:
        return jsonify({"msg": "POST FAILED"}), 400
    if 'title' not in json:
        return jsonify({"msg": "POST FAILED"}), 400
    if type(json['title']) is not str or len(json['title']) == 0:
        return jsonify({"msg": "POST FAILED"}), 400
    new_task = Task(id=idx, title=json['title'], completed=False)
    idx += 1
    tasks.append(new_task)
    return jsonify({"msg": "POST OK"}), 201

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_value():
    pass

@app.route('/tasks', methods=['GET'])
def get_value():
    if not tasks:
        return jsonify({"msg": "GET FAILED"}), 404
    val = [{"id": task.id, "title": task.title, "completed": task.completed} for task in tasks]
    return jsonify({"msg" : "GET OK", "value": val}), 200

if __name__ == '__main__':
    app.run()

