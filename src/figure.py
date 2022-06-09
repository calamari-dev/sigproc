from pathlib import Path
import subprocess

filedir = Path(__file__).parent

for fig in filedir.glob("chapter/**/*.py"):
    print("processing ./chapter/**/" + fig.name + " ...")
    subprocess.run(["black", fig.name], cwd=fig.parent.as_posix())
    subprocess.run(["python", fig.name], cwd=fig.parent.as_posix())

for tex in filedir.glob("chapter/**/*.tex"):
    if tex.stem == "index":
        continue

    print("processing ./chapter/**/" + tex.name + " ...")
    subprocess.run(["lualatex", tex.stem], cwd=tex.parent.as_posix(), stdout=subprocess.DEVNULL)
