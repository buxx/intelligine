from intelligine.sandbox.colored.RedColonyConfiguration import RedColonyConfiguration
from intelligine.sandbox.colored.BlueColonyConfiguration import BlueColonyConfiguration
from intelligine.sandbox.colored.GreenColonyConfiguration import GreenColonyConfiguration
from intelligine.synergy.Colony import Colony
from intelligine.synergy.Rocks import Rocks
from intelligine.synergy.RocksConfiguration import RocksConfiguration

collections = [Colony(BlueColonyConfiguration()), \
               Colony(RedColonyConfiguration()), \
               Colony(GreenColonyConfiguration()), \
               Rocks(RocksConfiguration())]