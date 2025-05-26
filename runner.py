import subprocess
from concurrent.futures import ThreadPoolExecutor


def run_instance(i):
    print(f"Starting stake.py instance {i}")
    subprocess.run(["python", "stake.py"])
    print(f"stake.py instance {i} finished")


if __name__ == "__main__":
    num_instances = 10
    with ThreadPoolExecutor(max_workers=num_instances) as executor:
        executor.map(run_instance, range(1, num_instances + 1))
