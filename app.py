from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os
import psycopg2

app = Flask(__name__)

# 🔐 OPENAI
os.environ["OPENAI_API_KEY"] = ""
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

# ---------------- DATABASE ----------------
def get_connection():
    return psycopg2.connect(
        database="mojadolezitadatabaza",
        user="mojadolezitadatabaza_user",
        password="nbPhlHM6AlCB60m1ebluwkEwv4yf1p29",
        host="dpg-d7ng6tugvqtc73ar66pg-a.oregon-postgres.render.com",
        port=5432
    )

# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("index.html")

# ---------------- SORT STUDENTS ----------------
@app.route("/students")
def get_students():

    sort = request.args.get("sort")

    conn = get_connection()
    cur = conn.cursor()

    # BONUS: viac variantov zoraďovania
    if sort == "age_desc":
        query = "SELECT * FROM students ORDER BY age DESC"

    elif sort == "age_asc":
        query = "SELECT * FROM students ORDER BY age ASC"

    elif sort == "name":
        query = "SELECT * FROM students ORDER BY name ASC"

    elif sort == "iq":
        query = "SELECT * FROM students ORDER BY iq DESC"

    else:
        query = "SELECT * FROM students"

    cur.execute(query)

    rows = cur.fetchall()

    students = []

    for s in rows:
        students.append({
            "id": s[0],
            "name": s[1],
            "age": s[2],
            "iq": s[3],
            "image": s[4]
        })

    cur.close()
    conn.close()

    return jsonify(students)

# ---------------- CHAT ----------------
@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()
    user_msg = data.get("message")

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": """
Si AI chatbot pre školskú stránku.
"""
                },
                {"role": "user", "content": user_msg}
            ]
        )

        reply = response.choices[0].message.content

    except Exception as e:
        reply = f"Chyba AI: {e}"

    return jsonify({"reply": reply})

# ---------------- START ----------------
if __name__ == "__main__":
    app.run(debug=True)
