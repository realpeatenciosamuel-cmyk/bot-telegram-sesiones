import os
import time
from datetime import datetime
import pytz
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot de Telegram activo y funcionando."

# Credenciales de tu bot y grupo
TOKEN = "9259372426:AAH5Xnih6bXZdeRqGZtFLge5kBuFbdQ3Az0"
CHAT_ID = "-1003919002803"

def enviar_mensaje(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": texto, "parse_mode": "Markdown"}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Error al enviar mensaje: {e}")

# Funciones de horario (UTC)
def alerta_asia():
    enviar_mensaje("🇯🇵 *¡Apertura de Sesión Asia (Tokio)!* El mercado asiático ha abierto.")

def alerta_londres():
    enviar_mensaje("🇬🇧 *¡Apertura de Sesión Londres!* Ha iniciado la sesión europea.")

def alerta_new_york():
    enviar_mensaje("🇺🇸 *¡Apertura de Sesión Nueva York!* Ha iniciado la sesión americana.")

# Configurar el planificador
scheduler = BackgroundScheduler(timezone=pytz.utc)
scheduler.add_job(alerta_asia, 'cron', hour=0, minute=0)
scheduler.add_job(alerta_londres, 'cron', hour=8, minute=0)
scheduler.add_job(alerta_new_york, 'cron', hour=13, minute=0)
scheduler.start()

if __name__ == "__main__":
    # Render asigna un puerto automáticamente mediante la variable de entorno PORT
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
