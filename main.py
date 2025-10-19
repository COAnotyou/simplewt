from flask import Flask
import requests

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1409649940321276060/lgqC2HqRj_OnEPeIVbiutb-z8ibnY3utMfinFT0dujRCuZ-tKe-81BbpcNvbRYFbz4yo"

@app.route("/")
def home():
    # Nachricht an den Webhook schicken
    payload = {
        "content": "Jemand hat deine Website besucht!"
    }
    try:
        requests.post(WEBHOOK_URL, json=payload)
    except Exception as e:
        print(f"Fehler beim Senden des Webhooks: {e}")
    
    return "<h1>Haello World!</h1><p>Website runs</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
