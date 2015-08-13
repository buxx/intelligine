from intelligine.simulation.object.brain.part.move.AntStar.HostFeeler import HostFeeler
from intelligine.synergy.event.move.direction import get_position_with_direction_decal
from synergine_xyz.cst import POSITION


class Host:

    def __init__(self, context, object_id):
        self._context = context
        self._object_id = object_id
        self._feeler = HostFeeler(context, object_id)
        self._moved_to_direction = None
        self._position_3d = self._context.metas.value.get(POSITION, self._object_id)

    def get_position(self):
        return self._position_3d[1], self._position_3d[2]

    def get_feeler(self):
        return self._feeler

    def move_to(self, direction):
        self._moved_to_direction = direction
        self._position_3d = get_position_with_direction_decal(direction, self._position_3d)

    def get_moved_to_direction(self):
        return self._moved_to_direction
