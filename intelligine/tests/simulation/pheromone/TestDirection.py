from os import getcwd
from sys import path as ppath
ppath.insert(1,getcwd()+'/modules') # TODO: win32 compatibilite (python path)
# TODO: load et launch des tests auto (avec bootstrap contenant ci dessus)

from intelligine.tests.simulation.pheromone.Base import Base
from intelligine.simulation.pheromone.DirectionPheromone import DirectionPheromone
from intelligine.core.Context import Context
from intelligine.cst import PHEROMON_DIRECTION, PHEROMON_DIR_EXPLO


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
            self._context.pheromones().set_pheromones(position, pheromones[position])

    def _test_direction_point(self, pheromones, direction, pheromone_type=PHEROMON_DIR_EXPLO, reference_point=(0, 0, 0)):
        """

        :param pheromones:
        :param direction:
        :param pheromone_type:
        :param reference_point:
        :return: void
        """
        self._set_up_pheromones(pheromones)
        direction_tested = DirectionPheromone.get_direction_for_point(self._context, reference_point, pheromone_type)
        self.assertEqual(direction, direction_tested, "Direction must be %s" % direction)

    def test_direct_route(self):
        """
        Test easy direction with 1 best pheromones just near actual position
        :return:
        """
        test_data = {
            10: {
                (0, 0, 0): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                (0, -1, -1): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}}
            },
            11: {
                (0, 0, 0): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                (0, 0, -1): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}}
            },
            12: {
                (0, 0, 0): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                (0, 1, -1): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}}
            },
            13: {
                (0, 0, 0): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                (0, -1, 0): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}}
            },
            15: {
                (0, 0, 0): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                (0, 1, 0): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}}
            },
            16: {
                (0, 0, 0): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                (0, -1, 1): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}}
            },
            17: {
                (0, 0, 0): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                (0, 0, 1): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}}
            },
            18: {
                (0, 0, 0): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                (0, 1, 1): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}}
            }
        }

        for direction_wanted in test_data:
            self._test_direction_point(test_data[direction_wanted], direction_wanted)

    def test_with_multiple_same_intensity(self):
        """
        Test find route in middle of multiple pheromones
        :return:
        """
        test_data = {
            10: {
                (0, 0, 0): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                (0, -1, -1): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}},
                (0, 1, 1): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (12, 1)}}
            },
            10: {
                (0, 0, 0): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 1)}},
                (0, -1, -1): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 1)}},
                (0, 1, 1): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (12, 1)}},
                (0, 0, 1): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (12, 1)}}
            },
        }

        for direction_wanted in test_data:
            self._test_direction_point(test_data[direction_wanted], direction_wanted)

    def test_with_multiple_different_intensity(self):
        """
        Test find route in middle of multiple pheromones
        :return:
        """
        test_data = {
            10: {
                (0, 0, 0): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (10, 2)}},
                (0, -1, -1): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (9, 2)}},
                (0, 1, 1): {PHEROMON_DIRECTION: {PHEROMON_DIR_EXPLO: (8, 1)}}
            }
        }

        for direction_wanted in test_data:
            self._test_direction_point(test_data[direction_wanted], direction_wanted)