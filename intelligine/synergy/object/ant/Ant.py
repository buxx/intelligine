from intelligine.core.exceptions import MoleculeException
from intelligine.synergy.object.Bug import Bug
from intelligine.cst import CARRYING, TRANSPORTER, ATTACKER, COL_TRANSPORTER, COL_TRANSPORTER_NOT_CARRYING, \
    COL_FIGHTER, MOVE_MODE_EXPLO, MOVE_MODE_GOHOME, BODY_PART_PHEROMONE_GLAND, TYPE, TYPE_ANT, \
    COL_TRANSPORTER_CARRYING, MOVE_MODE_NURSE, MOVE_MODE_HOME
from intelligine.synergy.object.Food import Food
from intelligine.simulation.object.molecule.MovementMoleculeGland import MovementMoleculeGland
from intelligine.simulation.object.brain.AntBrain import AntBrain


class Ant(Bug):

    _body_parts = {
        BODY_PART_PHEROMONE_GLAND: MovementMoleculeGland
    }
    _brain_class = AntBrain

    def __init__(self, collection, context):
        super().__init__(collection, context)
        context.metas.states.add_list(self.get_id(), [TRANSPORTER, ATTACKER])
        context.metas.collections.add_list(self.get_id(), [COL_TRANSPORTER,
                                                           COL_TRANSPORTER_NOT_CARRYING,
                                                           COL_FIGHTER])
        self._carried = None
        self._brain.switch_to_mode(MOVE_MODE_EXPLO)
        context.metas.list.add(TYPE, self.get_id(), TYPE_ANT)

    def die(self):
        super().die()
        self._remove_state(TRANSPORTER)
        self._remove_state(ATTACKER)
        self._remove_col(COL_TRANSPORTER)
        self._remove_col(COL_TRANSPORTER_NOT_CARRYING)
        self._remove_col(COL_TRANSPORTER_CARRYING, allow_not_in=True)
        self._remove_col(COL_FIGHTER)

    def get_movement_molecule_gland(self):
        return self.get_body_part(BODY_PART_PHEROMONE_GLAND)

    def put_carry(self, obj, position=None):
        if position is None:
            position = self._get_position()
        self._carried = None
        obj.set_position(position)
        obj.set_is_carried(False, self)
        self._context.metas.states.remove(self.get_id(), CARRYING)
        self._add_col(COL_TRANSPORTER_NOT_CARRYING)
        self._remove_col(COL_TRANSPORTER_CARRYING)

    def get_carried(self):
        return self._carried

    def carry(self, obj):
        self._carried = obj
        self._context.metas.states.add(self.get_id(), CARRYING)
        self._add_col(COL_TRANSPORTER_CARRYING)
        self._remove_col(COL_TRANSPORTER_NOT_CARRYING)
        obj.set_is_carried(True, self)
        # TODO: pour le moment hardcode, a gerer dans AntTakeBrainPart (callback en fct de ce qui est depose)
        if isinstance(obj, Food):
            self.get_brain().switch_to_mode(MOVE_MODE_GOHOME)
            self.get_movement_molecule_gland().appose()

    def is_carrying(self):
        if self._carried:
            return True
        return False

    def set_position(self, position):
        if self._position is not None and position != self._position:
            self._brain.host_moved()
        super().set_position(position)
        if self.is_carrying():
            self._carried.set_position(position)

    def initialize(self):
        super().initialize()
        if self.get_movement_molecule_gland().is_enabled():
            try:
                self.get_movement_molecule_gland().appose()
            except MoleculeException:
                pass

    def get_colony(self):
        return self.get_collection()