import unittest

from os import getcwd
from sys import path as ppath
ppath.insert(1,getcwd()+'/modules') # TODO: win32 compatibilite (python path)

"""
python3.4 -m unittest /home/bux/Projets/socialintengine/intelligine/tests/simulation/mode/TestChangeMode.py && python3.4 -m unittest intelligine/tests/simulation/molecule/TestDirection.py
"""

test_modules = [
    'intelligine.tests.simulation.mode.TestChangeMode.TestChangeMode',
    'intelligine.tests.simulation.molecule.TestDirection.TestDirection',
    'intelligine.tests.simulation.bypass.TestByPass.TestByPass',
]

suite = unittest.TestSuite()

for t in test_modules:
    try:
        # If the module defines a suite() function, call it to get the suite.
        mod = __import__(t, globals(), locals(), ['suite'])
        suitefn = getattr(mod, 'suite')
        suite.addTest(suitefn())
    except (ImportError, AttributeError):
        # else, just load all the test cases from the module.
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))

test_result = unittest.TextTestRunner().run(suite)
if test_result.failures or test_result.errors:
    exit(1)