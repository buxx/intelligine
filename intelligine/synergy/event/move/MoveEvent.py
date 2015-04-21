from intelligine.core.exceptions import UnableToFoundMovement
from intelligine.synergy.event.move.direction import get_position_with_direction_decal
from synergine.core.exceptions import NotConcernedEvent
from intelligine.synergy.event.Event import Event
from synergine.core.simulation.mechanism.Mechanism import Mechanism
from intelligine.cst import COL_WALKER, BRAIN_SCHEMA, BRAIN_PART_MOVE
from xyzworld.cst import POSITION


class MoveEvent(Event):

    PARAM_POSITION = 'pos'
    PARAM_DIRECTION = 'dir'

    concern = COL_WALKER

    def __init__(self, actions):
        super().__init__(actions)
        self._mechanism = Mechanism

    def _prepare(self, object_id, context, parameters={}):
        try:
            direction = self._get_direction(object_id, context)
        except UnableToFoundMovement:
            raise NotConcernedEvent()

        object_point = context.metas.value.get(POSITION, object_id)
        move_to_point = get_position_with_direction_decal(direction, object_point)
        # TODO: future: c le brain qui calcule ou aller, et donc si c possible
        if self._direction_point_is_possible(context, move_to_point):
            parameters[self.PARAM_POSITION] = move_to_point
            parameters[self.PARAM_DIRECTION] = direction
        # TODO: Sinon lever un NotConcernedEvent
        return parameters

    def _get_direction(self, object_id, context):
        object_brain_schema = context.metas.value.get(BRAIN_SCHEMA, object_id)
        object_move_brain_part = object_brain_schema[BRAIN_PART_MOVE]
        return object_move_brain_part.get_direction(context, object_id)

    @staticmethod
    def _direction_point_is_possible(context, direction_point):
        return context.position_is_penetrable(direction_point)
