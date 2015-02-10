from xyworld.display.object.pygame.PygameImage import PygameImage
from xyworld.display.object.pygame.DirectionnedImage import DirectionnedImage
from socialintengine.synergy.object.Bug import Bug
from socialintengine.synergy.object.ant.Ant import Ant
from socialintengine.sandbox.redblue.BlueAnt import BlueAnt
from socialintengine.sandbox.redblue.RedAnt import RedAnt
from socialintengine.synergy.object.Rock import Rock
from os import getcwd
from synergine.metas import metas
from socialintengine.cst import PREVIOUS_DIRECTION

ant = PygameImage.from_filepath(getcwd()+'/socialintengine/display/pygame/image/ant.png')
red_ant = PygameImage.from_filepath(getcwd()+'/socialintengine/display/pygame/image/red_ant.png')
blue_ant = PygameImage.from_filepath(getcwd()+'/socialintengine/display/pygame/image/blue_ant.png')
bug = PygameImage.from_filepath(getcwd()+'/socialintengine/display/pygame/image/ant.png')
rock = PygameImage.from_filepath(getcwd()+'/socialintengine/display/pygame/image/rock.png')

directions_ant = DirectionnedImage(ant)
directions_red_ant = DirectionnedImage(red_ant)
directions_blue_ant = DirectionnedImage(blue_ant)

def bug_direction(bug):
    try:
        previous_direction = metas.value.get(PREVIOUS_DIRECTION, bug.get_id())
    except KeyError:
        previous_direction = 14
    return directions_ant.get_for_direction(previous_direction)

def red_ant_direction(bug):
    try:
        previous_direction = metas.value.get(PREVIOUS_DIRECTION, bug.get_id())
    except KeyError:
        previous_direction = 14
    return directions_red_ant.get_for_direction(previous_direction)

def blue_ant_direction(bug):
    try:
        previous_direction = metas.value.get(PREVIOUS_DIRECTION, bug.get_id())
    except KeyError:
        previous_direction = 14
    return directions_blue_ant.get_for_direction(previous_direction)

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