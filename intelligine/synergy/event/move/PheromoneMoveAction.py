from intelligine.synergy.event.move.MoveAction import MoveAction
from intelligine.cst import PHEROMONE_SEARCHING, MOVE_MODE_EXPLO
from intelligine.cst import COL_TRANSPORTER_NOT_CARRYING, COL_TRANSPORTER_CARRYING
from intelligine.core.exceptions import NoPheromone, BestPheromoneHere
from intelligine.simulation.pheromone.DirectionPheromone import DirectionPheromone


class PheromoneMoveAction(MoveAction):

    def _get_prepared_direction(self, context, object_point):
        try:
            return self._get_direction_with_pheromones(context, object_point)
        except NoPheromone:
            return super()._get_prepared_direction(context, object_point)

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

    def _apply_move(self, obj, context):
        super()._apply_move(obj, context)
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

    @staticmethod
    def _appose_pheromone(obj, context):
        # TODO: Cette action de pheromone doit etre une surcharge de Move afin d'avoir une Action Move generique.
        try:
            DirectionPheromone.appose(context,
                                      obj.get_position(),
                                      obj.get_movement_pheromone_gland().get_movement_molecules())
        except BestPheromoneHere as best_pheromone_here:
            obj.get_brain().set_distance_from_objective(best_pheromone_here.get_best_distance())


