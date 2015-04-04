from os import getcwd
from sys import path as ppath
from intelligine.core.exceptions import NoPheromone
from intelligine.simulation.pheromone.Pheromone import Pheromone
from intelligine.simulation.pheromone.PheromoneFlavour import PheromoneFlavour

ppath.insert(1,getcwd()+'/modules')

from intelligine.tests.simulation.pheromone.Base import Base
from intelligine.simulation.pheromone.DirectionPheromone import DirectionPheromone
from intelligine.core.Context import Context
from intelligine.cst import PHEROMON_DIRECTION, PHEROMON_DIR_EXPLO, PHEROMON_DIR_HOME
from intelligine.synergy.event.move.direction import NORTH, NORTH_EST, EST, SOUTH_EST, SOUTH, SOUTH_WEST, WEST, \
    NORTH_WEST, CENTER
from intelligine.synergy.event.move.direction import get_position_with_direction_decal as _p


class TestDirection(Base):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._context = Context()

    def setUp(self):
        self._context = Context()

    def _set_up_pheromones(self, pheromones, re_init=True):
        if re_init:
            self._context = Context()
        for position in pheromones:
            self._context.pheromones().set_flavour(position, PheromoneFlavour.new_from_raw_data(pheromones[position]))

    def _test_direction_for_point(self, pheromones, direction, pheromone_type=PHEROMON_DIR_EXPLO,
                                  reference_point=_p(CENTER), re_init=True):
        """

        :param pheromones:
        :param direction:
        :param pheromone_type:
        :param reference_point:
        :return:
        """
        self._set_up_pheromones(pheromones, re_init=re_init)
        direction_tested = DirectionPheromone.get_direction_for_point(self._context, reference_point, pheromone_type)
        self.assertEqual(direction, direction_tested, "Direction must be %s" % direction)

    def _test_direction_for_points(self, pheromones, direction, pheromone_type=PHEROMON_DIR_EXPLO,
                                   reference_point=_p(CENTER), re_init=True):
        """

        :param pheromones:
        :param direction:
        :param pheromone_type:
        :param reference_point:
        :return:
        """
        self._set_up_pheromones(pheromones, re_init=re_init)
        around_points = self._context.get_around_points_of(reference_point)
        direction_tested = DirectionPheromone.get_best_pheromone_direction_in(self._context,
                                                                              reference_point,
                                                                              around_points,
                                                                              pheromone_type)
        self.assertEqual(direction, direction_tested, "Direction must be %s" % direction)

    def test_route_direct_route(self):
        """
        Test easy direction with 1 best pheromones just near actual position
        :return:
        """
        test_data = {
            NORTH_WEST: {
                _p(CENTER): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                _p(NORTH_WEST): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}}
            },
            NORTH: {
                _p(CENTER): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                _p(NORTH): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}}
            },
            NORTH_EST: {
                _p(CENTER): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                _p(NORTH_EST): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}}
            },
            WEST: {
                _p(CENTER): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                _p(WEST): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}}
            },
            EST: {
                _p(CENTER): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                _p(EST): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}}
            },
            SOUTH_WEST: {
                _p(CENTER): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                _p(SOUTH_WEST): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}}
            },
            SOUTH: {
                _p(CENTER): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                _p(SOUTH): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}}
            },
            SOUTH_EST: {
                _p(CENTER): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                _p(SOUTH_EST): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}}
            }
        }

        for direction_wanted in test_data:
            self._test_direction_for_point(test_data[direction_wanted], direction_wanted)

    def test_route_with_multiple_same_intensity(self):
        """
        Test find route in middle of multiple pheromones
        :return:
        """
        test_data = {
            NORTH_WEST: {
                _p(CENTER): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                _p(NORTH_WEST): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}},
                _p(SOUTH_EST): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (12, 1)}}
            },
            NORTH_WEST: {
                _p(CENTER): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                _p(NORTH_WEST): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}},
                _p(SOUTH_EST): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (12, 1)}},
                _p(SOUTH): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (12, 1)}}
            },
            NORTH_WEST: {
                _p(CENTER): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                _p(NORTH_WEST): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}},
                _p(SOUTH_EST): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (12, 1)}},
                _p(SOUTH): {PHEROMON_DIRECTION: {PHEROMON_DIR_HOME: (8, 1)}}
            },
        }

        for direction_wanted in test_data:
            self._test_direction_for_point(test_data[direction_wanted], direction_wanted)

    def test_route_with_multiple_different_intensity(self):
        """
        Test find route in middle of multiple pheromones
        :return:
        """
        test_data = {
            NORTH_WEST: {
                _p(CENTER): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 2)}},
                _p(NORTH_WEST): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 2)}},
                _p(SOUTH_EST): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (8, 1)}}
            },
            NORTH_WEST: {
                _p(CENTER): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 2)}},
                _p(NORTH_WEST): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 2)}},
                _p(SOUTH_EST): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (8, 1)}},
                _p(SOUTH_EST): {PHEROMON_DIRECTION: {PHEROMON_DIR_HOME: (5, 10)}}  # an other pheromone type
            }
        }

        for direction_wanted in test_data:
            self._test_direction_for_point(test_data[direction_wanted], direction_wanted)

    def test_direction_direct(self):
        test_data = {
            NORTH: {
                _p(NORTH): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 2)}}
            },
            NORTH: {
                _p(NORTH): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 2)}},
                _p(NORTH_WEST): {PHEROMON_DIRECTION: {PHEROMON_DIR_HOME: (9, 500)}}  # An other pheromone type
            }
        }

        for direction in test_data:
            self._test_direction_for_points(test_data[direction], direction)

    def test_direction_with_multiple_intensity(self):
        test_data = {
            NORTH: {
                _p(NORTH): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 5)}},
                _p(SOUTH_EST): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 4)}},
                _p(NORTH_WEST): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 4)}}
            },
            NORTH: {
                _p(NORTH): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 5)}},
                _p(WEST): {PHEROMON_DIRECTION: {PHEROMON_DIR_HOME: (9, 500)}},  # An other pheromone_type
                _p(SOUTH_EST): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 4)}},
                _p(NORTH_WEST): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 4)}}
            }
        }

        for direction in test_data:
            self._test_direction_for_points(test_data[direction], direction)

    def test_no_pheromones_around(self):
        # No pheromone
        try:  # WTF ?
            self.assertRaises(NoPheromone, self._test_direction_for_points({}, -1))
        except NoPheromone:
            self.assertTrue(True)

        # Wrong pheromone type
        try:  # WTF ?
            self.assertRaises(NoPheromone, self._test_direction_for_points({
                _p(SOUTH_EST): {PHEROMON_DIRECTION: {PHEROMON_DIR_HOME: (9, 5)}}
            }, -1))
        except NoPheromone:
            self.assertTrue(True)

    def test_appose(self):
        self._test_point_raise_no_pheromone()
        self._test_points_raise_no_pheromone()

        # Une pheromone au centre
        DirectionPheromone.appose(self._context,
                                  _p(CENTER),
                                  self._get_pheromone(PHEROMON_DIR_EXPLO, 2))
        # Ne permet pas de trouver une route
        self._test_point_raise_no_pheromone(re_init=False)
        self._test_points_raise_no_pheromone(re_init=False)

        # Une pheromone au nord
        DirectionPheromone.appose(self._context,
                                  _p(NORTH),
                                  self._get_pheromone(PHEROMON_DIR_EXPLO, 1))
        # le permet
        self._test_direction_for_points({}, NORTH, re_init=False)
        self._test_direction_for_point({}, NORTH, re_init=False)


    def _test_point_raise_no_pheromone(self, pheromones={}, direction=-1, pheromone_type=PHEROMON_DIR_EXPLO,
                                 reference_point=_p(CENTER), re_init=True):
        try:  # WTF ?
            self._test_direction_for_point(pheromones, direction, re_init=re_init)
        except NoPheromone:
            self.assertTrue(True)

    def _test_points_raise_no_pheromone(self, pheromones={}, direction=-1, pheromone_type=PHEROMON_DIR_EXPLO,
                                 reference_point=_p(CENTER), re_init=True):
        try:  # WTF ?
            self._test_direction_for_points(pheromones, direction, re_init=re_init)
        except NoPheromone:
            self.assertTrue(True)

    def _get_pheromone(self, type, distance):
        return Pheromone(PHEROMON_DIRECTION, type, distance=distance)