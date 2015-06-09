from intelligine.core.exceptions import BodyPartAlreadyExist
from intelligine.synergy.object.Transportable import Transportable
from intelligine.cst import ALIVE, ATTACKABLE, COL_ALIVE
from intelligine.simulation.object.brain.Brain import Brain


class BaseBug(Transportable):

    _body_parts = {}

    def __init__(self, collection, context):
        super().__init__(collection, context)
        context.metas.states.add_list(self.get_id(), [ALIVE, ATTACKABLE])
        context.metas.collections.add(self.get_id(), COL_ALIVE)
        context.metas.value.set(COLONY, self.get_id(), collection.get_id())
        self._life_points = 10
        self._movements_count = -1
        self._brain = self._get_brain_instance()
        self._parts = {}
        self._init_parts()

    def _init_parts(self):
        for body_part_name in self._body_parts:
            self._set_body_part(body_part_name, self._body_parts[body_part_name](self, self._context))

    def _set_body_part(self, name, body_part, replace=False):
        if name in self._parts and not replace:
            raise BodyPartAlreadyExist()
        self._parts[name] = body_part

    def get_body_part(self, name):
        return self._parts[name]

    def hurted(self, points):
        self._life_points -= points

    def get_life_points(self):
        return self._life_points

    def set_position(self, point):
        super().set_position(point)
        self._movements_count += 1

    def get_movements_count(self):
        return self._movements_count

    def _get_brain_instance(self):
        return Brain(self._context, self)

    def get_brain(self):
        return self._brain

    def die(self):
        # TODO: Ca peut buger si pas , allow_not_in=True, pk ?
        self._remove_state(ALIVE, allow_not_in=True)
        self._remove_state(ATTACKABLE, allow_not_in=True)
        self._remove_col(COL_ALIVE, allow_not_in=True)
