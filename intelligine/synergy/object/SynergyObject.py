from intelligine.cst import OBJ_SMELL
from synergine_xyz.SynergyObject import SynergyObject as XyzSynergyObject


class SynergyObject(XyzSynergyObject):

    def __init__(self, collection, context):
        super().__init__(collection, context)
        self._smell = None

    def _set_smell(self, smell_type):
        self._smell = smell_type
        self._context.metas.value.set(OBJ_SMELL, self.get_id(), smell_type)

    def get_smell(self):
        if not self._smell:
            raise Exception('Smell type not defined')
        return self._smell