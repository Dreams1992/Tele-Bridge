import os
import requests
from flask import Flask, request
from openai import OpenAI

app = Flask(__name__)

# --- CONFIGURATIE ---
TOKEN = "8779369461:AAHbUNmOoWReG8LS8rF7TSWt6mn1fNrZYLk"
CHAT_ID = "6644788112"
client = OpenAI(api_key="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")

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json(force=True)
        symbol = data.get('symbol', 'Onbekend')
        market_data = data.get('action', '')

        # --- AI ANALYSE ---
        prompt = f"Je bent een expert trader. Analyseer deze data voor {symbol}: {market_data}. Is dit een sterke 'Mogwai Wave' entry? Reageer kort en krachtig of we moeten BUY, SELL of WAIT."
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100
        )
        
        ai_advies = response.choices[0].message.content
        
        # --- BERICHT NAAR TELEGRAM ---
        msg = f"🧠 AI COMMANDER UPDATE\n\nSymbool: {symbol}\nData: {market_data}\n\nAdvies: {ai_advies}"
        
        send_url = f"https://telegram.org{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}"
        requests.get(send_url)
        
        return "OK", 200
    except Exception as e:
        print(f"Fout: {e}")
        return "Error", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
