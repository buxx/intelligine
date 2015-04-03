from synergine.synergy.event.Action import Action
from intelligine.synergy.event.move.MoveEvent import MoveEvent
from synergine.synergy.event.exception.ActionAborted import ActionAborted
from xyzworld.cst import POSITION
from intelligine.cst import BLOCKED_SINCE, BRAIN_PART_MOVE, BRAIN_SCHEMA
from intelligine.synergy.event.move.direction import get_position_with_direction_decal


class MoveAction(Action):

    _listen = MoveEvent

    def __init__(self, object_id, parameters):
        super().__init__(object_id, parameters)
        self._move_to_point = None
        self._move_to_direction = None

    def prepare(self, context):
        object_point = context.metas.value.get(POSITION, self._object_id)
        direction = self._get_prepared_direction(context)
        self._set_prepared_direction(context, object_point, direction)

    def _get_prepared_direction(self, context):
        object_brain_schema = context.metas.value.get(BRAIN_SCHEMA, self._object_id)
        object_move_brain_part = object_brain_schema[BRAIN_PART_MOVE]
        return object_move_brain_part.get_direction(context, self._object_id)

    def _set_prepared_direction(self, context, object_point, direction):
        move_to_point = get_position_with_direction_decal(direction, object_point)
        if self._direction_point_is_possible(context, move_to_point):
            self._move_to_point = move_to_point
            self._move_to_direction = direction
        else:
            # TODO: mettre self._dont_move = True ?
            pass

    @staticmethod
    def _direction_point_is_possible(context, direction_point):
        return context.position_is_penetrable(direction_point)

    def run(self, obj, context, synergy_manager):
        try:
            self._apply_move(obj, context)
        except ActionAborted:
            blocked_since = context.metas.value.get(BLOCKED_SINCE, self._object_id, allow_empty=True, empty_value=0)
            context.metas.value.set(BLOCKED_SINCE, self._object_id, blocked_since+1)

    def _apply_move(self, obj, context):
        # TODO: il ne faut pas choisir une direction 14.
        if self._move_to_point is None or self._move_to_direction == 14:
            raise ActionAborted()

        obj.set_position(self._move_to_point)
        obj.get_brain().get_part(BRAIN_PART_MOVE).done(obj, context)
