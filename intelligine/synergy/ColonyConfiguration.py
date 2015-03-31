from synergine.synergy.collection.Configuration import Configuration
from intelligine.synergy.object.ant.Ant import Ant
from intelligine.cst import ALIVE, COLONY
from xyzworld.cst import POSITION


class ColonyConfiguration(Configuration):

    _start_position = (0, 20, 20)
    _ant_class = Ant
    _ant_count = 50

    @classmethod
    def get_start_position(cls):
        return cls._start_position

    def get_start_objects(self, collection, context):
      context.metas.value.set(POSITION, collection.get_id(), self._start_position)

      ants = []
      for i in range(self._ant_count):
          ant = self._ant_class(collection, context)
          context.metas.value.set(COLONY, ant.get_id(), collection.get_id())
          ant.set_position(self._start_position)
          ants.append(ant)

      return ants