from intelligine.synergy.ColonyConfiguration import ColonyConfiguration
from intelligine.synergy.object.ant.Ant import Ant


class ColonyConfiguration(ColonyConfiguration):

    _start_position = (0, 20, 20)
    _ant_class = Ant
    _ant_count = 2


