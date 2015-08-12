from intelligine.core.exceptions import NoTypeInMolecule, NoCategoryInMolecule
from intelligine.simulation.molecule.Molecule import Molecule


class MoleculeFlavour():

    @classmethod
    def new_from_raw_data(cls, raw_data):
        flavour = {}
        for category in raw_data:
            molecules_by_category = raw_data[category]
            for type in molecules_by_category:
                distance, intensity, cycle_age = molecules_by_category[type]
                if category not in flavour:
                    flavour[category] = {}
                flavour[category][type] = Molecule(category, type, distance, intensity, cycle_age)
        return cls(flavour)

    def get_raw_data(self):
        raw_data = {}
        for category in self._flavour:
            molecules_by_category = self._flavour[category]
            for type in molecules_by_category:
                molecule = molecules_by_category[type]
                if category not in raw_data:
                    raw_data[category] = {}
                if molecule.get_intensity() >= 0:
                    raw_data[category][type] = (molecule.get_distance(),
                                                molecule.get_intensity(),
                                                molecule.get_cycle_age())
        return raw_data

    def __init__(self, flavour):
        self._flavour = flavour

    def get_molecule(self, category, type):
        types = self.get_types(category)
        if type not in types:
            raise NoTypeInMolecule()
        return types[type]

    def get_molecules(self, category):
        """

        :param category:
        :return: Molecules dict or empty dict of no molecules
        """
        try:
            return self.get_types(category).values()
        except NoCategoryInMolecule:
            return {}

    def get_molecules_types(self, category):
        try:
            return self.get_types(category).keys()
        except NoCategoryInMolecule:
            return {}

    def get_types(self, category):
        if category not in self._flavour:
            raise NoCategoryInMolecule()
        return self._flavour[category]

    def set_molecule(self, molecule):
        category = molecule.get_category()
        type = molecule.get_type()

        if category not in self._flavour:
            self._flavour[category] = {}

        self._flavour[category][type] = molecule