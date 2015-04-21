from intelligine.core.exceptions import BrainPartAlreadyExist
from intelligine.cst import BRAIN_SCHEMA


class Brain():

    _brain_parts = {}

    def __init__(self, context, host):
        self._context = context
        self._host = host
        self._schema = {}
        self._parts = {}
        self._init_parts()

    def _init_parts(self):
        for brain_part_name in self._brain_parts:
            self._set_brain_part(brain_part_name, self._brain_parts[brain_part_name](self))

    def _set_brain_part(self, name, brain_part, replace=False):
        if name in self._parts and not replace:
            raise BrainPartAlreadyExist()
        self._parts[name] = brain_part
        self._update_schema()

    def get_part(self, name):
        return self._parts[name]

    def _update_schema(self):
        self._schema = {}
        for part_name in self._parts:
            self._schema[part_name] = self._parts[part_name].__class__
        # TODO: N'est-ce pas un schema appartenant a la classe ? Ne suffirai t-il pas de stocker ce schema par classe
        # plutôt que par objet ?
        self._context.metas.value.set(BRAIN_SCHEMA, self._host.get_id(), self._schema)
