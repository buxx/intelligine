from intelligine.cst import PHEROMON_DIRECTION, PHEROMON_POSITIONS
from intelligine.core.exceptions import NoPheromone
from random import shuffle
from xyzworld.geometry import get_degree_from_north
from intelligine.synergy.event.move.direction import get_direction_for_degrees


class DirectionPheromone():

    @staticmethod
    def appose(context, point, movement_molecules):
        pheromone_type, distance_from = movement_molecules
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
        around_points = context.get_around_points_of(point)

        around_pheromones_points = []
        for around_point in around_points:
            around_pheromone_info = context.pheromones().get_info(around_point,
                                                                   [PHEROMON_DIRECTION, pheromone_type],
                                                                   allow_empty=True,
                                                                   empty_value={})
            if around_pheromone_info and around_pheromone_info[0] < point_distance:
                around_pheromones_points.append((around_point, around_pheromone_info))

        if not around_pheromones_points:
            raise NoPheromone()

        shuffle(around_pheromones_points)
        around_pheromones_sorted = sorted(around_pheromones_points, key=lambda x: x[1][1], reverse=True)
        max_intensity = around_pheromones_sorted[0][1][1]

        around_pheromones_max = []
        for around_pheromone_sorted in around_pheromones_sorted:
            if around_pheromone_sorted[1][1] == max_intensity:
                around_pheromones_max.append(around_pheromone_sorted)

        around_pheromones_sorted_by_distance = sorted(around_pheromones_max, key=lambda x: x[1][0], reverse=False)

        go_to_point = around_pheromones_sorted_by_distance[0][0]

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
        around_pheromones_points = []
        for around_point in points:
            around_pheromone_info = context.pheromones().get_info(around_point,
                                                                   [PHEROMON_DIRECTION, pheromone_type],
                                                                   allow_empty=True,
                                                                   empty_value={})
            if around_pheromone_info:
                around_pheromones_points.append((around_point, around_pheromone_info))

        if not around_pheromones_points:
            raise NoPheromone()

        shuffle(around_pheromones_points)
        around_pheromones_sorted = sorted(around_pheromones_points, key=lambda x: x[1][1], reverse=True)
        go_to_point = around_pheromones_sorted[0][0]

        direction_degrees = get_degree_from_north(reference_point, go_to_point)
        direction = get_direction_for_degrees(direction_degrees)

        return direction