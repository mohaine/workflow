# -*- coding: utf-8 -*-

import json, os, unittest
from workflow.diagram import Diagram,FlowNode,JoinNode
from workflow.engine import Engine


class ModelTestSuite(unittest.TestCase):
    def test_simple(self):
        d = Diagram("Simple")

        n1 = FlowNode("1")
        n2 = FlowNode("2")
        n3 = FlowNode("3")

        d += n1 >> n2 >> n3

        e = Engine(d)
        e.startNode(n1)
        p = e.process

        self.assertEqual(1, len(p.activeSteps()))
        active_step = p.activeSteps()[0]
        self.assertEqual(n1.id, active_step.node_id)
        e.completeStep(active_step)

        self.assertEqual(1, len(p.activeSteps()))
        active_step = p.activeSteps()[0]
        self.assertEqual(n2.id, active_step.node_id)
        e.completeStep(active_step)

        self.assertEqual(1, len(p.activeSteps()))
        active_step = p.activeSteps()[0]
        self.assertEqual(n3.id, active_step.node_id)
        e.completeStep(active_step)

        self.assertEqual(0, len(p.activeSteps()))

    def test_join(self):
        d = Diagram("Simple")

        n1 = FlowNode("1")
        n2a = FlowNode("2a")
        n2b = FlowNode("2b")
        n3 = JoinNode("J3")
        n4 = FlowNode("4")

        d += n1 >> n2a >> n3
        d += n1 >> n2b >> n3
        d += n3 >> n4

        e = Engine(d)
        e.startNode(n1)
        p = e.process

        self.assertEqual(1, len(p.activeSteps()))
        active_step = p.activeSteps()[0]
        self.assertEqual(n1.id, active_step.node_id)
        e.completeStep(active_step)

        self.assertEqual(2, len(p.activeSteps()))
        active_step_a = list(filter(lambda s: s.node_id == n2a.id, p.activeSteps()))[0]
        active_step_b = list(filter(lambda s: s.node_id == n2b.id, p.activeSteps()))[0]
        self.assertEqual(n2a.id, active_step_a.node_id)
        self.assertEqual(n2b.id, active_step_b.node_id)

        e.completeStep(active_step_a)

        self.assertEqual(2, len(p.activeSteps()))
        active_step = p.activeSteps()[0]
        active_step_join = list(filter(lambda s: s.node_id == n3.id, p.activeSteps()))[0]
        self.assertEqual(n3.id, active_step_join.node_id)

        e.completeStep(active_step_b)
        self.assertEqual(1, len(p.activeSteps()))
        active_step = p.activeSteps()[0]
        self.assertEqual(n4.id, active_step.node_id)

        e.completeStep(active_step)
        self.assertEqual(0, len(p.activeSteps()))


if __name__ == '__main__':
    unittest.main()
