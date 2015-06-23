from intelligine.simulation.object.brain.part.move.MoveBrainPart import MoveBrainPart
from intelligine.synergy.event.move.direction import directions_modifiers, get_direction_for_degrees
from synergine_xyz.cst import POSITION
from intelligine.core.exceptions import NoPheromone
from intelligine.cst import PHEROMONE_SEARCHING, MOVE_MODE_EXPLO, \
    MOVE_MODE_HOME, MOVE_MODE, MOVE_MODE_GOHOME, EXPLORATION_VECTOR, POINTS_SMELL
from intelligine.simulation.pheromone.DirectionPheromone import DirectionPheromone
from synergine_xyz.geometry import get_degree_from_north


class AntMoveBrainPart(MoveBrainPart):

    def __init__(self, host_brain):
        super().__init__(host_brain)
        self._exploration_vector = (0, 0)

    def _set_exploration_vector(self, new_vector):
        self._exploration_vector = new_vector
        # TODO: On devrais donner le context aux brain parts
        self._host_brain.get_context().metas.value.set(EXPLORATION_VECTOR,
                                                       self._host_brain.get_host().get_id(),
                                                       new_vector)

    @classmethod
    def get_direction(cls, context, object_id):
        move_mode = context.metas.value.get(MOVE_MODE, object_id)
        if move_mode == MOVE_MODE_EXPLO:
            try:
                return cls._get_direction_with_pheromones(context, object_id)
            except NoPheromone:
                return super().get_direction(context, object_id)
        elif move_mode == MOVE_MODE_GOHOME:
            return cls._get_direction_with_exploration_vector(context, object_id)

        return super().get_direction(context, object_id)

    @classmethod
    def _get_direction_with_pheromones(cls, context, object_id):
        object_point = context.metas.value.get(POSITION, object_id)
        pheromone_type = context.metas.value.get(PHEROMONE_SEARCHING, object_id)
        try:
            direction = cls._get_pheromone_direction_for_point(context, object_point, pheromone_type)
        except NoPheromone:
            try:
                direction = cls._get_direction_of_pheromone(context, object_point, pheromone_type)
            except NoPheromone:
                raise
        return direction

    @staticmethod
    def _get_pheromone_direction_for_point(context, point, pheromone_type):
        return DirectionPheromone.get_direction_for_point(context, point, pheromone_type)

    @staticmethod
    def _get_direction_of_pheromone(context, point, pheromone_type):
        search_pheromone_in_points = context.get_around_points_of_point(point)
        try:
            best_pheromone_direction = DirectionPheromone.get_best_pheromone_direction_in(context,
                                                                                          point,
                                                                                          search_pheromone_in_points,
                                                                                          pheromone_type)
            return best_pheromone_direction
        except NoPheromone as err:
            raise err

    @staticmethod
    def _get_direction_with_exploration_vector(context, object_id):
        current_position = context.metas.value.get(POSITION, object_id)
        exploration_vector = context.metas.value.get(EXPLORATION_VECTOR, object_id)
        # TODO: inverser
        home_vector = (exploration_vector[0] - (exploration_vector[0]*2),
                       exploration_vector[1] - (exploration_vector[1]*2))
        home_position = (0, current_position[1]+home_vector[0], current_position[2]+home_vector[1])
        degree_from_north = get_degree_from_north(current_position, home_position)
        direction_for_home_vector = get_direction_for_degrees(degree_from_north)

        return direction_for_home_vector

    # TODO: obj pas necessaire, il est dans _host
    def done(self, obj, context):
        super().done(obj, context)
        self._appose_pheromone(obj)
        self._check_context(obj, context)
        self._apply_context(obj, context)

    @staticmethod
    def _appose_pheromone(obj):
        if obj.get_movement_pheromone_gland().is_enabled():
            obj.get_movement_pheromone_gland().appose()

    def _check_context(self, obj, context):
        """

        If was in exploration, and just found home smell;
            -> home mode (then, in this mode: no update vector, put food if food, etc)
        If was in home, and just loose home smell:
            -> exploration mode

        :param obj:
        :param context:
        :return:
        """
        if self._host_brain.get_movement_mode() == MOVE_MODE_EXPLO and self._on_home_smell(context, obj.get_id()):
            self._host_brain.switch_to_mode(MOVE_MODE_HOME)

        if self._host_brain.get_movement_mode() == MOVE_MODE_HOME and not self._on_home_smell(context, obj.get_id()):
            # TODO: sitwh explo que si rien a faire (rien a poser par exemple)
            self._host_brain.switch_to_mode(MOVE_MODE_EXPLO)
            self._start_new_exploration()

    @classmethod
    def _on_home_smell(cls, context, object_id):
        current_position = context.metas.value.get(POSITION, object_id)
        smell_points = context.metas.value.get(POINTS_SMELL, POINTS_SMELL, allow_empty=True, empty_value={})
        if current_position in smell_points:
            return True
        return False

    def _update_exploration_vector(self):
        # TODO: add tuple as vectors ?
        just_move_vector = directions_modifiers[self._host_brain.get_host().get_previous_direction()]
        self._set_exploration_vector((self._exploration_vector[0] + just_move_vector[1],
                                      self._exploration_vector[1] + just_move_vector[2]))


    def _apply_context(self, obj, context):
        movement_mode = self._host_brain.get_movement_mode()
        if movement_mode == MOVE_MODE_EXPLO or movement_mode == MOVE_MODE_GOHOME:
            self._update_exploration_vector()

    def _start_new_exploration(self):
        self._exploration_vector = (0, 0)