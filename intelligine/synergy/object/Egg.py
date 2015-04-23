from intelligine.synergy.object.BaseBug import BaseBug
from intelligine.cst import TRANSPORTABLE, TYPE_NURSERY, TYPE


class Egg(BaseBug):

    def __init__(self, collection, context):
        super().__init__(collection, context)
        context.metas.list.add(TYPE, self.get_id(), TYPE_NURSERY)
        self._life_points = 1
