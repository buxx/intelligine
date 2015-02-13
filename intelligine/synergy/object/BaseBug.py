from xyzworld.SynergyObject import SynergyObject as XyzSynergyObject
from synergine.metas import metas
from intelligine.cst import ALIVE, ATTACKABLE, TRANSPORTABLE
from synergine.synergy.Simulation import Simulation


class BaseBug(XyzSynergyObject):

    def __init__(self):
        super().__init__()
        metas.list.add(Simulation.STATE, self.get_id(), ALIVE)
        metas.list.add(Simulation.STATE, self.get_id(), ATTACKABLE)
        self._life_points = 10
        self._carried_by = []

    def hurted(self, points):
        self._life_points -= points

    def get_life_points(self):
        return self._life_points

    def set_carried_by(self, obj):
        self._carried_by.append(obj)
        metas.list.remove(Simulation.STATE, self.get_id(), TRANSPORTABLE)

    def is_carried(self):
        if self._carried_by:
            return True
        return False