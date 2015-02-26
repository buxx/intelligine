from intelligine.synergy.ColonyConfiguration import ColonyConfiguration
from intelligine.sandbox.colored.RedAnt import RedAnt
from intelligine.synergy.object.ant.Egg import Egg
from intelligine.cst import COLONY


class RedColonyConfiguration(ColonyConfiguration):

    _start_position = (0, 20, 70)
    _ant_class = RedAnt

    def get_start_objects(self, collection, context):
        objects = super().get_start_objects(collection, context)

        for x in range(50):
          for y in range(1, 50):
            if x % 3 == 0 and y % 3 == 0:
              egg = Egg(collection, context)
              egg.set_position((0, 1+x, 50+y))
              # TODO: Ce COLONY doit devenir un truc automatise au niveau de la collection (qd get_object)
              context.metas.value.set(COLONY, egg.get_id(), collection.get_id())
              objects.append(egg)

        return objects

