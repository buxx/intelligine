from xyzworld.SynergyObject import SynergyObject as XyzSynergyObject
from synergine.metas import metas
from intelligine.cst import ALIVE, ATTACKABLE, TRANSPORTABLE


class BaseBug(XyzSynergyObject):

    def __init__(self):
        super().__init__()
        metas.states.add_list(self.get_id(), [ALIVE, ATTACKABLE])
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
            metas.states.remove(self.get_id(), TRANSPORTABLE)
        else:
            assert self._carried_by is not None
            self._carried_by = None
            metas.states.add(self.get_id(), TRANSPORTABLE)

    def is_carried(self):
        if self._carried_by:
            return True
        return False