from xyzworld.SynergyObject import SynergyObject as XyzSynergyObject
from intelligine.cst import TRANSPORTABLE


class Transportable(XyzSynergyObject):

    def __init__(self, collection, context):
        super().__init__(collection, context)
        self._carried_by = None

    def set_carried_by(self, obj):
        if obj is not None:
            assert self._carried_by is None
            self._carried_by = obj
            self._context.metas.states.remove(self.get_id(), TRANSPORTABLE)
        else:
            assert self._carried_by is not None
            self._carried_by = None
            self._context.metas.states.add(self.get_id(), TRANSPORTABLE)

    def is_carried(self):
        if self._carried_by:
            return True
        return False

    def get_what_carry(self):
        return self

    def is_takable(self):
        return not self.is_carried()