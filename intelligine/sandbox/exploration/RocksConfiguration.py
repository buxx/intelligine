from synergine.synergy.collection.Configuration import Configuration
from intelligine.synergy.object.Rock import Rock
import pytmx
from os import getcwd


class RocksConfiguration(Configuration):

    def get_start_objects(self, collection, context):
        rocks = []
        # TODO: Experimental: Crer un loader de TMX (qui gere aussi les visualisation ?)
        tmxdata = pytmx.TiledMap(getcwd()+"/intelligine/sandbox/exploration/map2.tmx")

        objects = {}
        for tileset in tmxdata.tilesets:
            obj_id = tileset.firstgid
            file = tmxdata.tile_properties[obj_id]['file']
            classname = tmxdata.tile_properties[obj_id]['classname']
            mod = __import__(file,
                             fromlist=[classname])
            objects[obj_id] = {
                'class': getattr(mod, classname)
            }

        for layer in [vl for vl in tmxdata.visible_layers]:
            for xi, x in enumerate(layer.data):
                for yi, y in enumerate(x):
                    if y in objects:
                        rock = objects[y]['class'](collection, context)
                        rock.set_position((0, xi, yi))
                        rocks.append(rock)

        return rocks