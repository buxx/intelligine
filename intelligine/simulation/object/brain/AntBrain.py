from intelligine.simulation.object.brain.Brain import Brain
from intelligine.simulation.object.brain.part.move.AntMoveBrainPart import AntMoveBrainPart
from intelligine.cst import MOVE_MODE, MOVE_MODE_EXPLO, MOVE_MODE_GOHOME, PHEROMON_DIR_HOME, PHEROMON_DIR_EXPLO, \
    BRAIN_PART_TAKE, BRAIN_PART_PUT, MOVE_MODE_NURSE, PHEROMON_DIR_NONE
from intelligine.cst import PHEROMONE_SEARCHING
from intelligine.cst import BRAIN_PART_MOVE
from intelligine.simulation.object.brain.part.transport.AntPutBrainPart import AntPutBrainPart
from intelligine.simulation.object.brain.part.transport.AntTakeBrainPart import AntTakeBrainPart


class AntBrain(Brain):

    _brain_part_move_class = AntMoveBrainPart
    _brain_part_take_class = AntTakeBrainPart
    _brain_part_put_class = AntPutBrainPart

    def __init__(self, context, host):
        super().__init__(context, host)
        # TODO: Gerer les BrainPart avec un dictionnaire ?
        self._set_brain_part(BRAIN_PART_MOVE, self._get_move_brain_part_instance())
        self._set_brain_part(BRAIN_PART_TAKE, self._get_take_brain_part_instance())
        self._set_brain_part(BRAIN_PART_PUT, self._get_put_brain_part_instance())
        self._movement_mode = MOVE_MODE_EXPLO
        self._distance_from_objective = 0  # TODO rename: distance_since_objective
        self._pheromone_searching = PHEROMON_DIR_EXPLO

    def _get_move_brain_part_instance(self):
        return self._brain_part_move_class()

    def _get_take_brain_part_instance(self):
        return self._brain_part_take_class()

    def _get_put_brain_part_instance(self):
        return self._brain_part_put_class()

    def switch_to_mode(self, mode):
        self._movement_mode = mode
        self._update_pheromone_gland(mode)
        self._context.metas.value.set(MOVE_MODE, self._host.get_id(), mode)
        self._distance_from_objective = 0
        self._update_pheromone_searching(mode)

    def _update_pheromone_gland(self, mode):
        if mode == MOVE_MODE_EXPLO:
            pheromone_direction_type = PHEROMON_DIR_HOME
        elif mode == MOVE_MODE_GOHOME:
            pheromone_direction_type = PHEROMON_DIR_EXPLO
        elif mode == MOVE_MODE_NURSE:
            pheromone_direction_type = None
        else:
            raise NotImplementedError()

        if pheromone_direction_type:
            self._host.get_movement_pheromone_gland().set_pheromone_type(pheromone_direction_type)
            self._host.get_movement_pheromone_gland().enable()
        else:
            self._host.get_movement_pheromone_gland().disable()

    def _update_pheromone_searching(self, mode):
        if mode == MOVE_MODE_EXPLO:
            pheromone_searching = PHEROMON_DIR_EXPLO
        elif mode == MOVE_MODE_GOHOME:
            pheromone_searching = PHEROMON_DIR_HOME
        elif mode == MOVE_MODE_NURSE:
            pheromone_searching = PHEROMON_DIR_NONE
        else:
            raise NotImplementedError()
        self._pheromone_searching = pheromone_searching
        self._context.metas.value.set(PHEROMONE_SEARCHING, self._host.get_id(), pheromone_searching)

    def get_movement_mode(self):
        return self._movement_mode

    def host_moved(self, distance=1):
        self._distance_from_objective += 1

    def set_distance_from_objective(self, distance):
        self._distance_from_objective = distance

    def get_distance_from_objective(self):
        return self._distance_from_objective