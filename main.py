from flask import Flask, request, jsonify

app = Flask(__name__)

todos = []


@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)


@app.route("/todo", methods=["POST"])
def create_todo():
    todo_data = request.get_json()
    todos.append(todo_data)
    return jsonify(todos)


@app.route("/todo/<int:id>", methods=["DELETE"])
def delete_todo(id):
    todos.pop(id)
    return jsonify(todos)


@app.route("/todo/<int:id>", methods=["PUT"])
def update_todo(id):
    todo_data = request.get_json()
    todos[id] = todo_data
    return jsonify(todos)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
