from intelligine.synergy.object.BaseBug import BaseBug
from synergine.metas import metas
from intelligine.cst import ALIVE, TRANSPORTABLE


class Egg(BaseBug):

    def __init__(self):
        super().__init__()
        metas.states.add(self.get_id(), TRANSPORTABLE)
        self._life_points = 1
