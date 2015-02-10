from synergine.synergy.Simulation import Simulation as BaseSimulation
from xyzworld.cst import POSITION, POSITIONS


class Simulation(BaseSimulation):

    def end_cycle(self, context):
        if context.get_cycle() % 100 is 0:
            context.metas.list.clean(POSITIONS)
