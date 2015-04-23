from intelligine.synergy.object.ressource.Ressource import Resource
from intelligine.cst import TRANSPORTABLE, TYPE, TYPE_RESOURCE_TRANSFORMABLE


class Food(Resource):

    def __init__(self, collection, context):
        super().__init__(collection, context)
        context.metas.list.add(TYPE, self.get_id(), TYPE_RESOURCE_TRANSFORMABLE)

    def get_what_carry(self):
        clone = self.__class__(self._collection, self._context)
        self._collection.add_object(clone)
        return clone
