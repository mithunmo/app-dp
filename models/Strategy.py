import abc

class Strategy(object):
    """
    Declare an interface common to all supported algorithms. Context
    uses this interface to call the algorithm defined by a
    ConcreteStrategy.
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def output_interface(self, person):
        raise NotImplementedError
