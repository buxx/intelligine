from synergine.synergy.event.Event import Event
from intelligine.cst import COL_ALIVE # TODO: Crer une col TRANPORTER ?


class CycleEvent(Event):

    concern = COL_ALIVE

    def _object_match(self, object_id, context, parameters):
        return True