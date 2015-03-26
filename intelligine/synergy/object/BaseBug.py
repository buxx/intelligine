from intelligine.synergy.object.Transportable import Transportable
from intelligine.cst import ALIVE, ATTACKABLE, COL_ALIVE
from intelligine.simulation.object.brain.Brain import Brain


class BaseBug(Transportable):

    def __init__(self, collection, context):
        super().__init__(collection, context)
        context.metas.states.add_list(self.get_id(), [ALIVE, ATTACKABLE])
        context.metas.collections.add(self.get_id(), COL_ALIVE)
        self._life_points = 10
        self._movements_count = -1
        self._brain = self._get_brain_instance()

    def hurted(self, points):
        self._life_points -= points

    def get_life_points(self):
        return self._life_points

    def set_position(self, point):
        super().set_position(point)
        self._movements_count += 1

    def get_movements_count(self):
        return self._movements_count

    def _get_brain_instance(self):
        return Brain(self._context, self)

    def get_brain(self):
        return self._brain