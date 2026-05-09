import os
from flask import Flask, request
import requests

app = Flask(__name__)

# JOUW TELEGRAM DATA
TOKEN = "8779369461:AAHbUNmOoWReG8LS8rF7TSWt6mn1fNrZYLk"
CHAT_ID = "6644788112"

# DIT IS DE BELANGRIJKSTE REGEL (De deur naar de webhook)
@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    try:
        # We proberen de data van MetaTrader te lezen
        data = request.get_json(force=True)
        symbol = data.get('symbol', 'MOGWAI')
        action = data.get('action', 'LIVE')
    except:
        symbol = "TEST"
        action = "RESTART"

    msg = f"🚀 MOGWAI ALERTE\nSymbool: {symbol}\nStatus: {action}"
    
    # De link die je browser succesvol testte
    url = f"https://api.telegram.org{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}"
    
    # Verstuur naar Telegram
    requests.get(url)
    
    return "OK", 200

if __name__ == "__main__":
    # Render vereist poort 10000 of de PORT variabele
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
