import os
from flask import Flask, request
import requests

app = Flask(__name__)

# JOUW TELEGRAM DATA
TOKEN = "8779369461:AAHbUNmOoWReG8LS8rF7TSWt6mn1fNrZYLk"
CHAT_ID = "6644788112"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json(force=True)
    msg = f"🚀 MOGWAI BRIDGE: {data.get('symbol', 'TEST')} - {data.get('action', 'LIVE')}"
    url = f"https://telegram.org{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": msg})
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
