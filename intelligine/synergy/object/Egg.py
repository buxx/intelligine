from intelligine.synergy.object.BaseBug import BaseBug
from intelligine.cst import TYPE_NURSERY, TYPE, SMELL_EGG, COL_SMELL


class Egg(BaseBug):

    def __init__(self, collection, context):
        super().__init__(collection, context)
        context.metas.list.add(TYPE, self.get_id(), TYPE_NURSERY)
        self._life_points = 1
        self._add_col(COL_SMELL)
        self._set_smell(SMELL_EGG)
