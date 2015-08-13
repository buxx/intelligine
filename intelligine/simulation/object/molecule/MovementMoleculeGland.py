from intelligine.cst import MOLECULES_DIRECTION
from intelligine.simulation.object.molecule.MoleculeGland import MoleculeGland
from intelligine.simulation.molecule.Molecule import Molecule


class MovementMoleculeGland(MoleculeGland):

    def get_molecule(self):
        """
        :return: Molecule
        """
        return Molecule(MOLECULES_DIRECTION,
                        self._molecule_type,
                        self._host.get_brain().get_distance_from_objective(),
                        1)
