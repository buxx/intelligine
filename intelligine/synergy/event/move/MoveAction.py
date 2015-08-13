from synergine.synergy.event.Action import Action
from intelligine.synergy.event.move.MoveEvent import MoveEvent
from synergine.synergy.event.exception.ActionAborted import ActionAborted
from intelligine.cst import BRAIN_PART_MOVE
from synergine_xyz.cst import BLOCKED_SINCE


class MoveAction(Action):

    _listen = MoveEvent

    def __init__(self, object_id, parameters):
        super().__init__(object_id, parameters)
        self._move_to_point = None
        self._move_to_direction = None

    def run(self, obj, context, synergy_manager):
        try:
            self._apply_move(obj, context)
        except ActionAborted:
            # TODO: Dans l'obj ces lignes
            blocked_since = context.metas.value.get(BLOCKED_SINCE, self._object_id, allow_empty=True, empty_value=0)
            context.metas.value.set(BLOCKED_SINCE, obj.get_id(), blocked_since+1)

    def _apply_move(self, obj, context):
        # TODO: il ne faut pas choisir une direction 14.
        if MoveEvent.PARAM_DIRECTION not in self._parameters or self._parameters[MoveEvent.PARAM_DIRECTION] == 14:
            raise ActionAborted()

        obj.set_position(self._parameters[MoveEvent.PARAM_POSITION])
        obj.set_previous_direction(self._parameters[MoveEvent.PARAM_DIRECTION])
        obj.get_brain().get_part(BRAIN_PART_MOVE).done()
