import os
import requests
from flask import Flask, request
from openai import OpenAI

app = Flask(__name__)

# --- CONFIGURATIE ---
TOKEN = "8779369461:AAHbUNmOoWReG8LS8rF7TSWt6mn1fNrZYLk"
CHAT_ID = "6644788112"
client = OpenAI(api_key="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")

def stuur_naar_telegram(bericht):
    url = f"https://telegram.org{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={bericht}"
    r = requests.get(url)
    print(f"📡 Telegram Status: {r.status_code}")

@app.route('/')
@app.route('/webhook', methods=['POST', 'GET'])
def home():
    print("🔔 SYNC ONTVANGEN!")
    stuur_naar_telegram("🚀_MOGWAI_SYSTEEM_ONLINE")
    return "SYSTEEM ACTIEF", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
