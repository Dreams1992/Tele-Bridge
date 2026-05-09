import os
import requests
from flask import Flask, request

app = Flask(__name__)

# JOUW TELEGRAM DATA
TOKEN = "8779369461:AAHbUNmOoWReG8LS8rF7TSWt6mn1fNrZYLk"
CHAT_ID = "6644788112"

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    # We vangen de data op van MetaTrader
    try:
        data = request.get_json(force=True)
        symbol = data.get('symbol', 'MOGWAI')
        action = data.get('action', 'LIVE')
    except:
        symbol = "TEST"
        action = "CONNECTION"

    msg = f"🚀 MOGWAI ALERTE\nSymbool: {symbol}\nStatus: {action}"
    
    # De directe URL die we in de browser hebben getest
    url = f"https://api.telegram.org{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}"
    
    # Verstuur naar Telegram
    requests.get(url)
    
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
