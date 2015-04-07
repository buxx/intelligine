from synergine.core.exceptions import NotConcernedEvent
from intelligine.synergy.event.src.NearEvent import NearEvent
from xyzworld.mechanism.ArroundMechanism import ArroundMechanism
from intelligine.cst import TRANSPORTABLE, CANT_CARRY_STILL, COL_TRANSPORTER_NOT_CARRYING


class TakeableEvent(NearEvent):

    concern = COL_TRANSPORTER_NOT_CARRYING
    _near_name = 'objects_ids_transportable'
    _near_map = lambda self, near_object_id, context: context.metas.states.have(near_object_id, TRANSPORTABLE)

    def __init__(self, actions):
        super().__init__(actions)
        self._mechanism = ArroundMechanism

    def _prepare(self, object_id, context, parameters={}):
        if context.metas.value.get(CANT_CARRY_STILL, object_id, allow_empty=True):
            raise NotConcernedEvent()
        self.map(context, parameters, stop_at_first=True)
        if self._near_name not in parameters:
            raise NotConcernedEvent()
        return parameters