import subprocess
import sys

if __name__ == "__main__":
    try:
        subprocess.run(
            ["pipenv", "--venv"],
            check=True,
            stderr=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        subprocess.run(["pipenv", "sync", "--dev"])
    finally:
        if len(sys.argv) > 1:
            subprocess.run(sys.argv[1:])
