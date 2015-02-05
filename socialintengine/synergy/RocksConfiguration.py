from synergine.synergy.collection.Configuration import Configuration
from socialintengine.synergy.object.Rock import Rock
from synergine.metas import metas
from socialintengine.cst import IMPENETRABLE
from synergine.synergy.Simulation import Simulation


class RocksConfiguration(Configuration):

    def get_start_objects(self):

      rocks = []

      for i in range(20):
          rock = Rock()
          metas.list.add(Simulation.STATE, rock.get_id(), IMPENETRABLE)
          rock.add_trace((0, 10+i, 15))
          rocks.append(rock)

      for i in range(20):
          rock = Rock()
          rock.add_trace((0, 10+i, 25))
          metas.list.add(Simulation.STATE, rock.get_id(), IMPENETRABLE)
          rocks.append(rock)

      return rocks