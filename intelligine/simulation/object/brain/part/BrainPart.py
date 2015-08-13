class BrainPart():

    def __init__(self, host_brain):
        self._host_brain = host_brain
        self._context = self._host_brain.get_context()
        self._host = self._host_brain.get_host()

    def get_host_brain(self):
        return self._host_brain

    def get_host(self):
        return self.get_host_brain().get_host()

    def done(self):
        pass