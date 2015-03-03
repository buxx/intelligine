from xyzworld.Context import Context as XyzContext
from intelligine.cst import IMPENETRABLE
from xyzworld.cst import POSITIONS


class Context(XyzContext):

    def position_is_penetrable(self, position):
        objects_ids_on_this_point = self.metas.list.get(POSITIONS, position, allow_empty=True)
        for object_id_on_this_point in objects_ids_on_this_point:
          if self.metas.states.have(object_id_on_this_point, IMPENETRABLE):
            return False
        return True