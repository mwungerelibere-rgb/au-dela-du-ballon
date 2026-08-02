import time
import subprocess
from datetime import datetime


def update_news():

    print("\n🌍 BEYOND THE BALL")
    print("Updating newsroom...")
    print(datetime.now())


    try:
        subprocess.run(
            ["python", "beyond_agent.py"]
        )

        print("✅ Update completed")

    except Exception as e:

        print("❌ Update error:", e)



while True:

    update_news()


    print("⏳ Waiting 1 hour for next update...")


    time.sleep(3600)
