import subprocess
from pathlib import Path

selfdir = Path(__file__).parent

for fig in selfdir.glob("chapter/**/*.py"):
    print("processing chapter/**/" + fig.name + " ...")
    subprocess.run(["python", fig.name], cwd=fig.parent.as_posix())

for tex in filter(lambda x: x.stem != "index", selfdir.glob("chapter/**/*.tex")):
    print("processing chapter/**/" + tex.name + " ...")
    subprocess.run(
        ["lualatex", tex.stem], cwd=tex.parent.as_posix(), stdout=subprocess.DEVNULL
    )
