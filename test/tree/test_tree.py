import unittest
from random import random
from lib.tree import Node
from lib.tree import BinaryTree
from lib.tree import NodeTraversalAdapter


class TestNode(unittest.TestCase):

    def test_init(self):
        node = Node()
        self.assertEqual(node.value, None)
        self.assertEqual(node.left, None)
        self.assertEqual(node.right, None)
        r = random()
        node = Node(r)
        self.assertEqual(node.value, r)
        self.assertEqual(node.left, None)
        self.assertEqual(node.right, None)

    def test_value_property(self):
        r = random()
        node = Node()
        node.value = r
        self.assertEqual(node.value, r)

    def test_left_property(self):
        r = random()
        node = Node()
        left_node = Node(r)
        node.left = left_node
        self.assertEqual(node.left, left_node)

    def test_right_property(self):
        r = random()
        node = Node()
        right_node = Node(r)
        node.right = right_node
        self.assertEqual(node.right, right_node)


class TestBinaryTree(unittest.TestCase):

    def test_insert(self):
        bt = BinaryTree()
        bt.insert(Node(3))
        bt.insert(Node(1))
        bt.insert(Node(5))
        self.assertLess(bt.root.value, bt.root.right.value)
        self.assertLess(bt.root.left.value, bt.root.value)


"""
                  10
          /                \
         5                  15
     /       \            /     \
    2         8         13       17
   / \       / \       /  \     /  \
  N   4     6   N    12    N   N    18
     / \   / \      /  \           /  \
    3   N N   7    11   N         N    19
"""
bt = BinaryTree()
n10 = Node(10)
n5 = Node(5)
n2 = Node(2)
n4 = Node(4)
n3 = Node(3)
n8 = Node(8)
n6 = Node(6)
n7 = Node(7)
n15 = Node(15)
n13 = Node(13)
n12 = Node(12)
n11 = Node(11)
n17 = Node(17)
n18 = Node(18)
n19 = Node(19)
bt.insert(n10)
bt.insert(n5)
bt.insert(n2)
bt.insert(n4)
bt.insert(n3)
bt.insert(n8)
bt.insert(n6)
bt.insert(n7)
bt.insert(n15)
bt.insert(n13)
bt.insert(n12)
bt.insert(n11)
bt.insert(n17)
bt.insert(n18)
bt.insert(n19)


class TestTreeTraversalAdapter(unittest.TestCase):

    def test_level_traversal(self):
        self.assertEqual(NodeTraversalAdapter(bt.root).level_traversal(),
                         [n10, n5, n15, n2, n8, n13, n17, None, n4, n6, None,
                          n12, None, None, n18, n3, None, None, n7, n11,
                          None, None, n19])

    def test_pre_order_traversal(self):
        self.assertEqual(NodeTraversalAdapter(bt.root).pre_order_traversal(),
                         [n10, n5, n2, None, n4, n3, None, n8, n6, None,
                          n7, None, n15, n13, n12, n11, None, None, n17,
                          None, n18, None, n19])

    def test_in_order_traversal(self):
        self.assertEqual(NodeTraversalAdapter(bt.root).in_order_traversal(),
                         [None, n2, n3, n4, None, n5, None, n6, n7, n8, None,
                          n10, n11, n12, None, n13, None, n15, None, n17, None,
                          n18, n19])

    def test_post_order_traversal(self):
        self.assertEqual(NodeTraversalAdapter(bt.root).post_order_traversal(),
                         [None, n3, None, n4, n2, None, n7, n6, None, n8, n5,
                          n11, None, n12, None, n13, None, None, n19, n18, n17,
                          n15, n10])
