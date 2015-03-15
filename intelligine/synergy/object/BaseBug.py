from intelligine.synergy.object.Transportable import Transportable
from intelligine.cst import ALIVE, ATTACKABLE, COL_ALIVE


class BaseBug(Transportable):

    def __init__(self, collection, context):
        super().__init__(collection, context)
        context.metas.states.add_list(self.get_id(), [ALIVE, ATTACKABLE])
        context.metas.collections.add(self.get_id(), COL_ALIVE)
        self._life_points = 10
        self._movements_count = -1

    def hurted(self, points):
        self._life_points -= points

    def get_life_points(self):
        return self._life_points

    def set_position(self, point):
        super().set_position(point)
        self._movements_count += 1

    def get_movements_count(self):
        return self._movements_count