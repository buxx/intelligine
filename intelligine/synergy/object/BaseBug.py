from xyzworld.SynergyObject import SynergyObject as XyzSynergyObject
from intelligine.cst import ALIVE, ATTACKABLE, TRANSPORTABLE, COL_ALIVE


class BaseBug(XyzSynergyObject):

    def __init__(self, context):
        super().__init__(context)
        context.metas.states.add_list(self.get_id(), [ALIVE, ATTACKABLE])
        context.metas.collections.add(self.get_id(), COL_ALIVE)
        self._life_points = 10
        self._carried_by = None

    def hurted(self, points):
        self._life_points -= points

    def get_life_points(self):
        return self._life_points

    def set_carried_by(self, obj):
        if obj is not None:
            assert self._carried_by is None
            self._carried_by = obj
            self._context.metas.states.remove(self.get_id(), TRANSPORTABLE)
        else:
            assert self._carried_by is not None
            self._carried_by = None
            self._context.metas.states.add(self.get_id(), TRANSPORTABLE)

    def is_carried(self):
        if self._carried_by:
            return True
        return False