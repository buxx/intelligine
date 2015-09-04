from intelligine.synergy.Environment import Environment
from intelligine.synergy.object.Food import Food
from intelligine.tests.simulation.mode.Base import Base
from intelligine.synergy.Colony import Colony
from intelligine.synergy.Simulation import Simulation
from intelligine.synergy.ColonyConfiguration import ColonyConfiguration
from intelligine.synergy.event.move.MoveAction import MoveAction
from intelligine.synergy.event.move.direction import NORTH, SOUTH
from intelligine.tests.src.event.MoveAction import MoveAction as TestMoveAction
from synergine.synergy.collection.SynergyCollection import SynergyCollection
from synergine.synergy.collection.Configuration import Configuration
from intelligine.core.Context import Context
from intelligine.cst import MODE_EXPLO, MODE_GOHOME, MODE, MODE_HOME, PHEROMON_DIR_NONE
from intelligine.cst import PHEROMON_DIR_EXPLO


class TestChangeMode(Base):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ant = None
        self.food = None
        self._force_move = self._force_move

    @staticmethod
    def _force_move(self_move_action, object_id, context):
        object_movement_mode = context.metas.value.get(MODE, object_id)
        if object_movement_mode == MODE_GOHOME or object_movement_mode == MODE_HOME:
            return SOUTH
        return NORTH

    def _get_set_up_simulations(self):
        return [Simulation([self._get_colony(), self._get_foods(), self._get_environment()])]

    def _get_colony(self):
        test_case = self
        class TestColony(Colony):
            def __init__(self, configuration):
                super().__init__(configuration)
                self._actions.remove(MoveAction)
                TestMoveAction.set_move_event(test_case._force_move)
                self._actions.append(TestMoveAction)
        return TestColony(self._get_colony_configuration())

    def _get_colony_configuration(self):
        test_case = self
        class TestColonyConfiguration(ColonyConfiguration):
            _start_position = (0, 0, 0)
            _ant_count = 1
            def get_start_objects(self, collection, context):
                ants = super().get_start_objects(collection, context)
                test_case.ant = ants[0]
                return ants
        return TestColonyConfiguration()

    def _get_foods(self):
        class Foods(SynergyCollection):
            pass
        return Foods(self._get_food_configuration())

    def _get_food_configuration(self):
        test_case = self
        class FoodConfiguration(Configuration):
            def get_start_objects(self, collection, context):
                foods = []
                food = Food(collection, context)
                stocked_food = Food(collection, context)
                stocked_food.transform_to_stocked()
                food.set_position((0, 0, -20))
                stocked_food.set_position((0, 0, 0))
                foods.append(stocked_food)
                foods.append(food)
                test_case.food = food
                return foods
        return FoodConfiguration()

    def _get_environment(self):
        class TestEnvironment(Environment):
            pass
        return TestEnvironment(self._get_environment_configuration())

    def _get_environment_configuration(self):
        class TestEnvironmentConfiguration(Configuration):
            pass
        return TestEnvironmentConfiguration()

    def _get_core_configuration(self, cycles, main_process=True):
        config = super()._get_core_configuration(cycles, main_process)
        config.update({
            'app': {
                'classes': {
                    'Context': Context
                }
            },
            'ant': {
                'take': {
                    # Disable this constrain to test in little space
                    'cant_put_still': 0
                }
            }
        })
        return config

    def test_from_exploration_to_go_home(self):
        self._run_and_get_core(0)
        self.assertEquals((0, 0, 0), self.ant.get_position())
        self.assertEquals(MODE_EXPLO, self.ant.get_brain().get_movement_mode())
        self.assertFalse(self.ant.is_carrying())

        self._run_and_get_core(1)
        self.assertEquals((0, 0, -1), self.ant.get_position())
        self.assertEquals(MODE_EXPLO, self.ant.get_brain().get_movement_mode())
        self.assertFalse(self.ant.is_carrying())

        # Ant has take Food piece
        self._run_and_get_core(20)
        self.assertEquals((0, 0, -20), self.ant.get_position())
        self.assertTrue(self.ant.is_carrying())
        self.assertIsNotNone(self.ant.get_carried())
        self.assertEquals(self.food.__class__, self.ant.get_carried().__class__)
        molecule = self.ant.get_movement_molecule_gland().get_molecule()
        # Now it appose exploration molecule
        self.assertEquals((PHEROMON_DIR_EXPLO, 0), (molecule.get_type(), molecule.get_distance()))
        self.assertEquals(MODE_GOHOME, self.ant.get_brain().get_movement_mode())
        self.assertEquals(PHEROMON_DIR_EXPLO, self.ant.get_movement_molecule_gland().get_molecule_type())

        self._run_and_get_core(34)
        self.assertEquals((0, 0, -6), self.ant.get_position())
        self.assertTrue(self.ant.is_carrying())
        self.assertEquals(MODE_HOME, self.ant.get_brain().get_movement_mode())

        self._run_and_get_core(35)
        self.assertEquals((0, 0, -5), self.ant.get_position())
        self.assertTrue(self.ant.is_carrying())
        self.assertEquals(MODE_HOME, self.ant.get_brain().get_movement_mode())

        self._run_and_get_core(36)
        self.assertEquals((0, 0, -4), self.ant.get_position())
        self.assertEquals(MODE_HOME, self.ant.get_brain().get_movement_mode())

        self._run_and_get_core(39)
        self.assertEquals((0, 0, -1), self.ant.get_position())
        # Ant has NOT put his food piece
        self.assertFalse(self.ant.is_carrying())

        self._run_and_get_core(40)
        self.assertEquals((0, 0, -2), self.ant.get_position())
        self.assertFalse(self.ant.is_carrying())
