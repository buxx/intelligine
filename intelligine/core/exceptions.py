from synergine.synergy.event.exception.ActionAborted import ActionException


class MovementException(Exception):
    pass


class SamePosition(MovementException):
    pass


class UnableToFoundMovement(MovementException):
    pass


class MoleculeException(Exception):
    pass


class NoMolecule(MoleculeException):
    pass


class NoMoleculeMove(MoleculeException, MovementException):
    pass


class NoTypeInMolecule(NoMolecule):
    pass


class NoCategoryInMolecule(NoMolecule):
    pass


class BestMoleculeHere(MoleculeException):

    def __init__(self, best_distance,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._best_distance = best_distance

    def get_best_distance(self):
        return self._best_distance

class MoleculeGlandDisabled(MoleculeException):
    pass


class BrainException(Exception):
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