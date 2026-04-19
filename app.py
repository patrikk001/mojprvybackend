from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# 🔐 API KEY (musí byť nastavený v systéme)
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❌ CHYBA: OPENAI_API_KEY nie je nastavený!")

client = OpenAI(api_key=api_key)

# 📚 databáza študentov
databaza = {
    "students": [
        {"id": 1, "name": "Samuel Uhrík", "age": 12, "iq": 20, "image": "https://posvancfitness.com/wp-content/uploads/2025/06/12809_1.jpg"},
        {"id": 2, "name": "Tomáš Jurčák", "age": 61, "iq": 2, "image": "https://vedanadosah.cvtisr.sk/wp-content/uploads/importovane/img/articles/x6TpkjtO-896x600.jpg"},
        {"id": 3, "name": "Marko Mihalička", "age": 19, "iq": 67, "image": "https://www.nanogen.sk/wp-content/uploads/2024/03/ako-muzi-riesia-kuty-vo-vlasoch-2.jpg"},
        {"id": 4, "name": "Lukáš Vindiš", "age": 25, "iq": 100, "image": "https://www.svet-svietidiel.sk/led-stmievatelna-solarna-poulicna-lampa-led-12w-3-2v-6000k-ip65-10000-mah-do-img-vt2259_02-fd-11.jpg"},
        {"id": 5, "name": "Martin Krajčovič", "age": 30, "iq": 120, "image": "https://static.hnonline.sk/images/slike/2026/03/28/o_6812238_1024.jpg"}
    ]
}

# 🏠 homepage
@app.route("/")
def home():
    return render_template("index.html", students=databaza["students"])


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
{databaza['students']}

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
