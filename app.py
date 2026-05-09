import os
from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "8779369461:AAHbUNmOoWReG8LS8rF7TSWt6mn1fNrZYLk"
CHAT_ID = "6644788112"

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json(force=True)
        symbol = data.get('symbol', 'TEST')
        action = data.get('action', 'LIVE')
        
        msg = f"🚀 MOGWAI ALERTE\nSymbool: {symbol}\nActie: {action}"
        
        # Directe URL aanroep zoals in de browser
        url = f"https://api.telegram.org{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}"
        requests.get(url)
        
        return "OK", 200
    except Exception as e:
        print(f"Fout: {e}")
        return "Error", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
