from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

@app.route("/", methods=["GET"])
def hello():
    return "Hello World!"

@app.route("/users", methods=["POST"])
def create_user():
    try:
        data = request.get_json()
        name = data["name"]
        age = data["age"]
        user = {"name": name, "age": age}
        return jsonify(user)
    except Exception as e:
        logger.error("Error creating user", exc_info=True)
        return jsonify({"message": str(e)}), 400

if __name__ == "__main__":
    main()