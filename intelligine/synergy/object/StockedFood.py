from intelligine.cst import TYPE, TYPE_RESOURCE_EXPLOITABLE, COL_EATABLE
from intelligine.synergy.object.Food import Food


class StockedFood(Food):

    def __init__(self, collection, context):
        super().__init__(collection, context)
        context.metas.list.remove(TYPE, self.get_id(), TYPE_RESOURCE_EXPLOITABLE)
        self._add_col(COL_EATABLE)
