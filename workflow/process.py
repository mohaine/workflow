import uuid

class Process:
    """A Process"""
    def __init__(self):
        self.id = uuid.uuid4()
        self.steps = []

    def __repr__(self):
        return "Process({})".format(self.id)

    def __iadd__(self, other):
        self.steps.append(other)
        return self

    def activeSteps(self):
        return list(filter(lambda s: not s.complete, self.steps))

    def getActiveStepForNode(self, id):
        for s in self.steps:
            if not s.complete and s.node_id == id:
                return s

        return None

    def __getitem__(self, id):
        if id is not None:
            for n in self.steps:
                if n.id == id:
                    return n
        return None


class Step:
    """A Step in a Process"""
    def __init__(self, node_id, prior_step_id):
        self.id = uuid.uuid4()
        self.node_id = node_id
        self.complete = False
        self.prior_step_id = prior_step_id

    def __repr__(self):
        return "Step({})".format(self.node_id)

    def completeStep(self):
        if self.complete:
            raise "Step is already complete"
        self.complete = True
