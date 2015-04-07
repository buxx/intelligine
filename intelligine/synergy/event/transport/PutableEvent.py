from synergine.core.exceptions import NotConcernedEvent
from intelligine.synergy.event.transport.TakeableEvent import TakeableEvent
from intelligine.cst import CANT_PUT_STILL, COL_TRANSPORTER_CARRYING


class PutableEvent(TakeableEvent):

    concern = COL_TRANSPORTER_CARRYING

    def _prepare(self, object_id, context, parameters={}):
        if context.metas.value.get(CANT_PUT_STILL, object_id, allow_empty=True):
            raise NotConcernedEvent()
        return super()._prepare(object_id, context, parameters)