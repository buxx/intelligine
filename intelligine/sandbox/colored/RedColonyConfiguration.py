from intelligine.synergy.ColonyConfiguration import ColonyConfiguration
from intelligine.sandbox.colored.RedAnt import RedAnt
from intelligine.synergy.object.ant.Egg import Egg
from intelligine.cst import COLONY, MOVE_MODE_NURSE


class RedColonyConfiguration(ColonyConfiguration):

    _start_position = (0, 20, 70)
    _ant_class = RedAnt
    _ant_count = 50

    def get_start_objects(self, collection, context):
        objects = super().get_start_objects(collection, context)

        for ant in objects:
            ant._brain.switch_to_mode(MOVE_MODE_NURSE)

        for x in range(50):
          for y in range(1, 50):
            if x % 3 == 0 and y % 3 == 0:
              egg = Egg(collection, context)
              egg.set_position((0, 1+x, 50+y))
              context.metas.value.set(COLONY, egg.get_id(), collection.get_id())
              objects.append(egg)

        return objects

