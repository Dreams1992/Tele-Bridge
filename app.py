import os
import requests
from flask import Flask, request

app = Flask(__name__)

TOKEN = "8779369461:AAHbUNmOoWReG8LS8rF7TSWt6mn1fNrZYLk"
CHAT_ID = "6644788112"

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    try:
        # We maken de tekst voor het bericht
        tekst = "HET_WERKT_NU_ECHT_VIA_RENDER"
        
        # We bouwen de URL stap voor stap op om fouten te voorkomen
        base_url = f"https://telegram.org{TOKEN}/sendMessage"
        params = {
            "chat_id": CHAT_ID,
            "text": tekst
        }
        
        # Vuur het bericht af
        r = requests.get(base_url, params=params, timeout=10)
        return "OK", 200
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    # Render vereist poort 10000
    app.run(host='0.0.0.0', port=10000)
