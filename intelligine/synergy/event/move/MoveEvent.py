from synergine.synergy.event.Event import Event
from synergine.core.simulation.mechanism.Mechanism import Mechanism
from intelligine.cst import COL_WALKER


class MoveEvent(Event):

    concern = COL_WALKER

    def __init__(self, actions):
        super().__init__(actions)
        self._mechanism = Mechanism

    def _prepare(self, object_id, context, parameters={}):
        return parameters