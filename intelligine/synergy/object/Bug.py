from intelligine.synergy.object.BaseBug import BaseBug
from synergine.metas import metas
from intelligine.cst import WALKER
from synergine.synergy.Simulation import Simulation


class Bug(BaseBug):

    def __init__(self):
        super().__init__()
        metas.list.add(Simulation.STATE, self.get_id(), WALKER)
