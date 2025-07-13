import os
import requests
from dotenv import load_dotenv

load_dotenv()

class SignalSender:
    def __init__(self):
        self.webhook_url = os.getenv("WEBHOOK_URL")
        self.webhook_secret = os.getenv("WEBHOOK_SECRET")

        if not self.webhook_url:
            raise ValueError("Missing WEBHOOK_URL")
        if not self.webhook_secret:
            raise ValueError("Missing WEBHOOK_SECRET")

    def send_signal_webhook(self, identifier, signal_name, signal_type, sl, symbol, tps):
        payload = {
            "identifier": identifier,
            "signalName": signal_name,
            "type": signal_type,
            "sl": sl,
            "symbol": symbol,
            "tps": tps,
        }

        headers = {
            "Content-Type": "application/json",
            "x-webhook-secret": self.webhook_secret,
        }

        response = requests.post(self.webhook_url, json=payload, headers=headers)

        try:
            return response.json()
        except ValueError:
            return {
                "status": response.status_code,
                "text": response.text
            }
