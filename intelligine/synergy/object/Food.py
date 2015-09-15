from intelligine.synergy.object.ressource.Ressource import Resource
from intelligine.cst import TYPE, TYPE_RESOURCE_EXPLOITABLE, TYPE_RESOURCE_EATABLE, COL_EATABLE, COL_SMELL, SMELL_FOOD, \
    TRANSPORTABLE


class Food(Resource):

    def __init__(self, collection, context):
        super().__init__(collection, context)
        context.metas.list.add(TYPE, self.get_id(), TYPE_RESOURCE_EXPLOITABLE)

    def get_what_carry(self):
        return self  # dev
        clone = self.__class__(self._collection, self._context)
        self._collection.add_object(clone)
        return clone

    def transform_to_stocked(self):
        self._context.metas.list.remove(TYPE, self.get_id(), TYPE_RESOURCE_EXPLOITABLE)
        self._context.metas.list.add(TYPE, self.get_id(), TYPE_RESOURCE_EATABLE)
        self._add_col(COL_EATABLE)
        self._add_col(COL_SMELL)
        self._set_smell(SMELL_FOOD)
