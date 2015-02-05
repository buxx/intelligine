from xyworld.display.object.pygame.PygameImage import PygameImage
from socialintengine.synergy.object.Bug import Bug
from socialintengine.synergy.object.ant.Ant import Ant
from socialintengine.synergy.object.Rock import Rock
from os import getcwd

# TODO: Url relative au fichier
ant = PygameImage(getcwd()+'/socialintengine/display/pygame/image/ant.png')
bug = PygameImage(getcwd()+'/socialintengine/display/pygame/image/bug.png')
rock = PygameImage(getcwd()+'/socialintengine/display/pygame/image/rock.png')

visualisation = {
    'window': {},
    'objects': {
        Ant: {
            'default': ant
        },
        Bug: {
            'default': bug
        },
        Rock: {
            'default': rock
        }
    }
}