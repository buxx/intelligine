from intelligine.core.exceptions import NoMolecule
from intelligine.simulation.molecule.Molecule import Molecule
from intelligine.simulation.molecule.MoleculeFlavour import MoleculeFlavour
from intelligine.tests.simulation.molecule.Base import Base
from intelligine.simulation.molecule.DirectionMolecule import DirectionMolecule
from intelligine.core.Context import Context
from intelligine.cst import MOLECULES_DIRECTION, PHEROMON_DIR_EXPLO, PHEROMON_DIR_NONE
from intelligine.synergy.event.move.direction import NORTH, NORTH_EST, EST, SOUTH_EST, SOUTH, SOUTH_WEST, WEST, \
    NORTH_WEST, CENTER
from intelligine.synergy.event.move.direction import get_position_with_direction_decal as _p


class TestDirection(Base):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._context = Context()

    def setUp(self):
        self._context = Context()

    def _set_up_molecules(self, molecules, re_init=True):
        if re_init:
            self._context = Context()
        for position in molecules:
            self._context.molecules().set_flavour(position, MoleculeFlavour.new_from_raw_data(molecules[position]))

    def _test_direction_for_point(self, molecules, direction, molecule_type=PHEROMON_DIR_EXPLO,
                                  reference_point=_p(CENTER), re_init=True):
        """

        :param molecules:
        :param direction:
        :param molecule_type:
        :param reference_point:
        :return:
        """
        self._set_up_molecules(molecules, re_init=re_init)
        direction_tested = DirectionMolecule.get_direction_for_point(self._context, reference_point, molecule_type)
        self.assertEqual(direction, direction_tested, "Direction must be %s" % direction)

    def _test_direction_for_points(self, molecules, direction, molecule_type=PHEROMON_DIR_EXPLO,
                                   reference_point=_p(CENTER), re_init=True):
        """

        :param molecules:
        :param direction:
        :param molecule_type:
        :param reference_point:
        :return:
        """
        self._set_up_molecules(molecules, re_init=re_init)
        around_points = self._context.get_around_points_of_point(reference_point)
        direction_tested = DirectionMolecule.get_best_molecule_direction_in(self._context,
                                                                              reference_point,
                                                                              around_points,
                                                                              molecule_type)
        self.assertEqual(direction, direction_tested, "Direction must be %s" % direction)

    def test_route_direct_route(self):
        """
        Test easy direction with 1 best molecules just near actual position
        :return:
        """
        test_data = {
            NORTH_WEST: {
                _p(CENTER): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                _p(NORTH_WEST): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}}
            },
            NORTH: {
                _p(CENTER): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                _p(NORTH): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}}
            },
            NORTH_EST: {
                _p(CENTER): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                _p(NORTH_EST): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}}
            },
            WEST: {
                _p(CENTER): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                _p(WEST): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}}
            },
            EST: {
                _p(CENTER): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                _p(EST): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}}
            },
            SOUTH_WEST: {
                _p(CENTER): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                _p(SOUTH_WEST): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}}
            },
            SOUTH: {
                _p(CENTER): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                _p(SOUTH): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}}
            },
            SOUTH_EST: {
                _p(CENTER): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                _p(SOUTH_EST): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}}
            }
        }

        for direction_wanted in test_data:
            self._test_direction_for_point(test_data[direction_wanted], direction_wanted)

    def test_route_with_multiple_same_intensity(self):
        """
        Test find route in middle of multiple molecules
        :return:
        """
        test_data = {
            NORTH_WEST: {
                _p(CENTER): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                _p(NORTH_WEST): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}},
                _p(SOUTH_EST): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (12, 1)}}
            },
            NORTH_WEST: {
                _p(CENTER): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                _p(NORTH_WEST): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}},
                _p(SOUTH_EST): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (12, 1)}},
                _p(SOUTH): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (12, 1)}}
            },
            NORTH_WEST: {
                _p(CENTER): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                _p(NORTH_WEST): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}},
                _p(SOUTH_EST): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (12, 1)}},
                _p(SOUTH): {MOLECULES_DIRECTION: {PHEROMON_DIR_NONE: (8, 1)}}
            },
        }

        for direction_wanted in test_data:
            self._test_direction_for_point(test_data[direction_wanted], direction_wanted)

    def test_route_with_multiple_different_intensity(self):
        """
        Test find route in middle of multiple molecules
        :return:
        """
        test_data = {
            NORTH_WEST: {
                _p(CENTER): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 2)}},
                _p(NORTH_WEST): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 2)}},
                _p(SOUTH_EST): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (8, 1)}}
            },
            NORTH_WEST: {
                _p(CENTER): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 2)}},
                _p(NORTH_WEST): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 2)}},
                _p(SOUTH_EST): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (8, 1)}},
                _p(SOUTH_EST): {MOLECULES_DIRECTION: {PHEROMON_DIR_NONE: (5, 10)}}  # an other molecule type
            }
        }

        for direction_wanted in test_data:
            self._test_direction_for_point(test_data[direction_wanted], direction_wanted)

    def test_direction_direct(self):
        test_data = {
            NORTH: {
                _p(NORTH): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 2)}}
            },
            NORTH: {
                _p(NORTH): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 2)}},
                _p(NORTH_WEST): {MOLECULES_DIRECTION: {PHEROMON_DIR_NONE: (9, 500)}}  # An other molecule type
            }
        }

        for direction in test_data:
            self._test_direction_for_points(test_data[direction], direction)

    def test_direction_with_multiple_intensity(self):
        test_data = {
            NORTH: {
                _p(NORTH): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 5)}},
                _p(SOUTH_EST): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 4)}},
                _p(NORTH_WEST): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 4)}}
            },
            NORTH: {
                _p(NORTH): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 5)}},
                _p(WEST): {MOLECULES_DIRECTION: {PHEROMON_DIR_NONE: (9, 500)}},  # An other molecule_type
                _p(SOUTH_EST): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 4)}},
                _p(NORTH_WEST): {MOLECULES_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 4)}}
            }
        }

        for direction in test_data:
            self._test_direction_for_points(test_data[direction], direction)

    def test_no_molecules_around(self):
        # No molecule
        try:  # WTF ?
            self.assertRaises(NoMolecule, self._test_direction_for_points({}, -1))
        except NoMolecule:
            self.assertTrue(True)

        # Wrong molecule type
        try:  # WTF ?
            self.assertRaises(NoMolecule, self._test_direction_for_points({
                _p(SOUTH_EST): {MOLECULES_DIRECTION: {PHEROMON_DIR_NONE: (9, 5)}}
            }, -1))
        except NoMolecule:
            self.assertTrue(True)

    def test_appose(self):
        self._test_point_raise_no_molecule()
        self._test_points_raise_no_molecule()

        # Une molecule au centre
        DirectionMolecule.appose(self._context,
                                  _p(CENTER),
                                  self._get_molecule(PHEROMON_DIR_EXPLO, 2))
        # Ne permet pas de trouver une route
        self._test_point_raise_no_molecule(re_init=False)
        self._test_points_raise_no_molecule(re_init=False)

        # Une molecule au nord
        DirectionMolecule.appose(self._context,
                                  _p(NORTH),
                                  self._get_molecule(PHEROMON_DIR_EXPLO, 1))
        # le permet
        self._test_direction_for_points({}, NORTH, re_init=False)
        self._test_direction_for_point({}, NORTH, re_init=False)


    def _test_point_raise_no_molecule(self, molecules={}, direction=-1, molecule_type=PHEROMON_DIR_EXPLO,
                                 reference_point=_p(CENTER), re_init=True):
        try:  # WTF ?
            self._test_direction_for_point(molecules, direction, re_init=re_init)
        except NoMolecule:
            self.assertTrue(True)

    def _test_points_raise_no_molecule(self, molecules={}, direction=-1, molecule_type=PHEROMON_DIR_EXPLO,
                                 reference_point=_p(CENTER), re_init=True):
        try:  # WTF ?
            self._test_direction_for_points(molecules, direction, re_init=re_init)
        except NoMolecule:
            self.assertTrue(True)

    def _get_molecule(self, type, distance):
        return Molecule(MOLECULES_DIRECTION, type, distance=distance)