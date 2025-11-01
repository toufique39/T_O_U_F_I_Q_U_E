import requests
from pydub import AudioSegment
from pydub.playback import play
from io import BytesIO
import datetime

def log(message: str):
    """Simple timestamped logger"""
    print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}")

def play_audio_from_url(url: str):
    """Download and play audio from OrangeCarrier link"""
    try:
        log(f"🔊 Fetching audio from: {url}")
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            audio = AudioSegment.from_file(BytesIO(response.content), format="wav")
            play(audio)
            log("✅ Audio played successfully.")
        else:
            log(f"❌ Failed to fetch audio. Status code: {response.status_code}")
    except Exception as e:
        log(f"⚠️ Error playing audio: {e}")
