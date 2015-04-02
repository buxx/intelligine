from intelligine.synergy.event.move.MoveAction import MoveAction as BaseMoveAction
from intelligine.synergy.event.move.direction import NORTH


class MoveAction(BaseMoveAction):

    force_direction = lambda self, context, object_id: NORTH

    def _get_prepared_direction(self, context):
        return self.force_direction(context, self._object_id)
