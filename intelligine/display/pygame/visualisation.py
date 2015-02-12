from xyworld.display.object.pygame.PygameImage import PygameImage
from xyworld.display.object.pygame.DirectionnedImage import DirectionnedImage
from intelligine.synergy.object.Bug import Bug
from intelligine.synergy.object.ant.Ant import Ant
from intelligine.sandbox.colored.BlueAnt import BlueAnt
from intelligine.sandbox.colored.RedAnt import RedAnt
from intelligine.sandbox.colored.GreenAnt import GreenAnt
from intelligine.synergy.object.Rock import Rock
from os import getcwd
from synergine.metas import metas
from intelligine.cst import PREVIOUS_DIRECTION

# TODO: Analyser les procedes ici pour proposer des outils dans le framework

ant = PygameImage.from_filepath(getcwd()+'/intelligine/display/pygame/image/ant.png')
dead_ant = PygameImage.from_filepath(getcwd()+'/intelligine/display/pygame/image/dead_ant.png')
red_ant = PygameImage.from_filepath(getcwd()+'/intelligine/display/pygame/image/red_ant.png')
green_ant = PygameImage.from_filepath(getcwd()+'/intelligine/display/pygame/image/green_ant.png')
blue_ant = PygameImage.from_filepath(getcwd()+'/intelligine/display/pygame/image/blue_ant.png')
dead_red_ant = PygameImage.from_filepath(getcwd()+'/intelligine/display/pygame/image/dead_red_ant.png')
dead_green_ant = PygameImage.from_filepath(getcwd()+'/intelligine/display/pygame/image/dead_green_ant.png')
dead_blue_ant = PygameImage.from_filepath(getcwd()+'/intelligine/display/pygame/image/dead_blue_ant.png')
bug = PygameImage.from_filepath(getcwd()+'/intelligine/display/pygame/image/ant.png')
rock = PygameImage.from_filepath(getcwd()+'/intelligine/display/pygame/image/rock.png')

directions_ant = DirectionnedImage(ant)
directions_red_ant = DirectionnedImage(red_ant)
directions_blue_ant = DirectionnedImage(blue_ant)
directions_green_ant = DirectionnedImage(green_ant)

def bug_direction(bug):
    if bug.get_life_points() <= 0:
        return dead_ant
    try:
        previous_direction = metas.value.get(PREVIOUS_DIRECTION, bug.get_id())
    except KeyError:
        previous_direction = 14
    return directions_ant.get_for_direction(previous_direction)

def red_ant_direction(bug):
    if bug.get_life_points() <= 0:
        return dead_red_ant
    try:
        previous_direction = metas.value.get(PREVIOUS_DIRECTION, bug.get_id())
    except KeyError:
        previous_direction = 14
    return directions_red_ant.get_for_direction(previous_direction)

def blue_ant_direction(bug):
    if bug.get_life_points() <= 0:
        return dead_blue_ant
    try:
        previous_direction = metas.value.get(PREVIOUS_DIRECTION, bug.get_id())
    except KeyError:
        previous_direction = 14
    return directions_blue_ant.get_for_direction(previous_direction)

def green_ant_direction(bug):
    if bug.get_life_points() <= 0:
        return dead_green_ant
    try:
        previous_direction = metas.value.get(PREVIOUS_DIRECTION, bug.get_id())
    except KeyError:
        previous_direction = 14
    return directions_green_ant.get_for_direction(previous_direction)

visualisation = {
    'window': {},
    'objects': {
        RedAnt: {
            'default': red_ant,
            'callbacks': [red_ant_direction]
        },
        BlueAnt: {
            'default': blue_ant,
            'callbacks': [blue_ant_direction]
        },
        GreenAnt: {
            'default': green_ant,
            'callbacks': [green_ant_direction]
        },
        Ant: {
            'default': ant,
            'callbacks': [bug_direction]
        },
        Bug: {
            'default': bug,
            'callbacks': [bug_direction]
        },
        Rock: {
            'default': rock
        }
    }
}