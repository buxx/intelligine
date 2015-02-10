from socialintengine.sandbox.redblue.RedColonyConfiguration import RedColonyConfiguration
from socialintengine.sandbox.redblue.BlueColonyConfiguration import BlueColonyConfiguration
from socialintengine.synergy.Colony import Colony
from socialintengine.synergy.Rocks import Rocks
from socialintengine.synergy.RocksConfiguration import RocksConfiguration

collections = [Colony(BlueColonyConfiguration()), Colony(RedColonyConfiguration()), Rocks(RocksConfiguration())]