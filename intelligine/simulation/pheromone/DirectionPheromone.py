from intelligine.cst import PHEROMON_DIRECTION, PHEROMON_POSITIONS
from intelligine.core.exceptions import NoPheromone
from random import shuffle
from xyzworld.geometry import get_degree_from_north
from intelligine.synergy.event.move.direction import get_direction_for_degrees


class DirectionPheromone():

    @staticmethod
    def appose(context, point, pheromone):
        context.pheromones().increment_with_pheromone(point, pheromone)
        context.metas.list.add(PHEROMON_POSITIONS, PHEROMON_POSITIONS, point, assert_not_in=False)

    @staticmethod
    def get_direction_for_point(context, point, pheromone_type):
        flavour = context.pheromones().get_flavour(point)
        pheromone = flavour.get_pheromone(category=PHEROMON_DIRECTION, type=pheromone_type)

        distance = pheromone.get_distance()
        around_points = context.get_around_points_of(point)
        # TODO: Cet algo around a mettre ailleurs
        around_pheromones_points = []
        for around_point in around_points:
            flavour = context.pheromones().get_flavour(around_point)
            try:
                around_pheromone = flavour.get_pheromone(category=PHEROMON_DIRECTION, type=pheromone_type)
                if around_pheromone.get_distance() < distance:
                    around_pheromones_points.append((around_point, around_pheromone))
            except NoPheromone:
                pass  # No pheromone, ok continue to sniff around

        if not around_pheromones_points:
            raise NoPheromone()

        shuffle(around_pheromones_points)
        around_pheromones_sorted = sorted(around_pheromones_points, key=lambda x: x[1].get_intensity(), reverse=True)
        max_intensity = around_pheromones_sorted[0][1].get_intensity()

        around_pheromones_max = []
        for around_pheromone_sorted in around_pheromones_sorted:
            if around_pheromone_sorted[1].get_intensity() == max_intensity:
                around_pheromones_max.append(around_pheromone_sorted)

        around_pheromones_sorted_by_distance = sorted(around_pheromones_max,
                                                      key=lambda x: x[1].get_distance(),
                                                      reverse=False)

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
            flavour = context.pheromones().get_flavour(around_point)
            try:
                around_pheromone = flavour.get_pheromone(category=PHEROMON_DIRECTION, type=pheromone_type)
                around_pheromones_points.append((around_point, around_pheromone))
            except NoPheromone:
                pass  # Ok, no pheromone, continue to sniff around

        if not around_pheromones_points:
            raise NoPheromone()

        shuffle(around_pheromones_points)
        around_pheromones_sorted = sorted(around_pheromones_points, key=lambda x: x[1].get_intensity(), reverse=True)
        go_to_point = around_pheromones_sorted[0][0]

        direction_degrees = get_degree_from_north(reference_point, go_to_point)
        direction = get_direction_for_degrees(direction_degrees)

        return direction