import pygame
from intelligine.synergy.Colony import Colony
from intelligine.synergy.Environment import Environment
from intelligine.synergy.object.StockedFood import StockedFood
from synergine.synergy.Simulation import Simulation
from synergine_xyz.display.PygameImageRotate import PygameImageRotate
from synergine_xyz.display.PygameVisualisation import PygameVisualisation
from synergine_xyz.display.object.pygame.PygameImage import PygameImage
from intelligine.synergy.object.Food import Food
from intelligine.synergy.object.ant.Ant import Ant
from intelligine.synergy.object.Rock import Rock
from intelligine.synergy.object.ant.Egg import Egg
from os import getcwd
from synergine_xyz.cst import PREVIOUS_DIRECTION
from synergine_xyz.tmx.TileMapConnector import TileMapConnector

SURFACE_PHEROMONE_HOME = 'molecule_home'
SURFACE_PHEROMONE_EXPLORATION = 'molecule_exploration'

SURFACE_SMELL_EGG = 'smell_egg'
SURFACE_SMELL_FOOD = 'smell_food'

# TODO: Analyser les procedes ici pour proposer des outils dans le framework

# ant = PygameImage.from_filepath(getcwd()+'/intelligine/display/pygame/image/ant.png')
# food = PygameImage.from_filepath(getcwd()+'/intelligine/display/pygame/image/food.png')
# hole = PygameImage.from_filepath(getcwd()+'/intelligine/display/pygame/image/hole.png')
# dead_ant = PygameImage.from_filepath(getcwd()+'/intelligine/display/pygame/image/dead_ant.png')
# red_ant = PygameImage.from_filepath(getcwd()+'/intelligine/display/pygame/image/red_ant.png')
# green_ant = PygameImage.from_filepath(getcwd()+'/intelligine/display/pygame/image/green_ant.png')
# blue_ant = PygameImage.from_filepath(getcwd()+'/intelligine/display/pygame/image/blue_ant.png')
# dead_red_ant = PygameImage.from_filepath(getcwd()+'/intelligine/display/pygame/image/dead_red_ant.png')
# dead_green_ant = PygameImage.from_filepath(getcwd()+'/intelligine/display/pygame/image/dead_green_ant.png')
# dead_blue_ant = PygameImage.from_filepath(getcwd()+'/intelligine/display/pygame/image/dead_blue_ant.png')
# bug = PygameImage.from_filepath(getcwd()+'/intelligine/display/pygame/image/ant.png')
# rock = PygameImage.from_filepath(getcwd()+'/intelligine/display/pygame/image/rock.png')
egg = PygameImage.from_filepath(getcwd()+'/intelligine/display/pygame/image/egg.png')
eggc2 = PygameImage.from_filepath(getcwd()+'/intelligine/display/pygame/image/egg_c2.png')
eggc3 = PygameImage.from_filepath(getcwd()+'/intelligine/display/pygame/image/egg_c3.png')
eggc4 = PygameImage.from_filepath(getcwd()+'/intelligine/display/pygame/image/egg_c4.png')
eggc5 = PygameImage.from_filepath(getcwd()+'/intelligine/display/pygame/image/egg_c5.png')
eggc7 = PygameImage.from_filepath(getcwd()+'/intelligine/display/pygame/image/egg_c7.png')
phee = PygameImage.from_filepath(getcwd()+'/intelligine/display/pygame/image/phee.png')
pheh = PygameImage.from_filepath(getcwd()+'/intelligine/display/pygame/image/pheh.png')

smell = PygameImage.from_filepath(getcwd()+'/intelligine/display/pygame/image/smell.png')
#
# directions_ant = DirectionnedImage(ant)
# directions_red_ant = DirectionnedImage(red_ant)
# directions_blue_ant = DirectionnedImage(blue_ant)
# directions_green_ant = DirectionnedImage(green_ant)
#
# def bug_direction(bug, context):
#     if bug.get_life_points() <= 0:
#         return dead_ant
#     try:
#         previous_direction = context.metas.value.get(PREVIOUS_DIRECTION, bug.get_id())
#     except KeyError:
#         previous_direction = 14
#     return directions_ant.get_for_direction(previous_direction)
#
# def red_ant_direction(bug, context):
#     if bug.get_life_points() <= 0:
#         return dead_red_ant
#     try:
#         previous_direction = context.metas.value.get(PREVIOUS_DIRECTION, bug.get_id())
#     except KeyError:
#         previous_direction = 14
#     return directions_red_ant.get_for_direction(previous_direction)
#
# def blue_ant_direction(bug, context):
#     if bug.get_life_points() <= 0:
#         return dead_blue_ant
#     try:
#         previous_direction = context.metas.value.get(PREVIOUS_DIRECTION, bug.get_id())
#     except KeyError:
#         previous_direction = 14
#     return directions_blue_ant.get_for_direction(previous_direction)
#
# def green_ant_direction(bug, context):
#     if bug.get_life_points() <= 0:
#         return dead_green_ant
#     try:
#         previous_direction = context.metas.value.get(PREVIOUS_DIRECTION, bug.get_id())
#     except KeyError:
#         previous_direction = 14
#     return directions_green_ant.get_for_direction(previous_direction)
#
#
def for_position(position, objects, context):
    # TODO: DEV TMP: refact, etc
    eggs = []
    for obj in objects:
        if isinstance(obj, Egg):
            eggs.append(obj)
    if len(eggs) == 2:
        return (eggc2, eggs)
    if len(eggs) == 3:
        return (eggc3, eggs)
    if len(eggs) == 4:
        return (eggc4, eggs)
    if len(eggs) > 4:
        return (eggc7, eggs)
    return (None, [])
#
# visualisation = {
#     'window': {},
#     'callbacks': {
#         'position': for_position
#     },
#     'surfaces': {
#         SURFACE_PHEROMONE_EXPLORATION: {
#             'default': phee,
#             'callbacks': []
#         },
#         SURFACE_PHEROMONE_HOME: {
#             'default': pheh,
#             'callbacks': []
#         },
#     },
#     'objects': {
#         RedAnt: {
#             'default': red_ant,
#             'callbacks': [red_ant_direction]
#         },
#         BlueAnt: {
#             'default': blue_ant,
#             'callbacks': [blue_ant_direction]
#         },
#         GreenAnt: {
#             'default': green_ant,
#             'callbacks': [green_ant_direction]
#         },
#         Ant: {
#             'default': ant,
#             'callbacks': [bug_direction]
#         },
#         Bug: {
#             'default': bug,
#             'callbacks': [bug_direction]
#         },
#         Egg: {
#             'default': egg
#         },
#         Rock: {
#             'default': rock
#         },
#         Food: {
#             'default': food
#         },
#         Hole: {
#             'default': hole
#         }
#     }
# }

#############################
# Behind, new
#############################

map_config = {
    'simulation': {
        'base': Simulation
    },
    'collection': {
        'ant': Colony,
        'env': Environment
    },
    'object': {
        'ant': Ant,
        'egg': Egg,
        'rock': Rock,
        'food': Food,
        'stocked_food': StockedFood
    }
}
image_rotate = PygameImageRotate()


def dead_ant_callback_container(map_connector, production_class):
    tile_set_id = map_connector.get_dynamic_classes().get_production_class_collection_id(production_class)
    pil_image = map_connector.extract_image_with_class(tile_set_id, 'dead_ant')
    image_bytes = pil_image.tobytes()
    pygame_surface = pygame.image.fromstring(image_bytes, pil_image.size, pil_image.mode)
    pygame_image = PygameImage(pygame_surface)

    def dead_ant_callback(obj, context):
        # TODO: obj dans le col ALIVE truc comme ça
        if obj.get_life_points() <= 0:
            return pygame_image
        # TODO: raise, ou dans objectVisual.get_visual tests si bool plutot que is
        return False

    return dead_ant_callback


def ant_direction_modifier(obj, context, visual):
    try:
        previous_direction = context.metas.value.get(PREVIOUS_DIRECTION, obj.get_id())
    except KeyError:
        previous_direction = 14
    return image_rotate.get_for_direction(visual, previous_direction)


def get_standard_extract_from_map(map_file_path, map_config):
    map_connector = TileMapConnector.from_file(map_file_path, dict(map_config))
    visualisation = PygameVisualisation.get_default_visualisation()

    simulations = map_connector.create_simulations()
    visualizer = PygameVisualisation(visualisation)

    objects_images = map_connector.extract_objects_images()
    visualizer.update_objects_images(objects_images)

    map_connector.add_object_callback_to_visualisation(visualizer, [Ant], dead_ant_callback_container)
    ant_production_classes = map_connector.get_dynamic_classes().get_production_classes(Ant)

    for ant_production_class in ant_production_classes:
        visualizer.add_modifier(ant_production_class, ant_direction_modifier)

    visualisation.update({
        'callbacks': {
            'position': for_position
        },
        'surfaces': {
            SURFACE_PHEROMONE_EXPLORATION: {
                'default': phee,
                'callbacks': []
            },
            SURFACE_PHEROMONE_HOME: {
                'default': pheh,
                'callbacks': []
            },
            SURFACE_SMELL_EGG: {
                'default': smell,
                'callbacks': []
            },
            SURFACE_SMELL_FOOD: {
                'default': smell,
                'callbacks': []
            },
        }
    })

    return simulations, visualisation
