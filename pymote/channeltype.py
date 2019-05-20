from pymote.conf import settings
from numpy import sqrt
from numpy.random import random


class ChannelType(object):
    """ChannelType abstract base class."""

    @classmethod
    def create(cls, environment=None, **kwargs):

        for sub in cls.__subclasses__():
            if sub.__name__ == settings.CHANNEL_TYPE:
                return sub(environment)

        return ChannelType(environment)

    def in_comm_range(self, network, node1, node2):
        raise NotImplementedError


class Udg(ChannelType):
    """Unit disc graph channel type."""

    def __init__(self, environment):
        self.environment = environment

    def in_comm_range(self, network, node1, node2):
        """Two nodes are in communiocation range if they can see each other and
        are positioned so that their distance is smaller than commRange."""
        p1 = network.pos[node1]
        p2 = network.pos[node2]
        d = sqrt(sum(pow(p1 - p2, 2)))
        if (d < node1.commRange and d < node2.commRange):
            if (self.environment.are_visible(p1, p2)):
                return True
        return False


class SquareDisc(ChannelType):
    """ Probability of connection is 1-d^2/r^2 """

    def __init__(self, environment):
        self.environment = environment

    def in_comm_range(self, network, node1, node2):
        p1 = network.pos[node1]
        p2 = network.pos[node2]
        d = sqrt(sum(pow(p1 - p2, 2)))
        if random() > d ** 2 / node1.commRange ** 2:
            if (self.environment.are_visible(p1, p2)):
                assert node1.commRange == node2.commRange
                return True
        return False
