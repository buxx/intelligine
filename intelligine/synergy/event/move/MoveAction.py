from synergine.synergy.event.Action import Action
from intelligine.synergy.event.move.MoveEvent import MoveEvent
from random import randint, choice, randrange
from xyzworld.cst import POSITION, POSITIONS
from intelligine.cst import PREVIOUS_DIRECTION, BLOCKED_SINCE
from intelligine.synergy.event.move.direction import directions_same_level, directions_modifiers, directions_slighty
from intelligine.core.exceptions import NoPheromoneMove


class MoveAction(Action):

    _listen = MoveEvent

    def __init__(self, object_id, parameters):
      super().__init__(object_id, parameters)
      self._move_to_point = None
      self._move_to_direction = None

    def prepare(self, context):
      object_point = context.metas.value.get(POSITION, self._object_id)
      try:
          choosed_direction_name, choosed_direction_point = self._get_pheromone_direction_point(context, object_point)
      except NoPheromoneMove:
          choosed_direction_name, choosed_direction_point = self._get_random_direction_point(context, object_point)
      if self._direction_point_is_possible(context, choosed_direction_point):
        self._move_to_point = choosed_direction_point
        self._move_to_direction = choosed_direction_name

    def _get_random_direction_point(self, context, reference_point):
        z, x, y = reference_point
        direction_name = self._get_random_direction_name(context)
        directions_modifier = directions_modifiers[direction_name]
        new_position = (z + directions_modifier[0], x + directions_modifier[1], y + directions_modifier[2])
        return (direction_name, new_position)

    def _get_random_direction_name(self, context):
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

    def _direction_point_is_possible(self, context, direction_point):
        return context.position_is_penetrable(direction_point)

    def run(self, obj, context, synergy_manager):
        if self._move_to_point is not None:
            obj.set_position(self._move_to_point)
            context.metas.value.set(PREVIOUS_DIRECTION, self._object_id, self._move_to_direction)
            context.metas.value.set(BLOCKED_SINCE, self._object_id, 0)
        else:
            try:
                blocked_since = context.metas.value.get(BLOCKED_SINCE, self._object_id)
            except:
                blocked_since = 0
            context.metas.value.set(BLOCKED_SINCE, self._object_id, blocked_since+1)

    def _get_pheromone_direction_point(self, context, object_point):

        raise NoPheromoneMove()