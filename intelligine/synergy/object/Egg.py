from intelligine.synergy.object.BaseBug import BaseBug
from synergine.metas import metas
from intelligine.cst import ALIVE, TRANSPORTABLE
from synergine.synergy.Simulation import Simulation


class Egg(BaseBug):

    def __init__(self):
        super().__init__()
        metas.list.add(Simulation.STATE, self.get_id(), TRANSPORTABLE)
        self._life_points = 1
