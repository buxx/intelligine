from intelligine.synergy.Colony import Colony
from intelligine.synergy.object.ant.Ant import Ant
from intelligine.tests.src.simulation.SimpleTestWorld1Simulation import SimpleTestWorld1Simulation


class TestByPass(SimpleTestWorld1Simulation):

    _ant_move_history = []
    _assert_ant_move_history = [(0, 21, 20), (0, 20, 19), (0, 20, 19), (0, 20, 19), (0, 20, 19), (0, 20, 19), (0, 20, 19), (0, 21, 20), (0, 21, 20), (0, 21, 20), (0, 21, 20), (0, 21, 20), (0, 21, 19), (0, 21, 18), (0, 21, 17), (0, 21, 16), (0, 21, 16), (0, 21, 15), (0, 21, 14), (0, 22, 13), (0, 23, 13), (0, 24, 13), (0, 24, 13), (0, 24, 13), (0, 24, 13), (0, 24, 13), (0, 24, 13), (0, 23, 14), (0, 22, 15), (0, 21, 16), (0, 21, 16), (0, 21, 16), (0, 21, 16), (0, 21, 16), (0, 21, 15), (0, 21, 14), (0, 21, 13), (0, 21, 12), (0, 21, 11), (0, 21, 10), (0, 21, 9), (0, 21, 8), (0, 21, 7), (0, 21, 6), (0, 21, 5), (0, 21, 4), (0, 21, 3), (0, 21, 2), (0, 22, 1), (0, 22, 1), (0, 22, 1), (0, 22, 1), (0, 22, 1), (0, 22, 1), (0, 21, 1), (0, 20, 1), (0, 19, 1), (0, 18, 1), (0, 17, 1), (0, 16, 1), (0, 15, 1), (0, 14, 1), (0, 13, 1), (0, 12, 1), (0, 11, 1), (0, 10, 1), (0, 9, 1), (0, 8, 1), (0, 7, 2), (0, 6, 2), (0, 7, 3), (0, 8, 4), (0, 9, 5), (0, 10, 6), (0, 11, 7), (0, 12, 7), (0, 13, 7), (0, 14, 7), (0, 13, 7), (0, 12, 7), (0, 11, 7), (0, 11, 8), (0, 11, 9), (0, 11, 10), (0, 11, 9), (0, 11, 8), (0, 11, 7), (0, 12, 7), (0, 13, 7), (0, 14, 7), (0, 15, 7), (0, 16, 7), (0, 17, 7), (0, 18, 7), (0, 19, 7), (0, 20, 7), (0, 21, 7), (0, 21, 8), (0, 21, 9), (0, 21, 10), (0, 21, 11), (0, 21, 12), (0, 21, 13), (0, 21, 14), (0, 21, 15), (0, 21, 16), (0, 21, 17), (0, 21, 18), (0, 21, 19), (0, 20, 20), (0, 19, 21), (0, 19, 22), (0, 18, 23), (0, 17, 24), (0, 16, 25), (0, 16, 25), (0, 16, 25), (0, 16, 25), (0, 16, 25), (0, 16, 25), (0, 17, 25), (0, 18, 25), (0, 19, 25), (0, 19, 25), (0, 19, 25), (0, 19, 25), (0, 19, 25), (0, 19, 25), (0, 18, 25), (0, 17, 26), (0, 17, 26), (0, 17, 26), (0, 17, 26), (0, 17, 26), (0, 17, 26), (0, 18, 26), (0, 19, 26), (0, 19, 26), (0, 19, 26), (0, 19, 26), (0, 19, 26), (0, 18, 25), (0, 17, 24), (0, 17, 24), (0, 16, 24), (0, 16, 24), (0, 16, 24), (0, 16, 24), (0, 16, 24), (0, 16, 25), (0, 16, 26), (0, 16, 26), (0, 16, 26), (0, 16, 26), (0, 16, 26), (0, 16, 25), (0, 17, 24), (0, 18, 23), (0, 18, 23), (0, 19, 22), (0, 20, 21), (0, 21, 20), (0, 21, 20), (0, 21, 20), (0, 21, 20), (0, 21, 20), (0, 21, 20), (0, 21, 20), (0, 21, 20), (0, 21, 20), (0, 21, 19), (0, 21, 18), (0, 21, 17), (0, 21, 16), (0, 21, 15), (0, 21, 14), (0, 21, 13), (0, 21, 12), (0, 21, 11), (0, 21, 10), (0, 21, 9), (0, 21, 8), (0, 20, 7), (0, 19, 7), (0, 18, 7), (0, 17, 7), (0, 16, 7), (0, 15, 7), (0, 14, 7), (0, 13, 7), (0, 12, 7), (0, 11, 7), (0, 10, 6), (0, 9, 5), (0, 8, 4), (0, 7, 3), (0, 6, 2), (0, 5, 1), (0, 6, 2), (0, 7, 3), (0, 8, 4), (0, 9, 5), (0, 10, 6), (0, 11, 7), (0, 12, 7), (0, 13, 7), (0, 14, 7), (0, 13, 7), (0, 12, 7), (0, 11, 7), (0, 11, 8), (0, 11, 9), (0, 11, 10), (0, 11, 9), (0, 11, 8), (0, 11, 7), (0, 12, 7), (0, 13, 7), (0, 14, 7), (0, 15, 7), (0, 16, 7), (0, 17, 7), (0, 18, 7), (0, 19, 7), (0, 20, 7), (0, 21, 7), (0, 21, 8), (0, 21, 9), (0, 21, 10), (0, 21, 11), (0, 21, 12), (0, 21, 13), (0, 21, 14), (0, 21, 15), (0, 21, 16), (0, 21, 17), (0, 21, 18), (0, 21, 19), (0, 21, 20), (0, 20, 21), (0, 19, 22), (0, 18, 23), (0, 17, 24), (0, 16, 25), (0, 16, 25), (0, 16, 25), (0, 16, 25), (0, 16, 25), (0, 16, 24), (0, 16, 24), (0, 16, 24), (0, 16, 24), (0, 16, 24), (0, 16, 24), (0, 16, 24), (0, 16, 25), (0, 16, 26), (0, 16, 26), (0, 16, 26), (0, 16, 26), (0, 16, 26), (0, 16, 26), (0, 16, 26), (0, 16, 26), (0, 16, 26), (0, 16, 26), (0, 17, 26), (0, 18, 26), (0, 19, 26), (0, 19, 26), (0, 19, 26), (0, 19, 26), (0, 19, 26), (0, 19, 25), (0, 19, 24), (0, 19, 24), (0, 19, 24), (0, 19, 24), (0, 18, 23), (0, 18, 23), (0, 18, 23), (0, 18, 22), (0, 18, 21), (0, 18, 21), (0, 18, 21), (0, 18, 21), (0, 18, 21), (0, 18, 21), (0, 19, 22), (0, 19, 22), (0, 19, 22), (0, 19, 22), (0, 19, 22), (0, 19, 22), (0, 20, 21), (0, 21, 21), (0, 21, 21), (0, 21, 21), (0, 21, 21), (0, 21, 21), (0, 20, 22)]

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
