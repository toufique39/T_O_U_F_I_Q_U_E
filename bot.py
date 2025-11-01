import asyncio
from listener import start_listener
from utils import log

async def main():
    log("🚀 Orange Call Bot started successfully!")
    await start_listener()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        log("🛑 Bot stopped manually.")
