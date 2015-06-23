from intelligine.core.exceptions import BestMoleculeHere, MoleculeGlandDisabled
from intelligine.simulation.molecule.DirectionMolecule import DirectionMolecule

class MoleculeGland():

    def __init__(self, host, context):
        self._molecule_type = None
        self._host = host
        self._context = context
        self._enabled = False

    def set_molecule_type(self, molecule_type):
        self._molecule_type = molecule_type

    def get_molecule_type(self):
        if self._molecule_type is None:
            raise Exception("molecule_type not specified")
        return self._molecule_type

    def get_molecule(self):
        raise NotImplementedError()

    def appose(self):
        if not self._enabled:
            raise MoleculeGlandDisabled()

        try:
            DirectionMolecule.appose(self._context,
                                      self._host.get_position(),
                                      self.get_molecule())
        except BestMoleculeHere as best_molecule_here:
            self._host.get_brain().set_distance_from_objective(best_molecule_here.get_best_distance())

    def disable(self):
        self._enabled = False

    def enable(self):
        self._enabled = True

    def is_enabled(self):
        return self._enabled