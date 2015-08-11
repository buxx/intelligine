from intelligine.simulation.object.brain.Brain import Brain
from intelligine.simulation.object.brain.part.attack.AttackBrainPart import AttackBrainPart
from intelligine.simulation.object.brain.part.move.AntMoveBrainPart import AntMoveBrainPart
from intelligine.cst import MODE, MODE_EXPLO, MODE_GOHOME, PHEROMON_DIR_EXPLO, \
    BRAIN_PART_TAKE, BRAIN_PART_PUT, MODE_NURSE, PHEROMON_DIR_NONE, BRAIN_PART_ATTACK, MODE_HOME, \
    SMELL_FOOD, SMELL_EGG
from intelligine.cst import MOLECULE_SEARCHING
from intelligine.cst import BRAIN_PART_MOVE
from intelligine.simulation.object.brain.part.transport.AntPutBrainPart import AntPutBrainPart
from intelligine.simulation.object.brain.part.transport.AntTakeBrainPart import AntTakeBrainPart
from intelligine.synergy.object.Food import Food
from intelligine.synergy.object.ant.Egg import Egg
from synergine.core.exceptions import NotFound


class AntBrain(Brain):

    _brain_parts = Brain._brain_parts.copy()
    _brain_parts.update({
        BRAIN_PART_MOVE: AntMoveBrainPart,
        BRAIN_PART_TAKE: AntTakeBrainPart,
        BRAIN_PART_PUT: AntPutBrainPart,
        BRAIN_PART_ATTACK: AttackBrainPart
    })

    _taken_smell_matches = {
        Food: SMELL_FOOD,
        Egg: SMELL_EGG
    }
    """ Correspondance entre ce qui est ramassé et où ce doit être stocké """

    def __init__(self, context, host):
        super().__init__(context, host)
        self._movement_mode = MODE_HOME
        self._distance_from_objective = 0  # TODO rename: distance_since_objective
        self._molecule_searching = PHEROMON_DIR_EXPLO

    def switch_to_mode(self, mode):
        self._movement_mode = mode
        self._update_molecule_gland(mode)
        self._context.metas.value.set(MODE, self._host.get_id(), mode)
        self._update_molecule_searching(mode)

    def _update_molecule_gland(self, mode):
        if mode == MODE_EXPLO:
            molecule_direction_type = None
        elif mode == MODE_GOHOME:
            molecule_direction_type = PHEROMON_DIR_EXPLO
            self._distance_from_objective = 0
        elif mode == MODE_NURSE:
            molecule_direction_type = None
        elif mode == MODE_HOME:
            molecule_direction_type = PHEROMON_DIR_EXPLO
        else:
            raise NotImplementedError()

        if molecule_direction_type:
            self._host.get_movement_molecule_gland().set_molecule_type(molecule_direction_type)
            self._host.get_movement_molecule_gland().enable()
        else:
            self._host.get_movement_molecule_gland().disable()

    def _update_molecule_searching(self, mode):
        if mode == MODE_EXPLO:
            molecule_searching = PHEROMON_DIR_EXPLO
        elif mode == MODE_GOHOME:
            molecule_searching = PHEROMON_DIR_NONE
        elif mode == MODE_NURSE:
            molecule_searching = PHEROMON_DIR_NONE
        elif mode == MODE_HOME:
            # TODO: Ca depend de ce que fait la fourmis, si s'occupe des oeufs, etc
            molecule_searching = self.get_part(BRAIN_PART_TAKE).get_smell_target()
        else:
            raise NotImplementedError()

        self._molecule_searching = molecule_searching
        self._context.metas.value.set(MOLECULE_SEARCHING, self._host.get_id(), molecule_searching)

    def get_movement_mode(self):
        return self._movement_mode

    def host_moved(self, distance=1):
        self._distance_from_objective += distance

    def set_distance_from_objective(self, distance):
        self._distance_from_objective = distance

    def get_distance_from_objective(self):
        return self._distance_from_objective

    def get_smell_for_object_taken(self, obj):
        for take_class in self._taken_smell_matches:
            if isinstance(obj, take_class):
                return self._taken_smell_matches[take_class]
        raise NotFound()

    @classmethod
    def get_home_smells(cls):
        """
        Note: Actually return all know smells. Not really HOME smells.
        :return:
        """
        return cls._taken_smell_matches.values()
