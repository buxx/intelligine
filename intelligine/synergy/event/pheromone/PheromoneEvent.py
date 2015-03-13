from synergine.synergy.event.Event import Event
from intelligine.cst import COL_WALKER


class PheromoneEvent(Event):
    """
    TODO: dissipation des infos de pheromones:
          On doit manipuler l'environnement (pas des syn.obj.) car -= l'intensite d'un pt.
    """

    concern = COL_WALKER # Maybe more when more pheromones
    _each_cycle = 2

    def _object_match(self, object_id, context, parameters):
        return True