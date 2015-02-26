from synergine.synergy.event.Event import Event
from intelligine.cst import COL_TRANSPORTER


class CycleEvent(Event):

    concern = COL_TRANSPORTER

    def _object_match(self, object_id, context, parameters):
        return True