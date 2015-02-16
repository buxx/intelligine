from synergine.synergy.event.Event import Event
from intelligine.cst import CANT_CARRY_STILL, TRANSPORTER, ALIVE


class CycleEvent(Event):

    def concern(self, object_id, context):
        return context.metas.states.have_list(object_id, [TRANSPORTER, ALIVE])

    def _object_match(self, object_id, context, parameters):
        return True