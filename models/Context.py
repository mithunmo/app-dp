class Context(object):
    """
    Define the interface of interest to clients.
    Maintain a reference to a Strategy object.
    """
    def __init__(self, strategy):
        self._strategy = strategy

    def context_interface(self, person):
        self._strategy.output_interface(person)

