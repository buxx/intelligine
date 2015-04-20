from intelligine.core.exceptions import PheromoneException
from intelligine.synergy.object.Bug import Bug
from intelligine.cst import CARRYING, TRANSPORTER, ATTACKER, \
                            COL_TRANSPORTER, COL_TRANSPORTER_NOT_CARRYING, \
                            COL_FIGHTER, MOVE_MODE_EXPLO, MOVE_MODE_GOHOME, \
                            PHEROMON_DIR_EXPLO, LAST_PHERMONES_POINTS, CARRIED
from intelligine.synergy.object.Food import Food
from intelligine.simulation.object.pheromone.MovementPheromoneGland import MovementPheromoneGland
from intelligine.simulation.object.brain.AntBrain import AntBrain


class Ant(Bug):

    def __init__(self, collection, context):
        super().__init__(collection, context)
        context.metas.states.add_list(self.get_id(), [TRANSPORTER, ATTACKER])
        context.metas.collections.add_list(self.get_id(), [COL_TRANSPORTER,
                                                           COL_TRANSPORTER_NOT_CARRYING,
                                                           COL_FIGHTER])
        self._carried = []
        self._last_pheromones_points = {}
        # TODO: Faire un body_part schema pour ces trucs la
        self._movement_pheromone_gland = MovementPheromoneGland(self, self._context)
        self._brain.switch_to_mode(MOVE_MODE_EXPLO)

    def _get_brain_instance(self):
        return AntBrain(self._context, self)

    def get_movement_pheromone_gland(self):
        return self._movement_pheromone_gland

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
        #  TODO: On gere une liste de carried (mais pas juste la dessous). Ne gerer qu'un objet carried ?
        self._context.metas.value.set(CARRIED, self.get_id(), obj.get_id())
        # TODO: pour le moment hardcode
        if isinstance(obj, Food):
            self.get_brain().switch_to_mode(MOVE_MODE_GOHOME)
            self.set_last_pheromone_point(PHEROMON_DIR_EXPLO, obj.get_position())
            self.get_movement_pheromone_gland().appose()

    def is_carrying(self):
        if len(self._carried):
            return True
        return False

    # TODO: Est-ce ici que doit etre ce code ?
    def set_position(self, position):
        if self._position is not None and position != self._position:
            self._brain.host_moved()
        super().set_position(position)
        if self.is_carrying():
            for obj_carried in self._carried:
                obj_carried.set_position(position)

    # TODO: N'est plus utiliser ! delete it !
    def get_last_pheromone_point(self, pheromone_name):
        if pheromone_name in self._last_pheromones_points:
            return self._last_pheromones_points[pheromone_name]
        return self._start_position

    def set_last_pheromone_point(self, pheromone_name, position):
        self._last_pheromones_points[pheromone_name] = position
        self._context.metas.value.set(LAST_PHERMONES_POINTS, self.get_id(), self._last_pheromones_points)

    def initialize(self):
        super().initialize()
        if self.get_movement_pheromone_gland().is_enabled():
            try:
                self.get_movement_pheromone_gland().appose()
            except PheromoneException:
                pass

    def get_colony(self):
        return self.get_collection()