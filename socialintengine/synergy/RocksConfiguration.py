from synergine.synergy.collection.Configuration import Configuration
from socialintengine.synergy.object.Rock import Rock
from synergine.metas import metas
from socialintengine.cst import IMPENETRABLE
from synergine.synergy.Simulation import Simulation


class RocksConfiguration(Configuration):

    def get_start_objects(self):

      rocks = []

      for i in range(50):
          rock = Rock()
          metas.list.add(Simulation.STATE, rock.get_id(), IMPENETRABLE)
          rock.set_position((0, 0+i, 0))
          rocks.append(rock)

      for i in range(50):
          rock = Rock()
          metas.list.add(Simulation.STATE, rock.get_id(), IMPENETRABLE)
          rock.set_position((0, 0+i, 50))
          rocks.append(rock)

      for i in range(50):
          rock = Rock()
          rock.set_position((0, 0, 0+i))
          metas.list.add(Simulation.STATE, rock.get_id(), IMPENETRABLE)
          rocks.append(rock)

      for i in range(50):
          rock = Rock()
          rock.set_position((0, 50, 0+i))
          metas.list.add(Simulation.STATE, rock.get_id(), IMPENETRABLE)
          rocks.append(rock)

      rock = Rock()
      rock.set_position((0, 50, 50))
      metas.list.add(Simulation.STATE, rock.get_id(), IMPENETRABLE)
      rocks.append(rock)

      return rocks