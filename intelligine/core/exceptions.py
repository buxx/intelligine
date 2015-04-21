from synergine.synergy.event.exception.ActionAborted import ActionException


class MovementException(Exception):
    pass


class SamePosition(MovementException):
    pass


class UnableToFoundMovement(MovementException):
    pass


class PheromoneException(Exception):
    pass


class NoPheromone(PheromoneException):
    pass


class NoPheromoneMove(PheromoneException, MovementException):
    pass


class NoTypeInPheromone(NoPheromone):
    pass


class NoCategoryInPheromone(NoPheromone):
    pass


class BestPheromoneHere(PheromoneException):

    def __init__(self, best_distance,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._best_distance = best_distance

    def get_best_distance(self):
        return self._best_distance

class PheromoneGlandDisabled(PheromoneException):
    pass


class BrainException(Exception):
    pass


class BrainPartAlreadyExist(BrainException):
    pass


class BodyException(Exception):
    pass


class BodyPartAlreadyExist(BodyException):
    pass


class DirectionException(Exception):
    pass


class NearException(Exception):
    pass


class NearFound(NearException):
    pass


class NearNothingFound(NearException):
    pass


class CantFindWhereToPut(ActionException):
    pass