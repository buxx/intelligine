from synergine.synergy.event.Action import Action
from intelligine.synergy.event.move.MoveEvent import MoveEvent
from random import randint, choice, randrange
from xyzworld.cst import POSITION
from intelligine.cst import PREVIOUS_DIRECTION, BLOCKED_SINCE, MOVE_MODE, MOVE_MODE_EXPLO, PHEROMONE_SEARCHING
from intelligine.cst import COL_TRANSPORTER_NOT_CARRYING, COL_TRANSPORTER_CARRYING
from intelligine.synergy.event.move.direction import directions_same_level, directions_modifiers, directions_slighty
from intelligine.synergy.event.move.direction import get_position_with_direction_decal
from intelligine.core.exceptions import NoPheromone, BestPheromoneHere
from intelligine.simulation.pheromone.DirectionPheromone import DirectionPheromone


class MoveAction(Action):

    _listen = MoveEvent

    def __init__(self, object_id, parameters):
        super().__init__(object_id, parameters)
        self._move_to_point = None
        self._move_to_direction = None

    def prepare(self, context):
        object_point = context.metas.value.get(POSITION, self._object_id)

        try:
            direction = self._get_direction_with_pheromones(context, object_point)
        except NoPheromone:
            direction = self._get_random_direction(context)

        move_to_point = get_position_with_direction_decal(direction, object_point)
        if self._direction_point_is_possible(context, move_to_point):
            self._move_to_point = move_to_point
            self._move_to_direction = direction
        else:
            # TODO: mettre self._dont_move = True ?
            pass

    def _get_direction_with_pheromones(self, context, object_point):
        pheromone_type = context.metas.value.get(PHEROMONE_SEARCHING, self._object_id)
        try:
            direction = self._get_pheromone_direction_for_point(context, object_point, pheromone_type)
        except NoPheromone:
            try:
                direction = self._get_direction_of_pheromone(context, object_point, pheromone_type)
            except NoPheromone:
                raise
        return direction

    @staticmethod
    def _get_pheromone_direction_for_point(context, point, pheromone_type):
        return DirectionPheromone.get_direction_for_point(context, point, pheromone_type)

    @staticmethod
    def _get_direction_of_pheromone(context, point, pheromone_type):
        search_pheromone_in_points = context.get_arround_points_of(point, distance=1)
        try:
            best_pheromone_direction = DirectionPheromone.get_best_pheromone_direction_in(context,
                                                                                          point,
                                                                                          search_pheromone_in_points,
                                                                                          pheromone_type)
            return best_pheromone_direction
        except NoPheromone as err:
            raise err

    def _get_random_direction(self, context):
        try:
            blocked_since = context.metas.value.get(BLOCKED_SINCE, self._object_id)
        except KeyError:
            blocked_since = 0
        direction_name = None
        if blocked_since <= 3:  #TODO: config
            try:
                previous_direction = context.metas.value.get(PREVIOUS_DIRECTION, self._object_id)
                # TODO: Faut mettre ca en plus propre (proba d'aller tou droit, config, etc)
                if randrange(100) < 75:  # 75% de change d'aller tout droit
                    # Dans le futur: les fourmis vont moins tout droit quand elle se croient et se touche
                    return previous_direction

                directions_list = directions_slighty[previous_direction]
                # TODO: TMP tant que 1 niveau (z)
                directions_list = [direction for direction in directions_list if direction > 9 and direction < 19]
                direction_name = choice(directions_list)
            except KeyError:
                pass

        if not direction_name:
            direction_name = randint(directions_same_level[0], directions_same_level[1])

        return direction_name

    @staticmethod
    def _direction_point_is_possible(context, direction_point):
        return context.position_is_penetrable(direction_point)

    def run(self, obj, context, synergy_manager):
        if self._move_to_point is not None and self._move_to_direction != 14: # TODO: il ne faut pas choisir une direction 14.
            obj.set_position(self._move_to_point)
            context.metas.value.set(PREVIOUS_DIRECTION, self._object_id, self._move_to_direction)
            context.metas.value.set(BLOCKED_SINCE, self._object_id, 0)
            self._appose_pheromone(obj, context)

            # TEST: le temps de tout tester
            if self._move_to_point == obj.get_colony().get_start_position() and obj.is_carrying():
                obj_transported = obj.get_carried()
                obj_transported.set_carried_by(None)
                obj.put_carry(obj_transported, (-1, 0, 0))
                obj.get_brain().switch_to_mode(MOVE_MODE_EXPLO)
                context.metas.collections.add_remove(obj.get_id(),
                                                     COL_TRANSPORTER_NOT_CARRYING,
                                                     COL_TRANSPORTER_CARRYING)
        else:
            try:
                blocked_since = context.metas.value.get(BLOCKED_SINCE, self._object_id)
            except:
                blocked_since = 0
            context.metas.value.set(BLOCKED_SINCE, self._object_id, blocked_since+1)

    @staticmethod
    def _appose_pheromone(obj, context):
        # TODO: Cette action de pheromone doit etre une surcharge de Move afin d'avoir une Action Move generique.
        obj.get_brain().host_moved()  # TODO: Auto quand set_position ? (test iit)
        try:
            DirectionPheromone.appose(context,
                                      obj.get_position(),
                                      obj.get_movement_pheromone_gland().get_movement_molecules())
        except BestPheromoneHere as best_pheromone_here:
            obj.get_brain().set_distance_from_objective(best_pheromone_here.get_best_distance())
