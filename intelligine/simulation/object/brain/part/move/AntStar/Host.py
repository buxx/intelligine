from intelligine.simulation.object.brain.part.move.AntStar.HostFeeler import HostFeeler
from synergine_xyz.cst import POSITION


class Host:

    def __init__(self, context, object_id):
        self._context = context
        self._object_id = object_id
        self._feeler = HostFeeler(context, object_id)
        self._moved_to_direction = None

    def get_position(self):
        current_position = self._context.metas.value.get(POSITION, self._object_id)
        return current_position[1], current_position[2]

    def get_feeler(self):
        return self._feeler

    def move_to(self, direction):
        self._moved_to_direction = direction

    def get_moved_to_direction(self):
        return self._moved_to_direction
