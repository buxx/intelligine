from synergine.synergy.event.Event import Event
from synergine.core.simulation.mechanism.Mechanism import Mechanism
from intelligine.cst import ALIVE, WALKER


class MoveEvent(Event):

    def concern(self, object_id, context):
        return context.metas.states.have(object_id, [ALIVE, WALKER])

    def __init__(self, actions):
        super().__init__(actions)
        self._mechanism = Mechanism

    def _object_match(self, object_id, context, parameters={}):
      return True