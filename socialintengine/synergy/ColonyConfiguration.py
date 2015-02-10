from synergine.synergy.collection.Configuration import Configuration
from socialintengine.synergy.object.ant.Ant import Ant
from synergine.metas import metas
from socialintengine.cst import ALIVE
from synergine.synergy.Simulation import Simulation


class ColonyConfiguration(Configuration):

    _start_position = (0, 20, 20)
    _ant_class = Ant

    def get_start_objects(self):

      ants = []
      for i in range(100):
          ant = self._ant_class()
          ant.set_position(self._start_position)
          metas.list.add(Simulation.STATE, ant.get_id(), ALIVE)
          ants.append(ant)

      return ants