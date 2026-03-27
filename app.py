from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy databáza
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
        },
        {
            "id": 4,
            "name": "Lukáš Vindiš",
            "age": 25,
            "iq": 100,
            "image": "https://picsum.photos/200?random=4"
        },
        {
            "id": 5,
            "name": "Martin Krajčovič",
            "age": 30,
            "iq": 120,
            "image": "https://picsum.photos/200?random=5"
        },
        {
            "id": 6,
            "name": "Adam Krajčovič",
            "age": 12,
            "iq": 1,
            "image": "https://picsum.photos/200?random=6"
        },
        {
            "id": 7,
            "name": "Jožo Kováč",
            "age": 133,
            "iq": 35,
            "image": "https://picsum.photos/200?random=7"
        },
        {
            "id": 8,
            "name": "Janko Kráľ",
            "age": 19,
            "iq": 13,
            "image": "https://picsum.photos/200?random=8"
        },
        {
            "id": 9,
            "name": "Laco Strike",
            "age": 33,
            "iq": 66,
            "image": "https://picsum.photos/200?random=9"
        },
        {
            "id": 10,
            "name": "Jozef Krajčovič",
            "age": 6,
            "iq": 9,
            "image": "https://picsum.photos/200?random=10"
        }
    ]
}

# Root endpoint
@app.route("/")
def home():
    return jsonify({"message": "Flask backend beží!"})

@app.route("/api")
def api():
    return jsonify(databaza)

@app.route("/api/students/<int:student_id>")
def find_students(student_id):
    for student in databaza["students"]:
        if student["id"] == student_id:
            return jsonify(student)
    return jsonify({"error": "Student not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)