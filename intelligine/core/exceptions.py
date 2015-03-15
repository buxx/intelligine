class MovementException(Exception):
    pass

class SamePosition(MovementException):
    pass

class PheromoneException(Exception):
    pass

class NoPheromoneMove(PheromoneException, MovementException):
    pass