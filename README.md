[![Build Status](https://travis-ci.org/buxx/intelligine.svg?branch=master)](https://travis-ci.org/buxx/intelligine) - [![Coverage Status](https://coveralls.io/repos/buxx/intelligine/badge.svg?branch=master)](https://coveralls.io/r/buxx/intelligine?branch=master) - [![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/buxx/intelligine/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/buxx/intelligine/?branch=master) - [![Stories in Ready](https://badge.waffle.io/buxx/intelligine.png?label=ready&title=Ready)](https://waffle.io/buxx/intelligine)

# intelligine 

Social intelligence (/Ant colony) simulation.

## Links

* Tracker: [http://work.bux.fr/projects/intelligine/](http://work.bux.fr/projects/intelligine/)
* Forum: [http://work.bux.fr/projects/intelligine/boards](http://work.bux.fr/projects/intelligine/boards)

## Install

Project is not ready, but if you want to test it you will need:

* python3.4+
* pygame (see [here](http://www.pygame.org/wiki/CompileUbuntu#Python%203.x) for pygame python3 installation)
* requirements.txt dependencies (install them with pip install -r requirements.txt)

Then run ``python3.4 run.py exploration`` or ``python3.4 run.py all``. Keep in mind it's in developpment mode !

### Graphic keys

On current default graphic output, following keys can be used:

* Z: Zoom
* A: Unzoom
* Left,Right,...: Move screen
* M: Display/Hide molecules

## Quick test with Docker

Allow the docker user to communicate with your X session with ``xhost +local:docker`` then run (assuming docker installed) ``docker run -w /intelligine -v /tmp/.X11-unix:/tmp/.X11-unix -v /dev/snd:/dev/snd --privileged -e DISPLAY buxx/intelligine python3.4 run.py exploration``

## Screens

### Egg management

[![Intelligine: egg management](https://raw.githubusercontent.com/buxx/intelligine/master/doc/images/intelligine_eggs_20150421.gif)](https://raw.githubusercontent.com/buxx/intelligine/master/doc/images/intelligine_eggs_20150421.gif) 

### Ressource exploration

[![Intelligine: ressource exploration](https://raw.githubusercontent.com/buxx/intelligine/master/doc/images/intelligine_ressource_20150421_r.gif)](https://raw.githubusercontent.com/buxx/intelligine/master/doc/images/intelligine_ressource_20150421_r.gif) 
[![Intelligine: ressource exploration with AntStar algo for bypass](https://raw.githubusercontent.com/buxx/intelligine/dev/mol/doc/images/explo_antstar_glue.gif)](https://raw.githubusercontent.com/buxx/intelligine/dev/mol/doc/images/explo_antstar_glue.gif)
