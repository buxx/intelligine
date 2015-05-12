from synergine.synergy.event.Event import Event
from intelligine.cst import COL_TRANSPORTER


class CycleEvent(Event):

    _concern = COL_TRANSPORTER

    def _prepare(self, object_id, context, parameters):
        return parameters