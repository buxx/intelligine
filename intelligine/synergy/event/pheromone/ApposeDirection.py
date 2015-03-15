from synergine.synergy.event.Action import Action
from intelligine.synergy.event.pheromone.PheromoneEvent import PheromoneEvent
from xyzworld.cst import POSITION
from intelligine.cst import PHEROMON_DIRECTION, PHEROMON_DIR_HOME, PHEROMON_POSITIONS, MOVE_MODE_EXPLO
from xyzworld.geometry import get_degree_from_north
from intelligine.synergy.event.move.direction import get_direction_for_degrees, get_direction_opposite
from intelligine.core.exceptions import SamePosition


class ApposeDirection(Action):

    _listen = PheromoneEvent

    def prepare(self, context):
        """
        Recupere chaque coordonnees de points qui doivent etre update
        pour ne pas avoir a e calculer dans le run
        :param context:
        :return:
        """
        object_point =  context.metas.value.get(POSITION, self._object_id)
        distance = 1 # TODO: Config ?
        self._parameters['concerned_points'] = context.get_arround_points_of(object_point, distance)

    def run(self, obj, context, synergy_manager):
        """
        On effectue l'incrementation dans le process principal. Beaucoups plus lourd que de le faie dans les
        process. Mais si on le fait dans les process on va rater des infos ...
        met a jour les pts (incremente)
        """
        self._appose_pheromones(obj, context, synergy_manager)

    def _appose_pheromones(self, obj, context, synergy_manager):
        try:
            from_direction = self._get_from_direction(obj)
        except SamePosition:
            return

        depose_intensity = 1 # TODO: config
        pheromone_direction_type = self._get_pheromone_direction_type(obj)
        for affected_point in self._parameters['concerned_points']:
            context.pheromones().increment(affected_point, [PHEROMON_DIRECTION,
                                                            pheromone_direction_type,
                                                            from_direction], depose_intensity)
            context.metas.list.add(PHEROMON_POSITIONS, PHEROMON_POSITIONS, affected_point, assert_not_in=False)

        obj.set_last_pheromone_point(PHEROMON_DIRECTION, obj.get_position())

    def _get_from_direction(self, obj):
        obj_position = obj.get_position()
        obj_last_pheromon_position = obj.get_last_pheromone_point(PHEROMON_DIRECTION)
        try:
            direction_degrees = get_degree_from_north(obj_last_pheromon_position, obj_position)
        except ZeroDivisionError:
            raise SamePosition()
        direction = get_direction_for_degrees(direction_degrees)
        return get_direction_opposite(direction)

    def _get_pheromone_direction_type(self, obj):
        if obj.get_movement_mode() == MOVE_MODE_EXPLO:
            return PHEROMON_DIR_HOME
        raise NotImplementedError()