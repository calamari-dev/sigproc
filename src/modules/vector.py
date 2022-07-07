from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d.proj3d import proj_transform


class FancyArrowPatch3D(FancyArrowPatch):
    def __init__(self, posA, posB, *args, **kwargs):
        super().__init__((0, 0), (0, 0), *args, **kwargs)
        self.__xyzs = tuple(zip(posA, posB))

    def do_3d_projection(self, _=None):
        px, py, pz = proj_transform(*self.__xyzs, self.axes.get_proj())
        self.set_positions(*zip(px, py))
        return min(pz)

    def draw(self, renderer):
        px, py, _ = proj_transform(*self.__xyzs, self.axes.get_proj())
        self.set_positions(*zip(px, py))
        super().draw(renderer)


class Vector2D(FancyArrowPatch):
    def __init__(self, posA, posB, *args, **kwargs):
        kwargs = {"linewidth": 0.6, "mutation_scale": 7, "arrowstyle": "-|>"} | kwargs
        super().__init__(posA, posB, *args, **kwargs)


class Vector3D(FancyArrowPatch3D):
    def __init__(self, posA, posB, *args, **kwargs):
        kwargs = {"linewidth": 0.6, "mutation_scale": 7, "arrowstyle": "-|>"} | kwargs
        super().__init__(posA, posB, *args, **kwargs)
