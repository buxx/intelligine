from intelligine.cst import TRANSPORTABLE, CARRIED_BY, CARRY
from intelligine.synergy.object.SynergyObject import SynergyObject


class Transportable(SynergyObject):

    def __init__(self, collection, context):
        super().__init__(collection, context)
        self._carried_by = None
        context.metas.states.add(self.get_id(), TRANSPORTABLE)
        self._is_carried = False

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

    def set_is_carried(self, is_carried, by_obj):
        self._is_carried = bool(is_carried)
        if self._is_carried:
            self._context.metas.value.set(CARRIED_BY, self.get_id(), by_obj.get_id())
        else:
            self._context.metas.value.unset(CARRIED_BY, self.get_id())
