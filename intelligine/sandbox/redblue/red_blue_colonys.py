from intelligine.sandbox.redblue.RedColonyConfiguration import RedColonyConfiguration
from intelligine.sandbox.redblue.BlueColonyConfiguration import BlueColonyConfiguration
from intelligine.synergy.Colony import Colony
from intelligine.synergy.Rocks import Rocks
from intelligine.synergy.RocksConfiguration import RocksConfiguration

collections = [Colony(BlueColonyConfiguration()), Colony(RedColonyConfiguration()), Rocks(RocksConfiguration())]