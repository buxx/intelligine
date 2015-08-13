from intelligine.cst import COL_SMELL, CARRIED_BY
from intelligine.mechanism.TraversableDistanceFromMechanism import TraversableDistanceFromMechanism
from intelligine.synergy.event.Event import Event
from synergine.core.exceptions import NotConcernedEvent


class SmellEvent(Event):

    _mechanism = TraversableDistanceFromMechanism
    _concern = COL_SMELL
    _each_cycle = 100
    _first_cycle_force = True

    def _prepare(self, object_id, context, parameters={}):
        if not parameters['points_distances'] or not self._concerned_object(context, object_id):
            raise NotConcernedEvent()

        return parameters

    def _concerned_object(self, context, object_id):
        # TODO: Un peu hardcodé etant donné que cet event concerne tout les COL_SMELL et pas que les transportable ...
        return not context.metas.value.get(CARRIED_BY, object_id, allow_empty=True, empty_value=False)
