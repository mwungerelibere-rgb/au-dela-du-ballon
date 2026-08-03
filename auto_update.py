import time
import subprocess
from datetime import datetime


def update_news():

    print("\n🌍 BEYOND THE BALL")
    print("Updating newsroom...")
    print(datetime.now())


    try:

        # Collect and process news
        subprocess.run(
            ["python", "beyond_agent.py"]
        )

        # Export new data to news.json
        subprocess.run(
            ["python", "export_news.py"]
        )

        print("✅ Update completed")

    except Exception as e:

        print("❌ Update error:", e)



while True:

    update_news()

    print("⏳ Waiting 1 hour for next update...")

    time.sleep(3600)
