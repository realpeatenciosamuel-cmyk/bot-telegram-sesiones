import os
import time
from datetime import datetime
import pytz
import requests
from apscheduler.schedulers.blocking import BlockingScheduler

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

# Funciones de horario (ajustadas a UTC)
def alerta_asia():
    enviar_mensaje("🇯🇵 *¡Apertura de Sesión Asia (Tokio)!* El mercado asiático ha abierto.")

def alerta_londres():
    enviar_mensaje("🇬🇧 *¡Apertura de Sesión Londres!* Ha iniciado la sesión europea.")

def alerta_new_york():
    enviar_mensaje("🇺🇸 *¡Apertura de Sesión Nueva York!* Ha iniciado la sesión americana.")

# Configurar el planificador de horarios (Zona horaria UTC)
scheduler = BlockingScheduler(timezone=pytz.utc)

# Horarios UTC configurados (puedes ajustarlos según tu horario local/invierno-verano)
# 00:00 UTC = Asia | 08:00 UTC = Londres | 13:00 UTC = Nueva York
scheduler.add_job(alerta_asia, 'cron', hour=0, minute=0)
scheduler.add_job(alerta_londres, 'cron', hour=8, minute=0)
scheduler.add_job(alerta_new_york, 'cron', hour=13, minute=0)

if __name__ == "__main__":
    print("Bot de sesiones iniciado...")
    scheduler.start() 