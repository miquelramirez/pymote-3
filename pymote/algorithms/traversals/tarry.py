from pymote.logger import logger
from pymote.algorithm import NodeAlgorithm
from pymote.message import Message
import numpy as np

class Tarry(NodeAlgorithm):
    required_params = ('initiator',)
    default_params = {'neighbors': 'neighbors', 'z': 'z', 'parent': 'parent', 'fwd' : 'fwd'}


    def initializer(self):
        ini_nodes = []
        for node in self.network.nodes():
            node.memory[self.neighbors] = \
                list(node.compositeSensor.read()['Neighbors'])
            node.memory[self.fwd] = [False for n in node.memory[self.neighbors]]
            node.status = 'LISTENING'
            node.memory[self.z] = (900)*np.random.rand() + 100
            print('Node(id={},z={})'.format(node.id, node.memory[self.z]))
            if self.initiator in node.memory:
                node.status = 'INITIATOR'
                ini_nodes.append(node)
        for ini_node in ini_nodes:
            self.network.outbox.insert(0, Message(header=NodeAlgorithm.INI,
                                                 destination=ini_node))
    def initiate(self, node, message):
        node.memory[self.fwd][0] = True
        print('Node(id={}) is initator, sends token...'.format(node.id))
        node.send(Message(header='TOKEN',
                    data=node.memory[self.z],
                    destination=node.memory[self.neighbors][0]))
        node.memory[self.fwd][0] = True
        node.status = 'LISTENING'

    def listening(self, node, message):
        if message.header == 'TOKEN':
            print('Node(id={}) receives token...'.format(node.id))
            if self.initiator in node.memory:
                node.status = 'DONE'
                print('Decision: z={} m'.format(message.data))
                return
            node.memory[self.parent] = message.source
            payload = max(node.memory[self.z], message.data)
            forwarded = False
            for k in range(len(node.memory[self.neighbors])):
                if not node.memory[self.fwd][k]:
                    node.memory[self.fwd][k] = True
                    node.send(Message(header='TOKEN',
                                data=payload,
                                destination=node.memory[self.neighbors][k]))
                    forwarded = True
                    break
            if not forwarded:
                node.send(Message(header='TOKEN',
                            data=payload,
                            destination=node.memory[self.parent]))

    def done(self, node, message):
        pass


    STATUS = {
        'INITIATOR' : initiate,
        'DONE' : done,
        'LISTENING' : listening
    }
