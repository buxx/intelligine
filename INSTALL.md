INSTALL
=====================

Windows
--------------------

(dirty tmp howto)

Install python 3.4+: https://www.python.org/downloads/
Install Git: http://git-scm.com/download/win

Execute command 
````
C:\Python34\python -m pip install pytmx
````
Install pygame for python3.4: Download pygame‑1.9.2a0‑cp34‑none‑win32.whl on http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame

Execute command 
````
C:\Python34\python -m pip install "Downloads\pygame-1.9.2a0-cp34-none-win32.whl"
````
Launch Git Bash program and execute command 
````
mkdir ant
````

Execute command 
````
git clone https://github.com/buxx/synergine.git ant/synergine
````

Execute command 
````
git clone https://github.com/buxx/intelligine.git ant/intelligine
````

Open Cmd and execute commands 
````
cd ant\intelligine\modules
rmdir synergine
rmdir xyzworld
rmdir xyworld
mklink /j synergine ..\..\synergine\synergine
mklink /j xyzworld ..\..\synergine\modules\xyzworld
mklink /j xyworld ..\..\synergine\modules\xyworld
````

Open new Cmd:
````
cd ant\intelligine
C:\Python34\python run.py
````
