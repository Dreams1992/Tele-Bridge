import os
import requests
from flask import Flask, request

app = Flask(__name__)

# JOUW TELEGRAM DATA
TOKEN = "8779369461:AAHbUNmOoWReG8LS8rF7TSWt6mn1fNrZYLk"
CHAT_ID = "6644788112"

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json(force=True)
        symbol = data.get('symbol', 'TEST')
        action = data.get('action', 'LIVE')
        msg = f"🚀 MOGWAI TEST\nSymbool: {symbol}\nActie: {action}"
        
        # We bouwen de URL exact op
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        params = {"chat_id": CHAT_ID, "text": msg}
        
        # Verstuur en vang het resultaat op
        print(f"📡 Poging om bericht te sturen voor {symbol}...")
        r = requests.get(url, params=params, timeout=10)
        
        print(f"📊 Telegram antwoord: {r.status_code} - {r.text}")
        
        return "OK", 200
    except Exception as e:
        print(f"❌ KRITIEKE FOUT: {str(e)}")
        return "Error", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
