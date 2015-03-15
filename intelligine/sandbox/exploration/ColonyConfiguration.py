from intelligine.synergy.ColonyConfiguration import ColonyConfiguration
from intelligine.synergy.object.ant.Ant import Ant


class ColonyConfiguration(ColonyConfiguration):

    _start_position = (0, 5, 5)
    _ant_class = Ant
    _ant_count = 50

