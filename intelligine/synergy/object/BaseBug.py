from intelligine.core.exceptions import BodyPartAlreadyExist
from intelligine.synergy.object.Transportable import Transportable
from intelligine.cst import COL_ALIVE, COLONY, ACTION_DIE, BRAIN
from intelligine.simulation.object.brain.Brain import Brain
from intelligine.cst import ALIVE, ATTACKABLE
from synergine.core.Signals import Signals


class BaseBug(Transportable):

    _body_parts = {}
    _brain_class = Brain

    def __init__(self, collection, context):
        super().__init__(collection, context)
        context.metas.states.add_list(self.get_id(), [ALIVE, ATTACKABLE])
        context.metas.collections.add(self.get_id(), COL_ALIVE)
        context.metas.value.set(COLONY, self.get_id(), collection.get_id())
        self._life_points = 10
        self._alive = True
        self._movements_count = -1
        self._brain = self._brain_class(self._context, self)
        self._context.metas.value.set(BRAIN, self.get_id(), self._brain_class)
        self._parts = {}
        self._init_parts()

    def die(self):
        self._set_alive(False)
        self._remove_state(ALIVE)
        self._remove_state(ATTACKABLE)
        self._remove_col(COL_ALIVE)

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
        if self.get_life_points() <= 0 and self.is_alive():
            self.die()
            Signals.signal(ACTION_DIE).send(obj=self, context=self._context)

    def is_alive(self):
        return self._alive

    def _set_alive(self, alive):
        self._alive = bool(alive)

    def get_life_points(self):
        return self._life_points

    def set_position(self, point):
        super().set_position(point)
        self._movements_count += 1

    def get_movements_count(self):
        return self._movements_count

    def get_brain(self):
        return self._brain
