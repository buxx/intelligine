from synergine.synergy.event.Event import Event
from intelligine.cst import CANT_CARRY_STILL, TRANSPORTER, ALIVE
from intelligine.synergy.Simulation import Simulation


class CycleEvent(Event):

    def concern(self, object_id, context):
        return context.metas.list.have(Simulation.STATE, object_id, TRANSPORTER) and \
               context.metas.list.have(Simulation.STATE, object_id, ALIVE)

    def _object_match(self, object_id, context, parameters):
        return True