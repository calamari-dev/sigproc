from mpl_toolkits.mplot3d.proj3d import proj_transform
from matplotlib.patches import FancyArrowPatch
import numpy as np


class Arrow3D(FancyArrowPatch):
    def __init__(self, posA, posB, *args, **kwargs):
        super().__init__((0, 0), (0, 0), *args, **kwargs)
        self.__xyzs = np.transpose((posA, posB))

    def draw(self, renderer):
        px, py, _ = proj_transform(*self.__xyzs, self.axes.get_proj())
        self.set_positions((px[0], py[0]), (px[1], py[1]))
        super().draw(renderer)

    def do_3d_projection(self, _=None):
        px, py, pz = proj_transform(*self.__xyzs, self.axes.get_proj())
        self.set_positions((px[0], py[0]), (px[1], py[1]))
        return np.min(pz)


def add_2d_vector(ax, posA, posB, *args, **kwargs):
    kwargs["mutation_scale"] = kwargs.get("mutation_scale", 7)
    kwargs["arrowstyle"] = kwargs.get("arrowstyle", "-|>")
    arrow = FancyArrowPatch(posA, posB, *args, **kwargs)
    ax.add_artist(arrow)


def add_3d_vector(ax, posA, posB, *args, **kwargs):
    kwargs["mutation_scale"] = kwargs.get("mutation_scale", 7)
    kwargs["arrowstyle"] = kwargs.get("arrowstyle", "-|>")
    arrow = Arrow3D(posA, posB, *args, **kwargs)
    ax.add_artist(arrow)
