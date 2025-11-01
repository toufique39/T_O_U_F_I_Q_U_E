import asyncio
import json
import requests
from utils import log, play_audio_from_url


async def start_listener():
    log("🎧 Listening for incoming OrangeCarrier audio links...")

    # Demo: periodic check
    while True:
        try:
            with open("config.json", "r") as file:
                config = json.load(file)

            url = config.get("test_audio_url", "")
            if url:
                play_audio_from_url(url)

            await asyncio.sleep(120)  # প্রতি ২ মিনিট পর আবার চেক করবে
        except Exception as e:
            log(f"⚠️ Error in listener: {e}")
            await asyncio.sleep(10)
