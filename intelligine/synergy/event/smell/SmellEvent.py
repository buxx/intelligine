from intelligine.cst import COL_SMELL
from intelligine.mechanism.TraversableDistanceFromMechanism import TraversableDistanceFromMechanism
from intelligine.synergy.event.Event import Event
from intelligine.cst import SMELL_FOOD, SMELL_EGG
from intelligine.synergy.object.StockedFood import StockedFood
from intelligine.synergy.object.ant.Egg import Egg
from synergine.core.exceptions import NotConcernedEvent


class SmellEvent(Event):

    _mechanism = TraversableDistanceFromMechanism
    _concern = COL_SMELL
    _each_cycle = 100
    _first_cycle_force = True

    def _prepare(self, object_id, context, parameters={}):
        if not parameters['points_distances']:
            raise NotConcernedEvent()

        return parameters
