from intelligine.synergy.event.move.MoveAction import MoveAction as BaseMoveAction
from intelligine.synergy.event.move.direction import NORTH


class MoveAction(BaseMoveAction):

    force_direction = lambda self, context, object_point: NORTH

    def _get_direction_with_pheromones(self, context, object_point):
        return self.force_direction(context, object_point)

    # def _get_random_direction(self, context):
    #     return self.force_direction