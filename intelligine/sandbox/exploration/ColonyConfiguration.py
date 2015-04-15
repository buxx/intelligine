from intelligine.synergy.ColonyConfiguration import ColonyConfiguration
from intelligine.synergy.object.ant.Ant import Ant


class ColonyConfiguration(ColonyConfiguration):

    _start_position = (0, 1, 1)
    _ant_class = Ant
    _ant_count = 100
