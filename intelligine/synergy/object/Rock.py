from xyzworld.SynergyObject import SynergyObject as XyzSynergyObject
from synergine.metas import metas
from intelligine.cst import IMPENETRABLE


class Rock(XyzSynergyObject):

    def __init__(self):
        super().__init__()
        metas.states.add(self.get_id(), IMPENETRABLE)