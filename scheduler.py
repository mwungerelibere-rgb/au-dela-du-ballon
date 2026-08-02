import time
import subprocess

while True:
    print("\n🚀 Running BEYOND THE BALL...\n")

    subprocess.run(["python", "beyond_agent.py"])

    print("\n⏳ Waiting 1 hour...\n")

    time.sleep(3600)
