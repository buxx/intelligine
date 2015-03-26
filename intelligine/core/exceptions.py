class MovementException(Exception):
    pass


class SamePosition(MovementException):
    pass


class PheromoneException(Exception):
    pass


class NoPheromone(PheromoneException):
    pass


class NoPheromoneMove(PheromoneException, MovementException):
    pass


class BestPheromoneHere(PheromoneException):

    def __init__(self, best_distance,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._best_distance = best_distance

    def get_best_distance(self):
        return self._best_distance