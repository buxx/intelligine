from intelligine.simulation.molecule.DirectionMolecule import DirectionMolecule
from intelligine.simulation.object.brain.Brain import Brain
from intelligine.simulation.object.brain.part.attack.AttackBrainPart import AttackBrainPart
from intelligine.cst import MODE, MODE_EXPLO, MODE_GOHOME, PHEROMON_DIR_EXPLO, \
    BRAIN_PART_TAKE, BRAIN_PART_PUT, MODE_NURSE, PHEROMON_DIR_NONE, BRAIN_PART_ATTACK, MODE_HOME, \
    SMELL_FOOD, SMELL_EGG, MODE_GO_OUTSIDE, MOLECULE_SEARCHING_WAY, MODE_SEARCH_AROUND
from intelligine.cst import MOLECULE_SEARCHING
from intelligine.cst import BRAIN_PART_MOVE
from intelligine.simulation.object.brain.part.transport.AntPutBrainPart import AntPutBrainPart
from intelligine.simulation.object.brain.part.transport.AntTakeBrainPart import AntTakeBrainPart
from intelligine.synergy.object.Food import Food
from intelligine.synergy.object.ant.Egg import Egg
from intelligine.simulation.object.brain.part.move.AntMoveBrainPart import AntMoveBrainPart
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
        self._distance_from_objective = 0
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
        elif mode == MODE_GO_OUTSIDE:
            molecule_direction_type = None
        elif mode == MODE_SEARCH_AROUND:
            molecule_direction_type = PHEROMON_DIR_EXPLO
        else:
            raise NotImplementedError()

        if molecule_direction_type:
            self._host.get_movement_molecule_gland().set_molecule_type(molecule_direction_type)
            self._host.get_movement_molecule_gland().enable()
        else:
            self._host.get_movement_molecule_gland().disable()

    def _update_molecule_searching(self, mode):
        way = DirectionMolecule.WAY_UP
        if mode == MODE_EXPLO:
            molecule_searching = PHEROMON_DIR_EXPLO
        elif mode == MODE_GOHOME:
            molecule_searching = PHEROMON_DIR_NONE
        elif mode == MODE_NURSE:
            molecule_searching = PHEROMON_DIR_NONE
        elif mode == MODE_HOME:
            molecule_searching = self.get_part(BRAIN_PART_TAKE).get_smell_target()
        elif mode == MODE_GO_OUTSIDE:
            #  TODO: Dans l'idée c'est sortir, donc il faudrait remonter toutes les smells ...
            molecule_searching = self.get_part(BRAIN_PART_TAKE).get_smell_target()
            way = DirectionMolecule.WAY_DOWN
        elif mode == MODE_SEARCH_AROUND:
            molecule_searching = PHEROMON_DIR_NONE
        else:
            raise NotImplementedError()

        self._molecule_searching = molecule_searching
        self._molecule_searching_way = way
        self._context.metas.value.set(MOLECULE_SEARCHING, self._host.get_id(), molecule_searching)
        self._context.metas.value.set(MOLECULE_SEARCHING_WAY, self._host.get_id(), way)

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
