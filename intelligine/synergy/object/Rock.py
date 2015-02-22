from xyzworld.SynergyObject import SynergyObject as XyzSynergyObject
from intelligine.cst import IMPENETRABLE


class Rock(XyzSynergyObject):

    def __init__(self, context):
        super().__init__(context)
        context.metas.states.add(self.get_id(), IMPENETRABLE)