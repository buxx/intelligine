from intelligine.cst import BRAIN, BRAIN_SCHEMA


def get_brain_class(context, object_id):
    return context.metas.value.get(BRAIN, object_id)


def get_brain_part(context, object_id, brain_part_name):
    object_brain_schema = context.metas.value.get(BRAIN_SCHEMA, object_id)
    return object_brain_schema[brain_part_name]
