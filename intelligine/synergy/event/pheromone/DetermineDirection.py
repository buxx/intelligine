from synergine.synergy.event.Action import Action
from intelligine.synergy.event.mind.PheromoneEvent import PheromoneEvent


class DetermineDirection(Action):

    _listen = PheromoneEvent

    def prepare(self, context):
        """
        Recupere chaque coordonnees de points qui doivent etre update
        pour ne pas avoir a e calculer dans le run
        :param context:
        :return:
        """
        pass

    def run(self, obj, context, synergy_manager):
        """
        Met a jour la direction en cours de l'ant
        :param obj:
        :param context:
        :param synergy_manager:
        :return:
        """
        pass
