from intelligine.core.exceptions import BestMoleculeHere, NoMolecule
from intelligine.cst import PHEROMON_INFOS
from intelligine.simulation.molecule.MoleculeFlavour import MoleculeFlavour
from intelligine.simulation.molecule.Molecule import Molecule


class MoleculesManager():

    def __init__(self, context):
        self._context = context

    def get_flavour(self, position):
        point_molecules = self._context.metas.value.get(PHEROMON_INFOS,
                                                         position,
                                                         allow_empty=True,
                                                         empty_value={})
        return MoleculeFlavour.new_from_raw_data(point_molecules)

    def set_flavour(self, position, flavour):
        self._context.metas.value.set(PHEROMON_INFOS, position, flavour.get_raw_data())

    def get_molecule(self, position, category, type, allow_empty=False):
        flavour = self.get_flavour(position)
        try:
            return flavour.get_molecule(category, type)
        except NoMolecule:
            if allow_empty:
                return Molecule()
            raise

    def increment_with_molecule(self, position, apposed_molecule):
        flavour = self.get_flavour(position)
        try:
            position_molecule = flavour.get_molecule(apposed_molecule.get_category(), apposed_molecule.get_type())
        except NoMolecule:
            position_molecule = Molecule(apposed_molecule.get_category(),
                                           apposed_molecule.get_type(),
                                           distance=apposed_molecule.get_distance())

        position_molecule.increment_intensity(apposed_molecule.get_intensity())

        if apposed_molecule.get_distance() < position_molecule.get_distance():
            position_molecule.set_distance(apposed_molecule.get_distance())

        flavour.set_molecule(position_molecule)
        self.set_flavour(position, flavour)

        if apposed_molecule.get_distance() > position_molecule.get_distance():
            raise BestMoleculeHere(position_molecule.get_distance())