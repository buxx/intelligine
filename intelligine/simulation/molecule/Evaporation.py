from intelligine.cst import MOLECULES, MOLECULES_DIRECTION
from intelligine.synergy.stigmergy.MoleculesManager import MoleculesManager


class Evaporation:

    def __init__(self, context,
                 intensity_decrement=1,
                 molecule_minimum_age=0,
                 molecules_exclude_types=None,
                 molecules_include_types=None):
        self._context = context
        self._intensity_decrement = intensity_decrement
        self._molecules_manager = MoleculesManager(context)
        self._molecule_minimum_age = molecule_minimum_age
        self._molecules_exclude_types = molecules_exclude_types
        self._molecules_include_types = molecules_include_types

    def evaporate(self):
        for position, flavour in self._get_flavours():
            self._decrease_flavour(flavour)
            self._molecules_manager.set_flavour(position, flavour)

    def remove(self):
        for position, flavour in self._get_flavours():
            self._remove_molecule(flavour)
            self._molecules_manager.set_flavour(position, flavour)

    def _get_flavours(self):
        molecules_points = self._context.metas.list.get(MOLECULES, MOLECULES, allow_empty=True)
        for molecule_point in molecules_points:
            yield molecule_point, self._molecules_manager.get_flavour(molecule_point)

    def _decrease_flavour(self, flavour):
        for direction_molecule in self._get_molecules_from_flavour(flavour):
            direction_molecule.increment_intensity(-self._intensity_decrement)
            flavour.set_molecule(direction_molecule)

    def _get_molecules_from_flavour(self, flavour):
        molecules = []
        for direction_molecule in flavour.get_molecules(MOLECULES_DIRECTION):
            if not self._is_recent_molecule(direction_molecule) \
               and not self._is_excluded_molecule_type(direction_molecule):
                molecules.append(direction_molecule)
        return molecules

    def _remove_molecule(self, flavour):
        for direction_molecule in self._get_molecules_from_flavour(flavour):
            flavour.remove_molecule(direction_molecule)

    def _is_recent_molecule(self, molecule):
        return (self._context.get_cycle() - molecule.get_cycle_age()) < self._molecule_minimum_age

    def _is_excluded_molecule_type(self, molecule):
        if not self._molecules_exclude_types and not self._molecules_include_types:
            return False

        if self._molecules_exclude_types and not self._molecules_include_types:
            return molecule.get_type() in self._molecules_exclude_types

        if not self._molecules_exclude_types and self._molecules_include_types:
            return molecule.get_type() not in self._molecules_include_types
