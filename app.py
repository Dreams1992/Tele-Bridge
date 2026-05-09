import os
import requests
from flask import Flask, request
from openai import OpenAI

app = Flask(__name__)

# --- CONFIGURATIE ---
TOKEN = "8779369461:AAHbUNmOoWReG8LS8rF7TSWt6mn1fNrZYLk"
CHAT_ID = "6644788112"
# Jouw API Key
client = OpenAI(api_key="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")

def send_telegram(msg):
    url = f"https://api.telegram.org{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}"
    requests.get(url)

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    try:
        # Als MT5 data stuurt
        if request.is_json:
            data = request.get_json(force=True)
            symbol = data.get('symbol', 'MOGWAI')
            market_data = data.get('action', '')

            # AI Analyse aanroep
            prompt = f"Analyseer: {symbol} op {market_data}. Is dit een BUY of SELL voor een wave? Kort antwoord."
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=50
            )
            ai_advies = response.choices.message.content
            send_telegram(f"🧠 AI UPDATE: {symbol}\n{ai_advies}")
        
        return "OK", 200
    except Exception as e:
        print(f"Fout: {e}")
        return str(e), 500

# Forceer een bericht bij het opstarten van de server
send_telegram("🚀 AI COMMANDER IS ONLINE EN VERBONDEN")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
