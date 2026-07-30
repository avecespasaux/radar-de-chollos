import os
import asyncio
from telegram import Bot

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@RadarDeChollosES"

async def main():
    bot = Bot(token=TOKEN)

    await bot.send_message(
        chat_id=CHANNEL,
        text="📡 ¡Hola! Soy el bot de Radar de Chollos 🤖🔥\n\nPrueba de conexión realizada correctamente."
    )

    print("Mensaje enviado correctamente.")

if __name__ == "__main__":
    asyncio.run(main())
