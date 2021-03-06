class Molecule():

    def __init__(self, category, type, distance=None, intensity=0, cycle_age=None):
        self._category = category
        self._type = type
        self._distance = distance
        self._intensity = intensity
        self._cycle_age = cycle_age

    def get_category(self):
        return self._category

    def get_type(self):
        return self._type

    def get_distance(self):
        return self._distance

    def set_distance(self, distance):
        self._distance = distance

    def get_intensity(self):
        return self._intensity

    def get_cycle_age(self):
        return self._cycle_age

    def set_cycle_age(self, cycle_age):
        self._cycle_age = cycle_age

    def increment_intensity(self, increment_value):
        self._intensity += increment_value
