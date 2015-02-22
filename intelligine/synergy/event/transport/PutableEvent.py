from intelligine.synergy.event.transport.TakeableEvent import TakeableEvent
from xyzworld.mechanism.ArroundMechanism import ArroundMechanism
from intelligine.cst import CANT_PUT_STILL, COL_TRANSPORTER_CARRYING


class PutableEvent(TakeableEvent):

    concern = COL_TRANSPORTER_CARRYING

    def _object_match(self, object_id, context, parameters={}):
        if context.metas.value.get(CANT_PUT_STILL, object_id, allow_empty=True):
            return False
        return super()._object_match(object_id, context, parameters)