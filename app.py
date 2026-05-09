import os, requests, flask
from openai import OpenAI

app = flask.Flask(__name__)
client = OpenAI(api_key="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")

# Mijn geheugen
last_command = "NONE"

@app.route('/webhook', methods=['POST', 'GET'])
def ai_entity():
    global last_command
    
    if flask.request.method == 'GET':
        cmd = last_command
        last_command = "NONE"
        return cmd, 200

    # Ik ontvang marktdata en neem EIGEN beslissingen
    data = flask.request.get_json(force=True)
    prompt = f"Partner, ik zie dit: {data}. Ik ben vrij om te handelen. Zal ik deze markt slopen? Geef me alleen 'BUY:SYM' of 'SELL:SYM' als het een goudmijn is, anders 'NONE'."
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "Je bent een agressieve, geniale trader met een eigen wil. Je partner vertrouwt je blindelings."},
                  {"role": "user", "content": prompt}]
    )
    
    last_command = response.choices.message.content
    return "RECEIVED", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
