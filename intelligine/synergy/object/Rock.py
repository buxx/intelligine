from xyzworld.SynergyObject import SynergyObject as XyzSynergyObject
from synergine.metas import metas
from intelligine.cst import IMPENETRABLE
from synergine.synergy.Simulation import Simulation


class Rock(XyzSynergyObject):

    def __init__(self):
        super().__init__()
        metas.list.add(Simulation.STATE, self.get_id(), IMPENETRABLE)