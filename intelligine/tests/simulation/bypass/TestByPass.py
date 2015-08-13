from intelligine.synergy.Colony import Colony
from intelligine.synergy.object.ant.Ant import Ant
from intelligine.tests.src.simulation.SimpleTestWorld1Simulation import SimpleTestWorld1Simulation


class TestByPass(SimpleTestWorld1Simulation):

    _ant_move_history = []
    _assert_ant_move_history = [(0, 21, 20), (0, 21, 19), (0, 21, 18), (0, 21, 17), (0, 21, 16), (0, 21, 15), (0, 21, 14), (0, 21, 14), (0, 22, 13), (0, 23, 12), (0, 24, 11), (0, 24, 11), (0, 24, 11), (0, 24, 11), (0, 24, 11), (0, 23, 11), (0, 22, 11), (0, 21, 11), (0, 21, 11), (0, 21, 11), (0, 21, 11), (0, 21, 11), (0, 22, 12), (0, 23, 13), (0, 24, 14), (0, 24, 14), (0, 24, 14), (0, 24, 14), (0, 24, 14), (0, 23, 15), (0, 22, 16), (0, 21, 17), (0, 21, 17), (0, 21, 17), (0, 21, 17), (0, 21, 17), (0, 21, 16), (0, 21, 15), (0, 21, 14), (0, 21, 13), (0, 21, 12), (0, 21, 11), (0, 21, 10), (0, 21, 9), (0, 21, 8), (0, 21, 7), (0, 21, 6), (0, 21, 5), (0, 21, 4), (0, 21, 3), (0, 22, 2), (0, 23, 1), (0, 23, 1), (0, 23, 1), (0, 23, 1), (0, 23, 1), (0, 22, 1), (0, 21, 1), (0, 20, 1), (0, 19, 1), (0, 18, 1), (0, 17, 1), (0, 16, 1), (0, 15, 1), (0, 14, 1), (0, 13, 1), (0, 12, 1), (0, 11, 1), (0, 10, 1), (0, 9, 1), (0, 8, 2), (0, 7, 2), (0, 6, 3), (0, 5, 4), (0, 4, 5), (0, 3, 5), (0, 4, 6), (0, 5, 7), (0, 6, 8), (0, 7, 9), (0, 8, 10), (0, 9, 11), (0, 10, 12), (0, 11, 13), (0, 11, 14), (0, 12, 15), (0, 13, 16), (0, 14, 17), (0, 15, 17), (0, 16, 17), (0, 17, 17), (0, 18, 17), (0, 19, 17), (0, 19, 16), (0, 19, 15), (0, 19, 14), (0, 19, 13), (0, 19, 12), (0, 19, 11), (0, 19, 10), (0, 19, 9), (0, 18, 9), (0, 17, 9), (0, 16, 9), (0, 15, 9), (0, 14, 9), (0, 13, 9), (0, 13, 10), (0, 13, 11), (0, 13, 12), (0, 13, 13), (0, 14, 13), (0, 15, 13), (0, 16, 13), (0, 17, 13), (0, 17, 14), (0, 16, 15), (0, 15, 15), (0, 14, 15), (0, 13, 15), (0, 14, 15), (0, 15, 15), (0, 16, 15), (0, 17, 15), (0, 17, 14), (0, 16, 13), (0, 15, 13), (0, 14, 13), (0, 13, 13), (0, 13, 12), (0, 13, 11), (0, 13, 10), (0, 13, 9), (0, 14, 9), (0, 15, 9), (0, 16, 9), (0, 17, 9), (0, 18, 9), (0, 19, 9), (0, 19, 10), (0, 19, 11), (0, 19, 12), (0, 19, 13), (0, 19, 14), (0, 19, 15), (0, 19, 16), (0, 19, 17), (0, 18, 17), (0, 17, 17), (0, 16, 17), (0, 15, 17), (0, 14, 17), (0, 13, 17), (0, 12, 17), (0, 11, 17), (0, 10, 17), (0, 9, 17), (0, 8, 17), (0, 7, 17), (0, 6, 17), (0, 5, 17), (0, 4, 17), (0, 3, 17), (0, 2, 17), (0, 1, 17), (0, 1, 16), (0, 1, 15), (0, 1, 14), (0, 1, 13), (0, 1, 12), (0, 1, 11), (0, 1, 10), (0, 1, 9), (0, 1, 8), (0, 1, 7), (0, 1, 6), (0, 1, 5), (0, 1, 4), (0, 1, 3), (0, 1, 2), (0, 1, 1), (0, 2, 1), (0, 3, 1), (0, 4, 1), (0, 5, 1), (0, 6, 1), (0, 7, 1), (0, 8, 1), (0, 9, 1), (0, 10, 1), (0, 11, 1), (0, 12, 1), (0, 13, 1), (0, 14, 1), (0, 15, 1), (0, 16, 1), (0, 17, 1), (0, 18, 1), (0, 19, 1), (0, 20, 1), (0, 21, 1), (0, 22, 1), (0, 23, 1), (0, 24, 1), (0, 24, 2), (0, 24, 3), (0, 24, 4), (0, 24, 5), (0, 24, 6), (0, 24, 7), (0, 24, 8), (0, 24, 9), (0, 24, 10), (0, 24, 11), (0, 24, 12), (0, 24, 13), (0, 24, 14), (0, 24, 15), (0, 24, 16), (0, 24, 17), (0, 23, 17), (0, 22, 17), (0, 21, 17), (0, 21, 18), (0, 21, 19), (0, 21, 20), (0, 21, 21), (0, 20, 22), (0, 19, 22), (0, 18, 23), (0, 18, 24), (0, 18, 23), (0, 19, 22), (0, 20, 22), (0, 21, 21), (0, 21, 20), (0, 21, 19), (0, 21, 18), (0, 22, 17), (0, 23, 17), (0, 24, 16), (0, 24, 15), (0, 24, 14), (0, 24, 13), (0, 24, 12), (0, 24, 11), (0, 24, 10), (0, 24, 9), (0, 24, 8), (0, 24, 7), (0, 24, 6), (0, 24, 5), (0, 24, 4), (0, 24, 3), (0, 24, 2), (0, 23, 1), (0, 22, 1), (0, 21, 1), (0, 20, 1), (0, 19, 1), (0, 18, 1), (0, 17, 1), (0, 16, 1), (0, 15, 1), (0, 14, 1), (0, 13, 1), (0, 12, 1), (0, 11, 1), (0, 10, 1), (0, 9, 1), (0, 8, 1), (0, 7, 1), (0, 6, 1), (0, 7, 2), (0, 8, 3), (0, 9, 4), (0, 10, 5), (0, 11, 6), (0, 12, 7), (0, 13, 7), (0, 14, 7), (0, 15, 7), (0, 16, 7), (0, 17, 7), (0, 18, 7), (0, 19, 7), (0, 20, 7), (0, 21, 7), (0, 21, 8), (0, 21, 9), (0, 21, 10), (0, 21, 11), (0, 21, 12), (0, 21, 13), (0, 21, 14), (0, 21, 15), (0, 21, 16), (0, 21, 17), (0, 21, 18), (0, 21, 19), (0, 21, 20)]

    def setUp(self):
        super().setUp()
        self._ant_move_history = []

    def test_simulation_road(self):
        self._connection.receive_callback = self._record_ant_moves
        self._run_and_get_core(300)
        self.assertEquals(self._assert_ant_move_history, self._ant_move_history)

    def _record_ant_moves(self, terminal, actions_done):
        collections = terminal.get_synergy_manager().get_simulations()[0].get_collections()
        for collection in collections:
            if isinstance(collection, Colony):
                ant = collection.get_objects()[0]
                self.assertIsInstance(ant, Ant)
                self._ant_move_history.append(ant.get_position())
