from intelligine.core.exceptions import NearNothingFound, CantFindWhereToPut
from intelligine.shorcut.brain import get_brain_part
from intelligine.synergy.event.src.NearEvent import NearEvent
from synergine.core.exceptions import NotConcernedEvent
from intelligine.cst import CANT_PUT_STILL, COL_TRANSPORTER_CARRYING, TRANSPORTABLE, BRAIN_SCHEMA, BRAIN_PART_PUT
from synergine_xyz.mechanism.AroundMechanism import AroundMechanism


class PutableEvent(NearEvent):
    """
    TODO: Refactorise with TakableEvent
    """

    PARAM_PUT = 'put'
    PARAM_PUT_TO = 'put_to'
    _mechanism = AroundMechanism
    _concern = COL_TRANSPORTER_CARRYING
    _near_name = 'objects_ids_putable'
    _near_map = lambda self, near_object_id, context: context.metas.states.have(near_object_id, TRANSPORTABLE)

    def _prepare(self, object_id, context, parameters={}):
        if not self._can_put(object_id, context):
            raise NotConcernedEvent()

        try:
            self.map(context, parameters, stop_at_first=True)
        except NearNothingFound:
            raise NotConcernedEvent()

        object_near_id = parameters[self._near_name][0]
        brain_part = get_brain_part(context, object_id, BRAIN_PART_PUT)

        if not brain_part.can_put(context, object_id, object_near_id):
            raise NotConcernedEvent()

        try:
            put_position = brain_part.get_put_position(context, object_id, object_near_id)
        except CantFindWhereToPut:
            raise NotConcernedEvent()

        parameters[self.PARAM_PUT] = parameters[self._near_name][0]
        parameters[self.PARAM_PUT_TO] = put_position
        return parameters

    @staticmethod
    def _can_put(object_id, context):
        return not context.metas.value.get(CANT_PUT_STILL, object_id, allow_empty=True)

    @classmethod
    def _object_can_put(cls, object_id, context, object_to_put_id):
        object_take_brain_part = get_brain_part(context, object_id, BRAIN_PART_PUT)
        return object_take_brain_part.can_put(context, object_id, object_to_put_id)
