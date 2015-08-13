from intelligine.cst import BRAIN, BRAIN_SCHEMA, INSTANCE_CLASS


def get_brain_class(context, object_id):
    object_class = context.metas.value.get(INSTANCE_CLASS, object_id)
    return context.metas.value.get(BRAIN, object_class)


def get_brain_part(context, object_id, brain_part_name):
    object_class = context.metas.value.get(INSTANCE_CLASS, object_id)
    object_brain_schema = context.metas.value.get(BRAIN_SCHEMA, object_class)
    return object_brain_schema[brain_part_name]
