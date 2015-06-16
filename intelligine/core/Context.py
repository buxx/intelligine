from synergine_xyz.Context import Context as XyzContext
from intelligine.cst import IMPENETRABLE
from synergine_xyz.cst import POSITIONS
from intelligine.synergy.stigmergy.PheromonesManager import PheromonesManager


class Context(XyzContext):

    def __init__(self):
        super().__init__()
        self._pheromones = PheromonesManager(self)

    def pheromones(self):
        return self._pheromones

    def position_is_penetrable(self, position):
        """

        Return True if position is empty or occuped by non physical impenetrable object.

        :param position:
        :return:
        """
        objects_ids_on_this_point = self.metas.list.get(POSITIONS, position, allow_empty=True)
        for object_id_on_this_point in objects_ids_on_this_point:
          if self.metas.states.have(object_id_on_this_point, IMPENETRABLE):
            return False
        return True

    def position_can_be_odorus(self, position):
        """

        Return True if position can smell

        :param position:
        :return:
        """
        return self.position_is_penetrable(position)
