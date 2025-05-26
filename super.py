import subprocess
import time


def main():
    while True:
        print("Launching runner.py...")
        subprocess.Popen(["python3", "runner.py"])
        print("Waiting 150 seconds before launching the next runner.py...")
        time.sleep(240)


if __name__ == "__main__":
    main()
