from xyzworld.SynergyObject import SynergyObject as XyzSynergyObject
from synergine.metas import metas
from intelligine.cst import ALIVE, ATTACKABLE, ATTACKER
from synergine.synergy.Simulation import Simulation


class Bug(XyzSynergyObject):

    def __init__(self):
        super().__init__()
        metas.list.add(Simulation.STATE, self.get_id(), ALIVE)
        metas.list.add(Simulation.STATE, self.get_id(), ATTACKER)
        metas.list.add(Simulation.STATE, self.get_id(), ATTACKABLE)
        self._life_points = 10

    def hurted(self, points):
        self._life_points -= points

    def get_life_points(self):
        return self._life_points