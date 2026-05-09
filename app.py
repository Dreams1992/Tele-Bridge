import os
import requests
from flask import Flask, request

app = Flask(__name__)

# JOUW TELEGRAM DATA
TOKEN = "8779369461:AAHbUNmOoWReG8LS8rF7TSWt6mn1fNrZYLk"
CHAT_ID = "6644788112"

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    try:
        # We proberen data van MT5 te pakken, anders gebruiken we een testbericht
        if request.is_json:
            data = request.get_json(force=True)
            symbol = data.get('symbol', 'MOGWAI')
            action = data.get('action', 'LIVE')
            msg = f"🎯 SNIPER UPDATE\nSymbool: {symbol}\nStatus: {action}"
        else:
            msg = "🚀 MOGWAI SYNC: Verbinding met Render is geslaagd!"

        # DE EXACTE METHODE DIE IN JE BROWSER WERKT:
        url = f"https://telegram.org{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}"
        
        # Vuur het bericht af
        r = requests.get(url)
        print(f"Telegram Feedback: {r.text}")
        
        return "OK", 200
    except Exception as e:
        print(f"Fout: {str(e)}")
        return "Error", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
