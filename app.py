import os
from flask import Flask, request
import requests

app = Flask(__name__)

# JOUW TELEGRAM DATA
TOKEN = "8779369461:AAHbUNmOoWReG8LS8rF7TSWt6mn1fNrZYLk"
CHAT_ID = "6644788112"

# DEZE REGEL MOET EXACT ZO ZIJN:
@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    try:
        data = request.get_json(force=True)
        symbol = data.get('symbol', 'TEST')
        action = data.get('action', 'LIVE')
    except:
        symbol = "MOGWAI"
        action = "SYNC"

    msg = f"🚀 MOGWAI ALERTE\nSymbool: {symbol}\nStatus: {action}"
    
    # De link die in je browser werkte
    https://api.telegram.org/bot8779369461:AAHbUNmOoWReG8LS8rF7TSWt6mn1fNrZYLk/sendMessage?chat_id=6644788112&text=HET_WERKT_EINDELIJK"
    requests.get(url)
    
    return "OK", 200

if __name__ == "__main__":
    # Render gebruikt poort 10000
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
