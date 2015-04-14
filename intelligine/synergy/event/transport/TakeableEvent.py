from intelligine.core.exceptions import NearNothingFound
from synergine.core.exceptions import NotConcernedEvent
from intelligine.synergy.event.src.NearEvent import NearEvent
from xyzworld.mechanism.ArroundMechanism import ArroundMechanism
from intelligine.cst import TRANSPORTABLE, CANT_CARRY_STILL, COL_TRANSPORTER_NOT_CARRYING, BRAIN_SCHEMA, BRAIN_PART_TAKE


class TakeableEvent(NearEvent):

    PARAM_TAKE = 'take'
    concern = COL_TRANSPORTER_NOT_CARRYING
    _near_name = 'objects_ids_transportable'
    _near_map = lambda self, near_object_id, context: context.metas.states.have(near_object_id, TRANSPORTABLE)

    def __init__(self, actions):
        super().__init__(actions)
        self._mechanism = ArroundMechanism

    def _prepare(self, object_id, context, parameters={}):
        if not self._can_carry(object_id, context):
            raise NotConcernedEvent()

        try:
            self.map(context, parameters, stop_at_first=True)
        except NearNothingFound:
            raise NotConcernedEvent()

        if not self._object_can_take(object_id, context, parameters[self._near_name][0]):
            raise NotConcernedEvent()

        parameters[self.PARAM_TAKE] = parameters[self._near_name][0]
        return parameters

    @staticmethod
    def _can_carry(object_id, context):
        return not context.metas.value.get(CANT_CARRY_STILL, object_id, allow_empty=True)

    @staticmethod
    def _object_can_take(object_id, context, object_to_take_id):
        object_brain_schema = context.metas.value.get(BRAIN_SCHEMA, object_id)
        object_take_brain_part = object_brain_schema[BRAIN_PART_TAKE]
        return object_take_brain_part.can_take(context, object_id, object_to_take_id)