from pathlib import Path
import subprocess

filedir = Path(__file__).parent

for fig in filedir.glob("chapter/**/*.py"):
    print("running ./chapter/**/" + fig.name + " ...")
    subprocess.run(["black", fig.name], cwd=fig.parent.as_posix())
    subprocess.run(["python", fig.name], cwd=fig.parent.as_posix())


subprocess.run(["llmk", "-C"])
subprocess.run("llmk")
