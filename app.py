from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os
import psycopg2

app = Flask(__name__)

os.environ["OPENAI_API_KEY"] = ""
# 🔐 API KEY (musí byť nastavený v systéme)
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❌ CHYBA: OPENAI_API_KEY nie je nastavený!")

client = OpenAI(api_key=api_key)

# 🏠 homepage
@app.route("/")
def home():
    conn = psycopg2.connect(
        database="mojadolezitadatabaza",
        user="mojadolezitadatabaza_user",
        password="nbPhlHM6AlCB60m1ebluwkEwv4yf1p29",
        host="dpg-d7ng6tugvqtc73ar66pg-a.oregon-postgres.render.com",
        port=5432
    )

    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM students
    """)

    databaza = cur.fetchall()
    
def sort_users():
    cur = conn.cursor()
    cur.execute("SELECT * FROM students ORDER BY name ASC")
    databaza = cur.fetchall()
    cur.close()
    return jsonify(databaza)
    print(databaza)

    return render_template("index.html", students=databaza)

# 🤖 AI CHAT
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message")

    print("➡ USER:", user_msg)

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": f"""
Si AI chatbot pre školskú stránku.
Používaj tieto dáta o študentoch:


Ak odpoveď nevieš z dát, povedz:
"Neviem z dostupných údajov."
"""
                },
                {"role": "user", "content": user_msg}
            ]
        )

        reply = response.choices[0].message.content
        print("🤖 AI:", reply)

    except Exception as e:
        print("❌ OPENAI ERROR:", e)
        reply = f"Chyba AI: {e}"

    return jsonify({"reply": reply})


# 🚀 start server
if __name__ == "__main__":
    app.run(debug=True)
