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


class Vector2D(FancyArrowPatch):
    def __init__(self, posA, posB, *args, **kwargs):
        kwargs = {"linewidth": 0.6, "mutation_scale": 7, "arrowstyle": "-|>"} | kwargs
        super().__init__(posA, posB, *args, **kwargs)


class Vector3D(Arrow3D):
    def __init__(self, posA, posB, *args, **kwargs):
        kwargs = {"linewidth": 0.6, "mutation_scale": 7, "arrowstyle": "-|>"} | kwargs
        super().__init__(posA, posB, *args, **kwargs)
