from antstar.StickWallAntBrain import StickWallAntBrain
from intelligine.cst import EXPLORATION_VECTOR, MOVE_BYBASS, MOVE_BYBASS_DISTANCE, MOVE_BYBASS_MEMORY, MOVE_BYBASS_WALL,\
    MOVE_BYBASS_PREV_WALL


class ByPass(StickWallAntBrain):

    def __init__(self, host, home_vector, context, object_id):
        """

        Note: We broke Liskov principle here.

        :param host:
        :param home_vector:
        :param context:
        :param object_id:
        :return:
        """
        super().__init__(host, home_vector)
        self._context = context
        self._object_id = object_id
        self._memory_since_blocked = context.metas.value.get(MOVE_BYBASS_MEMORY,
                                                             object_id,
                                                             allow_empty=True,
                                                             empty_value=[])
        self._by_passing = context.metas.value.get(MOVE_BYBASS,
                                                   object_id,
                                                   allow_empty=True,
                                                   empty_value=False)
        self._distance_when_blocked = context.metas.value.get(MOVE_BYBASS_DISTANCE,
                                                              object_id,
                                                              allow_empty=True,
                                                              empty_value=None)
        self._current_wall_position = context.metas.value.get(MOVE_BYBASS_WALL,
                                                              object_id,
                                                              allow_empty=True,
                                                              empty_value=None)
        self._previous_wall_position = context.metas.value.get(MOVE_BYBASS_PREV_WALL,
                                                               object_id,
                                                               allow_empty=True,
                                                               empty_value=None)

    def _set_home_vector(self, home_vector):
        super()._set_home_vector(home_vector)
        self._context.metas.value.set(EXPLORATION_VECTOR, self._object_id, home_vector)

    def _set_memory_since_blocked(self, memory_since_blocked):
        super()._set_memory_since_blocked(memory_since_blocked)
        self._context.metas.value.set(MOVE_BYBASS_MEMORY, self._object_id, memory_since_blocked)

    def _set_by_passing(self, by_passing):
        super()._set_by_passing(by_passing)
        self._context.metas.value.set(MOVE_BYBASS, self._object_id, by_passing)

    def _set_distance_when_blocked(self, distance):
        super()._set_distance_when_blocked(distance)
        self._context.metas.value.set(MOVE_BYBASS_DISTANCE, self._object_id, distance)

    def _set_current_wall_position(self, position):
        super()._set_current_wall_position(position)
        self._context.metas.value.set(MOVE_BYBASS_WALL, self._object_id, position)

    def _set_previous_wall_position(self, position):
        super()._set_previous_wall_position(position)
        self._context.metas.value.set(MOVE_BYBASS_PREV_WALL, self._object_id, position)
