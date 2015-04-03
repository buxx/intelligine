from intelligine.cst import PHEROMON_DIRECTION, PHEROMON_POSITIONS
from intelligine.core.exceptions import NoPheromone
from random import shuffle
from xyzworld.geometry import get_degree_from_north
from intelligine.synergy.event.move.direction import get_direction_for_degrees


class DirectionPheromone():

    @staticmethod
    def appose(context, point, movement_molecules):
        pheromone_type, distance_from = movement_molecules
        # TODO: Ajouter l'age de la pheromone !
        context.pheromones().increment(point, [PHEROMON_DIRECTION, pheromone_type], distance=distance_from)
        context.metas.list.add(PHEROMON_POSITIONS, PHEROMON_POSITIONS, point, assert_not_in=False)

    @staticmethod
    def get_direction_for_point(context, point, pheromone_type):
        try:
            pheromone_info = context.pheromones().get_info(point, [PHEROMON_DIRECTION, pheromone_type])
        except KeyError:
            raise NoPheromone()

        # DEBUG: On se rettrouve avec un {} ...
        if not pheromone_info:
            raise NoPheromone()

        point_intensity = pheromone_info[1]
        point_distance = pheromone_info[0]
        arround_points = context.get_arround_points_of(point)

        arround_pheromones_points = []
        for arround_point in arround_points:
            arround_pheromone_info = context.pheromones().get_info(arround_point,
                                                                   [PHEROMON_DIRECTION, pheromone_type],
                                                                   allow_empty=True,
                                                                   empty_value={})
            if arround_pheromone_info and arround_pheromone_info[0] < point_distance:
                arround_pheromones_points.append((arround_point, arround_pheromone_info))

        if not arround_pheromones_points:
            raise NoPheromone()

        shuffle(arround_pheromones_points)
        arround_pheromones_sorted = sorted(arround_pheromones_points, key=lambda x: x[1][1], reverse=True)
        max_intensity = arround_pheromones_sorted[0][1][1]

        arround_pheromones_max = []
        for arround_pheromone_sorted in arround_pheromones_sorted:
            if arround_pheromone_sorted[1][1] == max_intensity:
                arround_pheromones_max.append(arround_pheromone_sorted)

        arround_pheromones_sorted_by_distance = sorted(arround_pheromones_max, key=lambda x: x[1][0], reverse=False)

        go_to_point = arround_pheromones_sorted_by_distance[0][0]

        direction_degrees = get_degree_from_north(point, go_to_point)
        direction = get_direction_for_degrees(direction_degrees)

        return direction
        # # 1: On melange
        # items = pheromone_info.items()
        # shuffle(items)
        # ph = OrderedDict(items)
        # foo = True
        # # 2: On trie par puissance
        # ph_sorted = sorted(ph.items(), key=lambda x: x[1])
        # # 3: On recupere les direction de la puissance max
        # max_intensity = ph_sorted[0][1][1]
        # max_directions = [direction_name for direction_name in pheromone_info
        #                  if pheromone_info[direction_name][1] == max_intensity]
        # # 4: On trie par age
        # # 5: On recupere les directions de l'age le plus court
        # # 6: On choisis une direction au hasard parmis elles (ou par rapport a direction precedente ??bug autre fois??)

    @staticmethod
    def get_best_pheromone_direction_in(context, reference_point, points, pheromone_type):
        arround_pheromones_points = []
        for arround_point in points:
            arround_pheromone_info = context.pheromones().get_info(arround_point,
                                                                   [PHEROMON_DIRECTION, pheromone_type],
                                                                   allow_empty=True,
                                                                   empty_value={})
            if arround_pheromone_info:
                arround_pheromones_points.append((arround_point, arround_pheromone_info))

        if not arround_pheromones_points:
            raise NoPheromone()

        shuffle(arround_pheromones_points)
        arround_pheromones_sorted = sorted(arround_pheromones_points, key=lambda x: x[1][1], reverse=True)
        go_to_point = arround_pheromones_sorted[0][0]

        direction_degrees = get_degree_from_north(reference_point, go_to_point)
        direction = get_direction_for_degrees(direction_degrees)

        return direction