from intelligine.synergy.Colony import Colony
from intelligine.synergy.Environment import Environment
from intelligine.synergy.Simulation import Simulation
from intelligine.synergy.object.Food import Food
from intelligine.synergy.object.Rock import Rock
from intelligine.synergy.object.ant.Ant import Ant
from intelligine.synergy.object.ant.Egg import Egg


def stocked_food(food):
    food.transform_to_stocked()

map_config = {
    'simulation': {
        'base': Simulation
    },
    'collection': {
        'ant': Colony,
        'env': Environment
    },
    'object': {
        'ant': Ant,
        'egg': Egg,
        'rock': Rock,
        'food': Food,
        'stocked_food': Food
    },
    'callbacks': {
        'stocked_food': [stocked_food]
    }
}