import mpl_toolkits.mplot3d.art3d as art3d
from matplotlib.patches import PathPatch
from matplotlib.text import TextPath
from matplotlib.transforms import Affine2D


class Text3D(PathPatch):
    def __init__(self, xyz, text, zdir="z", size=None, angle=0, usetex=False, **kwargs):
        match zdir:
            case "x":
                x, y, z = (xyz[1], xyz[2], xyz[0])

            case "y":
                x, y, z = (xyz[0], xyz[2], xyz[1])

            case "z":
                x, y, z = (xyz[0], xyz[1], xyz[2])

        trans = Affine2D().rotate(angle).translate(x, y)
        path = TextPath((0, 0), text, size=size, usetex=usetex)
        super().__init__(trans.transform_path(path), **kwargs)
        self.__z = z
        self.__zdir = zdir

    def to_3d(self):
        art3d.pathpatch_2d_to_3d(self, z=self.__z, zdir=self.__zdir)
