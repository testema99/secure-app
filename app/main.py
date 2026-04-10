from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, Secure World!"})

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    try:
        x = int(data.get("x"))
        y = int(data.get("y"))
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input"}), 400
    return jsonify({"result": x + y})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

