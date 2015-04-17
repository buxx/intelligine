from intelligine.simulation.object.brain.part.move.MoveBrainPart import MoveBrainPart
from xyzworld.cst import POSITION
from intelligine.core.exceptions import NoPheromone
from intelligine.cst import PHEROMONE_SEARCHING, MOVE_MODE_EXPLO, COL_TRANSPORTER_NOT_CARRYING, COL_TRANSPORTER_CARRYING
from intelligine.simulation.pheromone.DirectionPheromone import DirectionPheromone


class AntMoveBrainPart(MoveBrainPart):

    @classmethod
    def get_direction(cls, context, object_id):
        try:
            return cls._get_direction_with_pheromones(context, object_id)
        except NoPheromone:
            return super().get_direction(context, object_id)

    @classmethod
    def _get_direction_with_pheromones(cls, context, object_id):
        object_point = context.metas.value.get(POSITION, object_id)
        pheromone_type = context.metas.value.get(PHEROMONE_SEARCHING, object_id)
        try:
            direction = cls._get_pheromone_direction_for_point(context, object_point, pheromone_type)
        except NoPheromone:
            try:
                direction = cls._get_direction_of_pheromone(context, object_point, pheromone_type)
            except NoPheromone:
                raise
        return direction

    @staticmethod
    def _get_pheromone_direction_for_point(context, point, pheromone_type):
        return DirectionPheromone.get_direction_for_point(context, point, pheromone_type)

    @staticmethod
    def _get_direction_of_pheromone(context, point, pheromone_type):
        search_pheromone_in_points = context.get_around_points_of(point, distance=1)
        try:
            best_pheromone_direction = DirectionPheromone.get_best_pheromone_direction_in(context,
                                                                                          point,
                                                                                          search_pheromone_in_points,
                                                                                          pheromone_type)
            return best_pheromone_direction
        except NoPheromone as err:
            raise err

    def done(self, obj, context):
        super().done(obj, context)
        self._appose_pheromone(obj)

        # # TEST: le temps de tout tester
        # if obj.get_position() == obj.get_colony().get_start_position() and obj.is_carrying():
        #     obj_transported = obj.get_carried()
        #     obj_transported.set_carried_by(None)
        #     obj.put_carry(obj_transported, (-1, 0, 0))
        #     obj.get_brain().switch_to_mode(MOVE_MODE_EXPLO)
        #     context.metas.collections.add_remove(obj.get_id(),
        #                                          COL_TRANSPORTER_NOT_CARRYING,
        #                                          COL_TRANSPORTER_CARRYING)

    @staticmethod
    def _appose_pheromone(obj):
        obj.get_movement_pheromone_gland().appose()

