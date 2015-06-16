from intelligine.cst import PHEROMON_DIRECTION, PHEROMON_POSITIONS
from intelligine.core.exceptions import NoPheromone
from random import shuffle
from synergine_xyz.geometry import get_degree_from_north
from intelligine.synergy.event.move.direction import get_direction_for_degrees


class DirectionPheromone():

    @staticmethod
    def appose(context, point, pheromone):
        context.pheromones().increment_with_pheromone(point, pheromone)
        context.metas.list.add(PHEROMON_POSITIONS, PHEROMON_POSITIONS, point, assert_not_in=False)

    @classmethod
    def get_direction_for_point(cls, context, point, pheromone_type):
        flavour = context.pheromones().get_flavour(point)
        pheromone = flavour.get_pheromone(category=PHEROMON_DIRECTION, type=pheromone_type)

        distance = pheromone.get_distance()
        around_pheromone_filter = lambda around_pheromone: around_pheromone.get_distance() < distance
        around_pheromones_points = cls._get_around_pheromones(context, point, pheromone_type,
                                                              pheromone_filter=around_pheromone_filter)

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

    @staticmethod
    def _get_around_pheromones(context, reference_point, pheromone_type,
                               pheromone_filter=lambda around_pheromone: True):
        around_points = context.get_around_points_of_point(reference_point)
        around_pheromones_points = []
        for around_point in around_points:
            flavour = context.pheromones().get_flavour(around_point)
            try:
                around_pheromone = flavour.get_pheromone(category=PHEROMON_DIRECTION, type=pheromone_type)
                if pheromone_filter(around_pheromone):
                    around_pheromones_points.append((around_point, around_pheromone))
            except NoPheromone:
                pass  # No pheromone, ok continue to sniff around

        return around_pheromones_points

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