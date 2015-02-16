from intelligine.synergy.object.BaseBug import BaseBug
from synergine.metas import metas
from intelligine.cst import WALKER


class Bug(BaseBug):

    def __init__(self):
        super().__init__()
        metas.states.add(self.get_id(), WALKER)
