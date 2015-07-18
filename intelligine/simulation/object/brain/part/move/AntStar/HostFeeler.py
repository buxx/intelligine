from intelligine.synergy.event.move.direction import get_position_with_direction_decal
from synergine_xyz.cst import POSITION
from synergine_xyz.geometry import distance_from_points


class HostFeeler:

    def __init__(self, context, object_id):
        self._context = context
        self._object_id = object_id
        self._current_position = context.metas.value.get(POSITION, self._object_id)

    def direction_is_free(self, direction_of_home):
        position_will_be = get_position_with_direction_decal(direction_of_home, self._current_position)
        return self._context.position_is_penetrable(position_will_be)

    def position_is_free(self, position):
        threed_position = (0, position[0], position[1])
        points_distance = distance_from_points(threed_position, self._current_position)
        if points_distance > 1:
            raise Exception("Can't feel so far (%s to %s: %s)" % (str(self._current_position),
                                                                  str(position),
                                                                  str(points_distance)))
        return self._context.position_is_penetrable(threed_position)
