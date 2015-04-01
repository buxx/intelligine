from synergine.synergy.event.Action import Action
from intelligine.synergy.event.move.MoveEvent import MoveEvent
from random import randint, choice, randrange
from synergine.synergy.event.exception.ActionAborted import ActionAborted
from xyzworld.cst import POSITION
from intelligine.cst import PREVIOUS_DIRECTION, BLOCKED_SINCE
from intelligine.synergy.event.move.direction import directions_same_level, directions_slighty
from intelligine.synergy.event.move.direction import get_position_with_direction_decal


class MoveAction(Action):

    _listen = MoveEvent

    def __init__(self, object_id, parameters):
        super().__init__(object_id, parameters)
        self._move_to_point = None
        self._move_to_direction = None

    def prepare(self, context):
        object_point = context.metas.value.get(POSITION, self._object_id)
        direction = self._get_prepared_direction(context, object_point)
        self._set_prepared_direction(context, object_point, direction)

    def _get_prepared_direction(self, context, object_point):
        return self._get_random_direction(context)

    def _set_prepared_direction(self, context, object_point, direction):
        move_to_point = get_position_with_direction_decal(direction, object_point)
        if self._direction_point_is_possible(context, move_to_point):
            self._move_to_point = move_to_point
            self._move_to_direction = direction
        else:
            # TODO: mettre self._dont_move = True ?
            pass

    def _get_random_direction(self, context):
        try:
            blocked_since = context.metas.value.get(BLOCKED_SINCE, self._object_id)
        except KeyError:
            blocked_since = 0
        direction_name = None
        if blocked_since <= 3:  #TODO: config
            try:
                previous_direction = context.metas.value.get(PREVIOUS_DIRECTION, self._object_id)
                # TODO: Faut mettre ca en plus propre (proba d'aller tou droit, config, etc)
                if randrange(100) < 75:  # 75% de change d'aller tout droit
                    # Dans le futur: les fourmis vont moins tout droit quand elle se croient et se touche
                    return previous_direction

                directions_list = directions_slighty[previous_direction]
                # TODO: TMP tant que 1 niveau (z)
                directions_list = [direction for direction in directions_list if direction > 9 and direction < 19]
                direction_name = choice(directions_list)
            except KeyError:
                pass

        if not direction_name:
            direction_name = randint(directions_same_level[0], directions_same_level[1])

        return direction_name

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
        context.metas.value.set(PREVIOUS_DIRECTION, self._object_id, self._move_to_direction)
        context.metas.value.set(BLOCKED_SINCE, self._object_id, 0)