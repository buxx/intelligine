from intelligine.cst import BRAIN_SCHEMA


class Brain():

    _brain_parts = {}

    def __init__(self, context, host):
        self._context = context
        self._host = host
        self._parts = {}
        self._init_parts()

    def _init_parts(self):
        for brain_part_name in self._brain_parts:
            self._parts[brain_part_name] = self._brain_parts[brain_part_name](self)
        self._context.metas.value.set(BRAIN_SCHEMA, self._host.__class__, self._brain_parts)

    def get_part(self, name):
        return self._parts[name]

    def get_context(self):
        return self._context

    def get_host(self):
        return self._host