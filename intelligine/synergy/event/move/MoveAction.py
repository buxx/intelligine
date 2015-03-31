from synergine.synergy.event.Action import Action
from intelligine.synergy.event.move.MoveEvent import MoveEvent
from random import randint, choice, randrange
from xyzworld.cst import POSITION, POSITIONS
from intelligine.cst import PREVIOUS_DIRECTION, BLOCKED_SINCE, MOVE_MODE, MOVE_MODE_GOHOME, MOVE_MODE_EXPLO, \
                            PHEROMON_DIR_EXPLO, PHEROMON_DIR_HOME, PHEROMON_DIRECTION, \
    COL_TRANSPORTER_NOT_CARRYING, COL_TRANSPORTER_CARRYING
from intelligine.synergy.event.move.direction import directions_same_level, directions_modifiers, directions_slighty
from intelligine.core.exceptions import NoPheromoneMove, NoPheromone, BestPheromoneHere
import operator
from intelligine.simulation.pheromone.DirectionPheromone import DirectionPheromone
from xyzworld.geometry import get_degree_from_north
from intelligine.synergy.event.move.direction import get_direction_for_degrees, directions_opposites


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

        move_to_point = self._get_point_for_direction(object_point, direction)
        if self._direction_point_is_possible(context, move_to_point):
            self._move_to_point = move_to_point
            self._move_to_direction = direction
        else:
            # TODO: mettre self._dont_move = True ?
            pass

    def _get_direction_with_pheromones(self, context, object_point):
        # TODO: Placer directnement pheromone type dans les metas
        object_movement_mode = context.metas.value.get(MOVE_MODE, self._object_id)
        pheromone_type = DirectionPheromone.get_pheromone_type_for_move_mode(object_movement_mode)
        try:
            direction = self._get_pheromone_direction_for_point(context, object_point, pheromone_type)
        except NoPheromone:
            direction = self._get_direction_of_pheromone(context, object_point, pheromone_type)
        return direction

    @staticmethod
    def _get_pheromone_direction_for_point(context, point, pheromone_type):
        return DirectionPheromone.get_direction_for_point(context, point, pheromone_type)

    @staticmethod
    def _get_direction_of_pheromone(context, point, pheromone_type):
        search_pheromone_distance = 1  # TODO: config
        search_pheromone_in_points = context.get_arround_points_of(point, distance=search_pheromone_distance)
        try:
            # TODO: ? Avoir plutot un DirectionPheromone.get_best_pheromone_direction_in ?
            best_pheromone_direction = DirectionPheromone.get_best_pheromone_direction_in(context,
                                                                                          point,
                                                                                          search_pheromone_in_points,
                                                                                          pheromone_type)
            return best_pheromone_direction
        except NoPheromone as err:
            raise err

    # def _get_random_direction_point(self, context, reference_point):
    #     z, x, y = reference_point
    #     direction_name = self._get_random_direction_name(context)
    #     directions_modifier = directions_modifiers[direction_name]
    #     new_position = (z + directions_modifier[0], x + directions_modifier[1], y + directions_modifier[2])
    #     return (direction_name, new_position)

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
    def _get_point_for_direction(reference_point, direction):
        # TODO: mettre une fonction cote direction.py pour appliquer le modifier.
        z, x, y = reference_point
        directions_modifier = directions_modifiers[direction]
        return z + directions_modifier[0], x + directions_modifier[1], y + directions_modifier[2]

    @staticmethod
    def _direction_point_is_possible(context, direction_point):
        return context.position_is_penetrable(direction_point)

    def run(self, obj, context, synergy_manager):
        if self._move_to_point is not None and self._move_to_direction != 14: # TODO: il ne faut pas choisir une direction 14.
            obj.set_position(self._move_to_point)
            #direction_from = directions_opposites[self._move_to_direction]
            #obj.set_direction_from(direction_from)
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
                    COL_TRANSPORTER_NOT_CARRYING, COL_TRANSPORTER_CARRYING)

            # TMP: Devra etre un event et une action
            # if self._move_to_point == (0, 5, 5):  # position de depart
            #     if len(obj._carried):
            #         obj_transported = obj.get_carried()
            #         obj_transported.set_carried_by(None)
            #         obj.put_carry(obj_transported, (-1, 5, 5))
            #         context.metas.collections.add_remove(obj.get_id(), COL_TRANSPORTER_NOT_CARRYING, COL_TRANSPORTER_CARRYING)
            #     obj.set_movement_mode(MOVE_MODE_EXPLO)


        else:
            try:
                blocked_since = context.metas.value.get(BLOCKED_SINCE, self._object_id)
            except:
                blocked_since = 0
            context.metas.value.set(BLOCKED_SINCE, self._object_id, blocked_since+1)

    # def _get_pheromone_direction_point(self, context, object_point):
    #     try:
    #         blocked_since = context.metas.value.get(BLOCKED_SINCE, self._object_id)
    #     except KeyError:
    #         blocked_since = 0
    #     if blocked_since > 3:
    #         raise NoPheromoneMove()
    #     # Si on explore, on cherche pheromone d'explo
    #     # si on rentre a home, on cherche pheromone d'home...
    #     # TODO: code arrache
    #     object_movement_mode = context.metas.value.get(MOVE_MODE, self._object_id)
    #     if object_movement_mode == MOVE_MODE_EXPLO:
    #         pheromone_direction_type = PHEROMON_DIR_EXPLO
    #     elif object_movement_mode == MOVE_MODE_GOHOME:
    #         pheromone_direction_type = PHEROMON_DIR_HOME
    #
    #     sniff_points = context.get_arround_points_of(object_point, distance=0)
    #     # Faire un compile des infos de pheromones
    #
    #     directions = {}
    #     for sniff_point in sniff_points:
    #         info = context.pheromones().get_info(sniff_point,
    #                                              [PHEROMON_DIRECTION, pheromone_direction_type],
    #                                              allow_empty=True,
    #                                              empty_value={})
    #         for direction in info:
    #             if direction not in directions:
    #                 directions[direction] = info[direction]
    #             else:
    #                 directions[direction] += info[direction]
    #     if len(directions):
    #         sorted_directions = sorted(directions.items(), key=operator.itemgetter(1))
    #         sorted_directions.reverse()
    #         #best_direction_name = sorted_directions[0][0]
    #         best_direction_level = sorted_directions[0][1]
    #         best_direction_names = [direction for direction in directions \
    #                                if directions[direction] == best_direction_level]
    #         # Si plusieurs best directions, choisir mm direction que la precedente
    #         # si y a pas, au hasard.
    #         last_dir_name = context.metas.value.get(PREVIOUS_DIRECTION, self._object_id)
    #         if last_dir_name in best_direction_names:
    #             direction_name = last_dir_name
    #         else:
    #             direction_name = choice(best_direction_names)
    #
    #         # DRY
    #         z, x, y = object_point
    #         directions_modifier = directions_modifiers[direction_name]
    #         new_position = (z + directions_modifier[0], x + directions_modifier[1], y + directions_modifier[2])
    #         return (direction_name, new_position)
    #
    #         pass
    #     raise NoPheromoneMove()

    def _appose_pheromone(self, obj, context):
        # TODO: Cette action de pheromone doit etre une surcharge de Move afin d'avoir une Action Move generique.
        obj.get_brain().host_moved()
        try:
            DirectionPheromone.appose(context,
                                      obj.get_position(),
                                      obj.get_movement_pheromone_gland().get_movement_molecules())
        except BestPheromoneHere as best_pheromone_here:
            obj.get_brain().set_distance_from_objective(best_pheromone_here.get_best_distance())
