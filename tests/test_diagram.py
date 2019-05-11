# -*- coding: utf-8 -*-

import json, os, unittest
from workflow.diagram import Diagram,FlowNode

class ModelTestSuite(unittest.TestCase):
    def test_simple(self):

        d = Diagram("Simple")

        n1 = FlowNode("1")
        n2 = FlowNode("2")
        n3 = FlowNode("3")

        d += n1 >> n2 >> n3

        self.assertEqual(3, len(d.nodes))

        self.assertEqual(0, len(n1.incoming))
        self.assertEqual(1, len(n2.incoming))
        self.assertEqual(1, len(n3.incoming))

        self.assertEqual(1, len(n1.outgoing))
        self.assertEqual(1, len(n2.outgoing))
        self.assertEqual(0, len(n3.outgoing))

if __name__ == '__main__':
    unittest.main()
