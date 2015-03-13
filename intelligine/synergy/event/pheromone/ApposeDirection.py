from synergine.synergy.event.Action import Action
from intelligine.synergy.event.pheromone.PheromoneEvent import PheromoneEvent
from xyzworld.cst import POSITION
from intelligine.cst import PHEROMON_DIRECTION, PHEROMON_DIR_EXPLO, PHEROMON_POSITIONS
from xyzworld.geometry import get_direction_degrees, get_degree_from_north
from intelligine.synergy.event.move.direction import get_direction_for_degrees, get_direction_opposite


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
        :param obj:
        :param context:
        :param synergy_manager:
        :return:
        """
        # TODO: Remonter ca dans une objet

        # a = get_direction_degrees((0, 0, 0), (0, -1, -1)) # 315
        # a = get_direction_degrees((0, 0, 0), (0, 0, -1))  # 0
        # a = get_direction_degrees((0, 0, 0), (0, 1, -1))  # 45
        # a = get_direction_degrees((0, 0, 0), (0, -1, 0))  # 270
        # a = get_direction_degrees((0, 0, 0), (0, 1, 0))   # 90
        # a = get_direction_degrees((0, 0, 0), (0, -1, 1))  # 225
        # a = get_direction_degrees((0, 0, 0), (0, 0, 1))   # 180
        # a = get_direction_degrees((0, 0, 0), (0, 1, 1))   # 135

        # a = get_degree_from_north((0, 0, 0), (0, -1, -1)) # 315
        # a = get_degree_from_north((0, 0, 0), (0, 0, -1))  # 0
        # a = get_degree_from_north((0, 0, 0), (0, 1, -1))  # 45
        # a = get_degree_from_north((0, 0, 0), (0, -1, 0))  # 270
        # a = get_degree_from_north((0, 0, 0), (0, 1, 0))   # 90
        # a = get_degree_from_north((0, 0, 0), (0, -1, 1))  # 225
        # a = get_degree_from_north((0, 0, 0), (0, 0, 1))   # 180
        # a = get_degree_from_north((0, 0, 0), (0, 1, 1))   # 135
        self._appose_pheromones(obj, context, synergy_manager)

    def _appose_pheromones(self, obj, context, synergy_manager):
        obj_position = obj.get_position()
        obj_last_pheromon_position = obj.get_last_pheromone_point(PHEROMON_DIRECTION)
        try:
            direction_degrees = get_degree_from_north(obj_last_pheromon_position, obj_position)
        except ZeroDivisionError:
            return
        direction = get_direction_for_degrees(direction_degrees)
        from_direction = get_direction_opposite(direction)
        depose_intensity = 1 # TODO: config

        for affected_point in self._parameters['concerned_points']:
            self._appose_pheromone(context, affected_point, direction, depose_intensity)
            context.metas.list.add(PHEROMON_POSITIONS, PHEROMON_POSITIONS, affected_point, assert_not_in=False)

        obj.set_last_pheromone_point(PHEROMON_DIRECTION, obj.get_position())

    def _appose_pheromone(self, context, affected_point, direction, depose_intensity):
        context.pheromones().increment(affected_point, [PHEROMON_DIRECTION,
                                                        PHEROMON_DIR_EXPLO,
                                                        direction], depose_intensity)




