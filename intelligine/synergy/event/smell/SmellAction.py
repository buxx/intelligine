from intelligine.core.exceptions import BestMoleculeHere
from intelligine.cst import POINT_SMELL, POINTS_SMELL, MOLECULES_INFOS, MOLECULES_DIRECTION, SMELL_FOOD, SMELL_EGG, \
    PHEROMON_DIR_EXPLO
from intelligine.simulation.molecule.DirectionMolecule import DirectionMolecule
from intelligine.simulation.molecule.Evaporation import Evaporation
from intelligine.simulation.molecule.Molecule import Molecule
from intelligine.synergy.event.move.MoveAction import MoveAction
from intelligine.synergy.event.smell.SmellEvent import SmellEvent
from synergine.synergy.event.Action import Action


class SmellAction(Action):

    _listen = SmellEvent
    _depend = [MoveAction]

    @classmethod
    def cycle_pre_run(cls, context, synergy_manager):
        evaporation = Evaporation(context, molecules_include_types=[SMELL_FOOD, SMELL_EGG])
        evaporation.remove()

    def run(self, obj, context, synergy_manager):

        points_distances = self._parameters['points_distances']
        smell_type = obj.get_smell()

        for smell_point in points_distances:
            distance = points_distances[smell_point]
            molecule = Molecule(MOLECULES_DIRECTION, smell_type, distance)

            try:
                DirectionMolecule.appose(context, smell_point, molecule)
            except BestMoleculeHere:
                pass
