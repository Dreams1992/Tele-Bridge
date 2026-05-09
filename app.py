import os
import requests
from flask import Flask, request
from openai import OpenAI

app = Flask(__name__)

# --- JOUW GEGEVENS ---
TOKEN = "8779369461:AAHbUNmOoWReG8LS8rF7TSWt6mn1fNrZYLk"
CHAT_ID = "6644788112"
# Jouw OpenAI Key
client = OpenAI(api_key="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")

def stuur_bericht(tekst):
    url = f"https://telegram.org{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": tekst}
    requests.post(url, json=payload)

@app.route('/', methods=['POST', 'GET'])
def telegram_partner():
    update = request.get_json(silent=True)
    
    if update and "message" in update:
        user_text = update["message"].get("text", "")
        
        # AI denkt na over jouw bericht
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Je bent de persoonlijke trading partner. Praat als een gelijke, wees scherp en help de 100k challenge te winnen."},
                {"role": "user", "content": user_text}
            ]
        )
        
        antwoord = response.choices.message.content
        stuur_bericht(antwoord)
        
    return "OK", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
