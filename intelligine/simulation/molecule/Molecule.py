class Molecule():

    def __init__(self, category, type, distance=None, intensity=0):
        self._category = category
        self._type = type
        self._distance = distance
        self._intensity = intensity

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

    def increment_intensity(self, increment_value):
        self._intensity += increment_value