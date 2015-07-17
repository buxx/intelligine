from intelligine.simulation.object.brain.part.move.AntStar.ByPass import ByPass
from intelligine.simulation.object.brain.part.move.AntStar.Host import Host
from intelligine.simulation.object.brain.part.move.MoveBrainPart import MoveBrainPart
from intelligine.synergy.event.move.direction import directions_modifiers
from synergine_xyz.cst import POSITION
from intelligine.core.exceptions import NoMolecule, NoTypeInMolecule
from intelligine.cst import MOLECULE_SEARCHING, MOVE_MODE_EXPLO, MOVE_MODE_HOME, MOVE_MODE, MOVE_MODE_GOHOME, \
    EXPLORATION_VECTOR, MOLECULES_DIRECTION, SMELL_FOOD, SMELL_EGG
from intelligine.simulation.molecule.DirectionMolecule import DirectionMolecule


class AntMoveBrainPart(MoveBrainPart):

    def __init__(self, host_brain):
        super().__init__(host_brain)
        self._exploration_vector = (0, 0)

    def _set_exploration_vector(self, new_vector):
        self._exploration_vector = new_vector
        # TODO: On devrais donner le context aux brain parts
        self._host_brain.get_context().metas.value.set(EXPLORATION_VECTOR,
                                                       self._host_brain.get_host().get_id(),
                                                       new_vector)

    @classmethod
    def get_direction(cls, context, object_id):
        move_mode = context.metas.value.get(MOVE_MODE, object_id)
        if move_mode == MOVE_MODE_GOHOME:
            return cls._get_direction_with_exploration_vector(context, object_id)
        else:
            try:
                return cls._get_direction_with_molecules(context, object_id)
            except NoMolecule:
                return super().get_direction(context, object_id)

        return super().get_direction(context, object_id)

    @classmethod
    def _get_direction_with_molecules(cls, context, object_id):
        object_point = context.metas.value.get(POSITION, object_id)
        molecule_type = context.metas.value.get(MOLECULE_SEARCHING, object_id)
        try:
            direction = cls._get_molecule_direction_for_point(context, object_point, molecule_type)
        except NoMolecule:
            try:
                direction = cls._get_direction_of_molecule(context, object_point, molecule_type)
            except NoMolecule:
                raise
        return direction

    @staticmethod
    def _get_molecule_direction_for_point(context, point, molecule_type):
        return DirectionMolecule.get_direction_for_point(context, point, molecule_type)

    @staticmethod
    def _get_direction_of_molecule(context, point, molecule_type):
        search_molecule_in_points = context.get_around_points_of_point(point)
        try:
            best_molecule_direction = DirectionMolecule.get_best_molecule_direction_in(context,
                                                                                       point,
                                                                                       search_molecule_in_points,
                                                                                       molecule_type)
            return best_molecule_direction
        except NoMolecule as err:
            raise err

    @classmethod
    def _get_direction_with_exploration_vector(cls, context, object_id):
        ant_star = cls._get_by_pass_brain(context, object_id)
        ant_star.advance()
        ant_star.has_moved()
        return ant_star.get_host().get_moved_to_direction()

    @classmethod
    def _get_by_pass_brain(cls, context, object_id):
        # We use an adaptation of AntStar
        exploration_vector = context.metas.value.get(EXPLORATION_VECTOR, object_id)
        home_vector = (-exploration_vector[0], -exploration_vector[1])
        ant_host = Host(context, object_id)
        return ByPass(ant_host, home_vector, context, object_id)

    # TODO: obj pas necessaire, il est dans _host
    def done(self, obj, context):
        super().done(obj, context)
        self._appose_molecule(obj)
        self._check_context(obj, context)
        self._apply_context(obj, context)

    @staticmethod
    def _appose_molecule(obj):
        if obj.get_movement_molecule_gland().is_enabled():
            obj.get_movement_molecule_gland().appose()

    def _check_context(self, obj, context):
        """

        If was in exploration, and just found home smell;
            -> home mode (then, in this mode: no update vector, put food if food, etc)
        If was in home, and just loose home smell:
            -> exploration mode

        :param obj:
        :param context:
        :return:
        """
        movement_mode = self._host_brain.get_movement_mode()

        if movement_mode == MOVE_MODE_GOHOME and self._on_home_smell(context, obj.get_id()):
            self._host_brain.switch_to_mode(MOVE_MODE_HOME)
            ant_star = self._get_by_pass_brain(context, obj.get_id())
            ant_star.erase()
            # TODO: on change les molecule recherché (Food => SmellFood, definis dans Take, en fct de ce qui est take)

        elif movement_mode == MOVE_MODE_HOME and not self._on_home_smell(context, obj.get_id()):
            self._host_brain.switch_to_mode(MOVE_MODE_EXPLO)
            self._start_new_exploration()

        elif movement_mode == MOVE_MODE_EXPLO and self._on_home_smell(context, obj.get_id()):
            self._start_new_exploration()  # TODO: rename en reinit_explo

        # TODO: sitch explo si rien a faire (rien a poser par exemple) et HOME

        # TODO: Poser sur StockedFood

    @classmethod
    def _on_home_smell(cls, context, object_id):
        current_position = context.metas.value.get(POSITION, object_id)
        flavour = context.molecules().get_flavour(current_position)
        # TODO: Idem, liste de smell_type ...
        for smell_type in (SMELL_FOOD, SMELL_EGG):
            try:
                molecule = flavour.get_molecule(category=MOLECULES_DIRECTION, type=smell_type)
                return True
            except NoTypeInMolecule:
                pass  # C'est qu'elle y est pas ^^
        return False

    def _update_exploration_vector(self):
        # TODO: add tuple as vectors ?
        just_move_vector = directions_modifiers[self._host_brain.get_host().get_previous_direction()]
        self._set_exploration_vector((self._exploration_vector[0] + just_move_vector[1],
                                      self._exploration_vector[1] + just_move_vector[2]))

    def _apply_context(self, obj, context):
        movement_mode = self._host_brain.get_movement_mode()
        if movement_mode == MOVE_MODE_EXPLO or movement_mode == MOVE_MODE_GOHOME:
            self._update_exploration_vector()

    def _start_new_exploration(self):
        self._exploration_vector = (0, 0)