
from .process import Process,Step
from .diagram import JoinNode


class Engine:
    """A Process Engine"""

    def __init__(self,diagram):
        self.diagram = diagram
        self.process = Process()


    def shouldCompleteJoinNode(self,join):
        active_steps = self.process.activeSteps()
        incoming = join.incoming
        for in_id in incoming:
            incoming_nodes = list(filter(lambda n: in_id in n.outgoing, self.diagram.nodes))
            for node in incoming_nodes:
                for step in active_steps:
                        while step is not None:
                            if step.node_id == join.id:
                                # Looped. Good to contine
                                break
                            elif step.node_id == node.id:
                                return False
                            step = self.process[step.prior_step_id]
        return True

    def shouldCompleteNodeStep(self,node):
        if type(node) is JoinNode:
            return self.shouldCompleteJoinNode(node)
        return False

    def startNode(self, n, prior_step_id = None):
        step = Step(n.id, prior_step_id)
        self.process += step
        if self.shouldCompleteNodeStep(n):
            self.completeStep(step)

    def completeStep(self, step):
        step.completeStep()
        self.startOutgoing(self.diagram[step.node_id],step.id)


    def startOutgoing(self, node,prior_step_id):
        for id in node.outgoing:
            out_node = self.diagram[id]
            active_step_for_node = self.process.getActiveStepForNode(id)
            if active_step_for_node is None:
                self.startNode(out_node,prior_step_id)
            elif self.shouldCompleteNodeStep(out_node):
                self.completeStep(active_step_for_node)
