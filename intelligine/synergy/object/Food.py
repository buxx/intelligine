from intelligine.synergy.object.Transportable import Transportable
from intelligine.cst import TRANSPORTABLE


class Food(Transportable):

    def __init__(self, collection, context):
        super().__init__(collection, context)
        context.metas.states.add(self.get_id(), TRANSPORTABLE)

    def get_what_carry(self):
        clone = self.__class__(self._collection, self._context)
        self._collection.add_object(clone)
        return clone
