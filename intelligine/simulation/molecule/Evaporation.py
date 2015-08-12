from intelligine.cst import MOLECULES, MOLECULES_DIRECTION
from intelligine.synergy.stigmergy.MoleculesManager import MoleculesManager


class Evaporation:

    def __init__(self, context, intensity_decrement, molecules_exclude_types, molecule_minimum_age):
        self._context = context
        self._intensity_decrement = intensity_decrement
        self._molecules_manager = MoleculesManager(context)
        self._molecules_exclude_types = molecules_exclude_types
        self._molecule_minimum_age = molecule_minimum_age

    def evaporate(self):
        for position, flavour in self._get_flavours():
            self._decrease_flavour(flavour)
            self._molecules_manager.set_flavour(position, flavour)

    def _get_flavours(self):
        molecules_points = self._context.metas.list.get(MOLECULES, MOLECULES)
        for molecule_point in molecules_points:
            yield molecule_point, self._molecules_manager.get_flavour(molecule_point)

    def _decrease_flavour(self, flavour):
        for direction_molecule in flavour.get_molecules(MOLECULES_DIRECTION):
            if not self._is_recent_molecule(direction_molecule) \
               and not self._is_excluded_molecule_type(direction_molecule):
                direction_molecule.increment_intensity(-self._intensity_decrement)
                flavour.set_molecule(direction_molecule)

    def _is_recent_molecule(self, molecule):
        return (self._context.get_cycle() - molecule.get_cycle_age()) < self._molecule_minimum_age

    def _is_excluded_molecule_type(self, molecule):
        return molecule.get_type() in self._molecules_exclude_types
