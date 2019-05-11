import uuid

class Node:
    """A Diagram Node"""
    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name

    def __str__(self):
        return "Node({})".format(self.name)

class Diagram(Node):
    """Diagram """
    def __init__(self, name):
        Node.__init__(self,name)
        self.nodes = set()

    def __iadd__(self, other):
        self.nodes.update(other.nodes)
        return self


class _NodeAccumulator:
    def __init__(self, node):
        self.nodes = set()
        self.current = node
        self.nodes.add(node)

    def __rshift__(self, next):
        print("{} -> {}".format(self.current, next))
        self.current.transition(next)
        self.nodes.add(next)
        self.current = next
        return self

class FlowNode(Node):
    """FlowNode """
    def __init__(self, name):
        Node.__init__(self,name)
        self.outgoing = []
        self.incoming = []

    def transition(self,next):
        self.outgoing.append(next.id)
        next.incoming.append(self.id)

    def __rshift__(self, next):
        accum = _NodeAccumulator(self)
        return accum >> next

    def __str__(self):
        return "Flow({})".format(self.name)
