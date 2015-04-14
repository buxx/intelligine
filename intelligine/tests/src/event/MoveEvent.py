from intelligine.synergy.event.move.MoveEvent import MoveEvent as BaseMoveEvent
from intelligine.synergy.event.move.direction import NORTH


class MoveEvent(BaseMoveEvent):

    force_direction = lambda self, object_id, context: NORTH

    def _get_direction(self, object_id, context):
        return self.force_direction(object_id, context)
