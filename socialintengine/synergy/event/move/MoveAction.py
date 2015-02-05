from synergine.synergy.event.Action import Action
from socialintengine.synergy.event.move.MoveEvent import MoveEvent
from random import randint
from xyzworld.cst import POSITION, POSITIONS
from socialintengine.cst import IMPENETRABLE
from synergine.synergy.Simulation import Simulation


class MoveAction(Action):

    _listen = MoveEvent

    def __init__(self, object_id, parameters):
      super().__init__(object_id, parameters)
      self._move_to = None

    def prepare(self, context):
      object_point = context.metas.value.get(POSITION, self._object_id)
      choosed_direction_point = self._get_random_direction_point(object_point)
      if self._direction_point_is_possible(context, choosed_direction_point):
        self._move_to = choosed_direction_point

    def _get_random_direction_point(self, reference_point):
        z, x, y = reference_point
        new_z = z
        new_x = x + randint(-1, 1)
        new_y = y + randint(-1, 1)
        return (new_z, new_x, new_y)

    def _direction_point_is_possible(self, context, direction_point):
        objects_ids_on_this_point = context.metas.list.get(POSITIONS, direction_point, allow_empty=True)
        for object_id_on_this_point in objects_ids_on_this_point:
          if context.metas.list.have(Simulation.STATE, object_id_on_this_point, IMPENETRABLE):
            return False
        return True

    def run(self, obj, collection, context):
        if self._move_to is not None:
            obj.add_trace(self._move_to)