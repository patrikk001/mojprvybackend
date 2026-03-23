from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy databáza
items = [
]


# Root endpoint
@app.route("/")
def home():
    return jsonify({"message": "Flask backend beží!"})

databaza = {
    "students": [
        {
            "id": 1,
            "name": "Samuel Uhrík",
            "age": 12,
            "iq": 20
        },{
            "id": 2,
            "name": "Tomáš Jurčák",
            "age": 61,
            "iq": 2
        },{
            "id": 3,
            "name": "Marko Mihalička",
            "age": 19,
            "iq": 67
        }
    ]
}

@app.route("/api")
def api():
    return jsonify(databaza)

@app.route("/api/students/<int:student_id>")
def find_students(student_id):
    for student in databaza["students"]:
        if student["id"] == student_id:
            return jsonify(student)
    return jsonify({"error": "Student not found"})  

if __name__ == "__main__":
    app.run(debug=True)