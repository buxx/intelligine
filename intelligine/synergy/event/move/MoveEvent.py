from synergine.synergy.event.Event import Event
from synergine.core.simulation.mechanism.Mechanism import Mechanism
from intelligine.synergy.Simulation import Simulation
from intelligine.cst import ALIVE


class MoveEvent(Event):

    def concern(self, object_id, context):
        return context.metas.list.have(Simulation.STATE, object_id, ALIVE)

    def __init__(self, actions):
        super().__init__(actions)
        self._mechanism = Mechanism

    def _object_match(self, object_id, context, parameters={}):
      return True