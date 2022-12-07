import subprocess
from pathlib import Path

if __name__ == "__main__":
    selfdir = Path(__file__).parent

    for fig in selfdir.glob("chapter/**/figures/*.py"):
        print("processing " + fig.name + " ...")
        cwd = fig.parent.as_posix()
        subprocess.run(["python", fig.name], cwd=cwd)

    for tex in selfdir.glob("chapter/**/figures/*.tex"):
        print("processing " + tex.name + " ...")
        cwd = tex.parent.as_posix()
        subprocess.run(["lualatex", tex.stem], cwd=cwd, stdout=subprocess.DEVNULL)
