from intelligine.synergy.object.BaseBug import BaseBug
from intelligine.cst import TRANSPORTABLE


class Egg(BaseBug):

    def __init__(self, collection, context):
        super().__init__(collection, context)
        context.metas.states.add(self.get_id(), TRANSPORTABLE)
        self._life_points = 1
