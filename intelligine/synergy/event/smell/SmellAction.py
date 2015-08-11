from intelligine.core.exceptions import BestMoleculeHere
from intelligine.cst import POINT_SMELL, POINTS_SMELL, MOLECULES_INFOS, MOLECULES_DIRECTION, SMELL_FOOD, SMELL_EGG
from intelligine.simulation.molecule.DirectionMolecule import DirectionMolecule
from intelligine.simulation.molecule.Molecule import Molecule
from intelligine.synergy.event.smell.SmellEvent import SmellEvent
from synergine.synergy.event.Action import Action


class SmellAction(Action):

    _listen = SmellEvent

    @classmethod
    def cycle_pre_run(cls, context, synergy_manager):
        smell_positions = context.metas.list.get(POINTS_SMELL, POINTS_SMELL, allow_empty=True)
        for smell_position in smell_positions:
            # TODO: Remonter ca dans MoleculeManager ?
            flavour_raw_data = context.metas.value.get(MOLECULES_INFOS, smell_position)
            # TODO: Calculer ou definir qqpart la liste des smells
            for smell_type in (SMELL_FOOD, SMELL_EGG):
                if smell_type in flavour_raw_data:
                    del(flavour_raw_data[smell_type])
                context.metas.value.set(MOLECULES_INFOS, smell_position, flavour_raw_data)
        context.metas.list.unset(POINTS_SMELL, POINTS_SMELL, allow_empty=True)

    def run(self, obj, context, synergy_manager):

        points_distances = self._parameters['points_distances']
        smell_type = obj.get_smell()

        for smell_point in points_distances:
            distance = points_distances[smell_point]
            molecule = Molecule(MOLECULES_DIRECTION, smell_type, distance)

            try:
                DirectionMolecule.appose(context, smell_point, molecule)
            except BestMoleculeHere:
                pass  #

            #
            # current_point_smell = points_distances[smell_point]
            # where_to_put_smells = context.metas.value.get(POINT_SMELL, smell_point, allow_empty=True, empty_value={})
            #
            #
            # if smell_type not in where_to_put_smells:
            #     where_to_put_smells[smell_type] = current_point_smell
            # else:
            #     where_to_put_smell = where_to_put_smells[smell_type]
            #     if current_point_smell < where_to_put_smell:
            #         where_to_put_smells[smell_type] = where_to_put_smell
            #
            # context.metas.value.set(POINT_SMELL, smell_point, where_to_put_smells)
            # context.metas.list.add(POINTS_SMELL, POINTS_SMELL, smell_point, assert_not_in=False)
