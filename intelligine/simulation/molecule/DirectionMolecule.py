from intelligine.cst import POINTS_SMELL, MOLECULES, MOLECULES_DIRECTION
from intelligine.core.exceptions import NoMolecule
from random import shuffle
from synergine_xyz.geometry import get_degree_from_north
from intelligine.synergy.event.move.direction import get_direction_for_degrees


class DirectionMolecule():

    _positions_key = None

    @classmethod
    def appose(cls, context, point, molecule):
        context.molecules().increment_with_molecule(point, molecule)
        context.metas.list.add(MOLECULES, MOLECULES, point, assert_not_in=False)

    @classmethod
    def get_direction_for_point(cls, context, point, molecule_type):
        flavour = context.molecules().get_flavour(point)
        molecule = flavour.get_molecule(category=MOLECULES_DIRECTION, type=molecule_type)

        distance = molecule.get_distance()
        around_molecule_filter = lambda around_molecule: around_molecule.get_distance() < distance
        around_molecules_points = cls._get_around_molecules(context, point, molecule_type,
                                                            molecule_filter=around_molecule_filter)

        if not around_molecules_points:
            raise NoMolecule()

        shuffle(around_molecules_points)
        around_molecules_sorted = sorted(around_molecules_points, key=lambda x: x[1].get_intensity(), reverse=True)
        max_intensity = around_molecules_sorted[0][1].get_intensity()

        around_molecules_max = []
        for around_molecule_sorted in around_molecules_sorted:
            if around_molecule_sorted[1].get_intensity() == max_intensity:
                around_molecules_max.append(around_molecule_sorted)

        around_molecules_sorted_by_distance = sorted(around_molecules_max,
                                                      key=lambda x: x[1].get_distance(),
                                                      reverse=False)

        go_to_point = around_molecules_sorted_by_distance[0][0]

        direction_degrees = get_degree_from_north(point, go_to_point)
        direction = get_direction_for_degrees(direction_degrees)

        return direction

    @classmethod
    def _get_around_molecules(cls, context, reference_point, molecule_type,
                              molecule_filter=lambda around_molecule: True):
        around_points = context.get_around_points_of_point(reference_point)
        around_molecules_points = []
        for around_point in around_points:
            flavour = context.molecules().get_flavour(around_point)
            try:
                around_molecule = flavour.get_molecule(category=MOLECULES_DIRECTION, type=molecule_type)
                if molecule_filter(around_molecule):
                    around_molecules_points.append((around_point, around_molecule))
            except NoMolecule:
                pass  # No molecule, ok continue to sniff around

        return around_molecules_points

    @classmethod
    def get_best_molecule_direction_in(cls, context, reference_point, points, molecule_type):
        around_molecules_points = []
        for around_point in points:
            flavour = context.molecules().get_flavour(around_point)
            try:
                around_molecule = flavour.get_molecule(category=MOLECULES_DIRECTION, type=molecule_type)
                around_molecules_points.append((around_point, around_molecule))
            except NoMolecule:
                pass  # Ok, no molecule, continue to sniff around

        if not around_molecules_points:
            raise NoMolecule()

        shuffle(around_molecules_points)
        around_molecules_sorted = sorted(around_molecules_points, key=lambda x: x[1].get_intensity(), reverse=True)
        go_to_point = around_molecules_sorted[0][0]

        direction_degrees = get_degree_from_north(reference_point, go_to_point)
        direction = get_direction_for_degrees(direction_degrees)

        return direction