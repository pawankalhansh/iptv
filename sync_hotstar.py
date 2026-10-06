import urllib.request
import os

SOURCE_URL = "https://raw.githubusercontent.com/Sflex0719/JH4K/main/JHS.m3u"
OUTPUT_FILE = "hotstar.m3u"

def sync():
    try:
        req = urllib.request.Request(
            SOURCE_URL,
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read().decode("utf-8")
        
        if content and "#EXTM3U" in content:
            with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Successfully synced {OUTPUT_FILE} ({len(content)} bytes)")
        else:
            print("Received invalid content, skipping update.")
    except Exception as e:
        print(f"Error syncing Hotstar playlist: {e}")

if __name__ == "__main__":
    sync()
