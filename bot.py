import os
import asyncio
from telegram import Bot

TOKEN = os.getenv("BOT_TOKEN")


async def main():
    bot = Bot(token=TOKEN)

    print("🤖 Radar de Chollos está funcionando correctamente.")

    # Mantener el proceso activo
    while True:
        await asyncio.sleep(60)


if __name__ == "__main__":
    asyncio.run(main())
