from synergine.synergy.collection.Configuration import Configuration
from intelligine.synergy.object.ant.Ant import Ant
from synergine.metas import metas
from intelligine.cst import ALIVE, COLONY


class ColonyConfiguration(Configuration):

    _start_position = (0, 20, 20)
    _ant_class = Ant

    def get_start_objects(self, collection):

      ants = []
      for i in range(20):
          ant = self._ant_class()
          metas.value.set(COLONY, ant.get_id(), collection.get_id())
          ant.set_position(self._start_position)
          ants.append(ant)

      return ants