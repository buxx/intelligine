from intelligine.core.exceptions import BestPheromoneHere
from intelligine.simulation.pheromone.DirectionPheromone import DirectionPheromone
from intelligine.synergy.ColonyConfiguration import ColonyConfiguration
from intelligine.synergy.object.ant.Ant import Ant
from intelligine.cst import PHEROMON_DIR_HOME


class ColonyConfiguration(ColonyConfiguration):

    _start_position = (0, 5, 5)
    _ant_class = Ant
    _ant_count = 5
