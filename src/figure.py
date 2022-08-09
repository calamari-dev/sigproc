import subprocess
from pathlib import Path

if __name__ == "__main__":
    selfdir = Path(__file__).parent

    for fig in selfdir.glob("chapter/**/*.py"):
        print("processing chapter/**/" + fig.name + " ...")
        cwd = fig.parent.as_posix()
        subprocess.run(["python", fig.name], cwd=cwd)

    for tex in filter(lambda x: x.stem != "index", selfdir.glob("chapter/**/*.tex")):
        print("processing chapter/**/" + tex.name + " ...")
        cwd = tex.parent.as_posix()
        subprocess.run(["lualatex", tex.stem], cwd=cwd, stdout=subprocess.DEVNULL)
