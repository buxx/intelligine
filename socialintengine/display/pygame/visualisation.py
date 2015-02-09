from xyworld.display.object.pygame.PygameImage import PygameImage
from xyworld.display.object.pygame.DirectionnedImage import DirectionnedImage
from socialintengine.synergy.object.Bug import Bug
from socialintengine.synergy.object.ant.Ant import Ant
from socialintengine.synergy.object.Rock import Rock
from os import getcwd
from synergine.metas import metas
from socialintengine.cst import PREVIOUS_DIRECTION

ant = PygameImage.from_filepath(getcwd()+'/socialintengine/display/pygame/image/ant.png')
bug = PygameImage.from_filepath(getcwd()+'/socialintengine/display/pygame/image/ant.png')
rock = PygameImage.from_filepath(getcwd()+'/socialintengine/display/pygame/image/rock.png')

directions_ant = DirectionnedImage(ant)

def bug_direction(bug):
    try:
        previous_direction = metas.value.get(PREVIOUS_DIRECTION, bug.get_id())
    except KeyError:
        previous_direction = 14
    return directions_ant.get_for_direction(previous_direction)

visualisation = {
    'window': {},
    'objects': {
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