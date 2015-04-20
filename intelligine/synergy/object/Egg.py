from intelligine.synergy.object.BaseBug import BaseBug
from intelligine.cst import TRANSPORTABLE, TYPE_NURSERY, TYPE


class Egg(BaseBug):

    def __init__(self, collection, context):
        super().__init__(collection, context)
        context.metas.list.add(TYPE, self.get_id(), TYPE_NURSERY)
        # TODO: ?? TRANSPORTABLE ne devrait pas ette du cote de Transportable ?
        context.metas.states.add(self.get_id(), TRANSPORTABLE)
        self._life_points = 1
