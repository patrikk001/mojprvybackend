from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

databaza = {
    "students": [
        {
            "id": 1,
            "name": "Samuel Uhrík",
            "age": 12,
            "iq": 20,
            "image": "https://picsum.photos/200?random=1"
        },
        {
            "id": 2,
            "name": "Tomáš Jurčák",
            "age": 61,
            "iq": 2,
            "image": "https://picsum.photos/200?random=2"
        },
        {
            "id": 3,
            "name": "Marko Mihalička",
            "age": 19,
            "iq": 67,
            "image": "https://picsum.photos/200?random=3"
        }
    ]
}

@app.route("/api")
def api():
    return jsonify(databaza)

if __name__ == "__main__":
    app.run(debug=True)