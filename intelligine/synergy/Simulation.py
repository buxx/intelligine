from intelligine.simulation.molecule.Evaporation import Evaporation
from synergine.core.Core import Core
from synergine.synergy.Simulation import Simulation as BaseSimulation
from synergine_xyz.cst import POSITIONS


class Simulation(BaseSimulation):

    _smells = []

    @classmethod
    def add_smell(cls, smell):
        if smell not in cls._smells:
            cls._smells.append(smell)

    @classmethod
    def get_smells(cls):
        return cls._smells

    def end_cycle(self, context):
        clean_each_cycle = Core.get_configuration_manager().get('engine.clean_each_cycle', 100)
        evaporate_each_cycle = Core.get_configuration_manager().get('stigmergy.molecule.evaporate_each_cycle', 100)

        if context.get_cycle() % clean_each_cycle is 0:
            context.metas.list.clean(POSITIONS)

        if context.get_cycle() % evaporate_each_cycle is 0:
            self._evaporate(context)

    def _evaporate(self, context):
        evaporation_increment = Core.get_configuration_manager().get('stigmergy.molecule.evaporate_decrement', 5)
        evaporation_min_age = Core.get_configuration_manager().get('stigmergy.molecule.evaporate_min_age', 100)
        evaporation = Evaporation(context,
                                  evaporation_increment,
                                  molecules_exclude_types=self.get_smells(),
                                  molecule_minimum_age=evaporation_min_age)
        evaporation.evaporate()
