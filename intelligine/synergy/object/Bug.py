from intelligine.synergy.object.BaseBug import BaseBug
from intelligine.cst import WALKER, COL_WALKER


class Bug(BaseBug):

    def __init__(self, collection, context):
        super().__init__(collection, context)
        context.metas.states.add(self.get_id(), WALKER)
        context.metas.collections.add(self.get_id(), COL_WALKER)

    def die(self):
        super().die()
        self._remove_state(WALKER)
        self._remove_col(COL_WALKER)
