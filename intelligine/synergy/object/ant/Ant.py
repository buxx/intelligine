from intelligine.synergy.object.Bug import Bug
from intelligine.cst import CARRYING, TRANSPORTER, ATTACKER, \
                            COL_TRANSPORTER, COL_TRANSPORTER_NOT_CARRYING, \
                            COL_FIGHTER, MOVE_MODE_EXPLO, MOVE_MODE_GOHOME, \
                            PHEROMON_DIR_EXPLO
from intelligine.synergy.object.Food import Food


class Ant(Bug):

    def __init__(self, collection, context):
        super().__init__(collection, context)
        context.metas.states.add_list(self.get_id(), [TRANSPORTER, ATTACKER])
        context.metas.collections.add_list(self.get_id(), [COL_TRANSPORTER,
                                                           COL_TRANSPORTER_NOT_CARRYING,
                                                           COL_FIGHTER])
        self._carried = []
        self._last_pheromones_points = {}
        self._movement_mode = MOVE_MODE_EXPLO

    def put_carry(self, obj, position=None):
        if position is None:
            position = self._get_position()
        self._carried.remove(obj)
        obj.set_position(position)
        self._context.metas.states.remove(self.get_id(), CARRYING)

    def get_carried(self):
        # TODO: cas ou plusieurs ?
        return self._carried[0]

    def carry(self, obj):
        self._carried.append(obj)
        self._context.metas.states.add(self.get_id(), CARRYING)
        # TODO: pour le moment hardcode
        if isinstance(obj, Food):
            self.set_movement_mode(MOVE_MODE_GOHOME)
            self.set_last_pheromone_point(PHEROMON_DIR_EXPLO, obj.get_position())

    def is_carrying(self):
        if len(self._carried):
            return True
        return False

    # TODO: Est-ce ici que doit etre ce code ?
    def set_position(self, position):
        super().set_position(position)
        if self.is_carrying():
            for obj_carried in self._carried:
                obj_carried.set_position(position)

    def get_last_pheromone_point(self, pheromone_name):
        if pheromone_name in self._last_pheromones_points:
            return self._last_pheromones_points[pheromone_name]
        return self._start_position

    def set_last_pheromone_point(self, pheromone_name, position):
        self._last_pheromones_points[pheromone_name] = position

    def get_movement_mode(self):
        return self._movement_mode

    def set_movement_mode(self, movement_mode):
        self._movement_mode = movement_mode