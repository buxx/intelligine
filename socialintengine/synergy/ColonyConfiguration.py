from synergine.synergy.collection.Configuration import Configuration
from socialintengine.synergy.object.ant.Ant import Ant
from synergine.metas import metas
from socialintengine.cst import ALIVE
from synergine.synergy.Simulation import Simulation


class ColonyConfiguration(Configuration):

    def get_start_objects(self):

      ants = []
      for i in range(10):
          ant = Ant()
          ant.set_position((0, 20, 20))
          metas.list.add(Simulation.STATE, ant.get_id(), ALIVE)
          ants.append(ant)

      return ants