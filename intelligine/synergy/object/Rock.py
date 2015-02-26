from xyzworld.SynergyObject import SynergyObject as XyzSynergyObject
from intelligine.cst import IMPENETRABLE


class Rock(XyzSynergyObject):

    def __init__(self, collection, context):
        super().__init__(collection, context)
        context.metas.states.add(self.get_id(), IMPENETRABLE)