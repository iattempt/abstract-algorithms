import unittest
from random import random, randint

from lib.sort import (
    insertion_sort,
    selection_sort,
    bubble_sort,
)
from lib.tree import Node
from lib.design_pattern import Decorator


class TestSort(unittest.TestCase):

    def test_bubble_sort(self):
        self.__test_n_square_complexity_sort(bubble_sort)

    def test_selection_sort(self):
        self.__test_n_square_complexity_sort(selection_sort)

    def test_insertion_sort(self):
        self.__test_n_square_complexity_sort(insertion_sort)

    def __test_n_square_complexity_sort(self, sort):
        self.__test_sort_boundary(sort)
        self.__test_sort_in_median_size(sort)
        self.__test_sort_reversed(sort)

    def __test_n_log_n_complexity_sort(self, sort):
        self.__test_n_square_complexity_sort(sort)
        self.__test_sort_in_large_size(sort)

    def __test_sort_reversed(self, sort):
        self.__test_sort_boundary(sort)
        self.__test_sort_boundary(sort, reverse=True)
        self.__test_sort_boundary(sort, reverse=False)

    def __test_sort_boundary(self, sort, **kwargs):
        self.__test_sort_in_range(sort, range(0, 10**1), **kwargs)

    def __test_sort_in_median_size(self, sort, **kwargs):
        self.__test_sort_in_range(sort, range(10**1, 10**2), **kwargs)

    def __test_sort_in_large_size(self, sort, **kwargs):
        self.__test_sort_in_range(sort, range(10**3, 10**10), **kwargs)

    def __test_sort_in_range(self, sort, range_, **kwargs):
        self.__test_sort_in_range_default(sort, range_, **kwargs)
        self.__test_sort_in_range_with_custom_less(sort, range_, **kwargs)
        self.__test_sort_in_range_with_custom_swap_only_property(
            sort, range_, **kwargs)

    def __test_sort_in_range_default(self, sort, range_, **kwargs):
        for size in range_:
            shuffle_list = self.__get_random_list(size)
            sort_list = sorted(shuffle_list)
            actual = shuffle_list
            sort(actual, **kwargs)
            if kwargs.get('reverse', False) is True:
                self.assertEqual(sort_list[::-1], actual)
            else:
                self.assertEqual(sort_list, actual)

    def __test_sort_in_range_with_custom_less(self, sort, range_, **kwargs):
        for size in range_:
            shuffle_list = self.__get_random_embedded_list(size)
            sort_list = sorted(shuffle_list, key=lambda x: x[1])
            actual = shuffle_list
            kwargs['less_closure'] = lambda a, b: a[1] < b[1]
            sort(actual, **kwargs)
            if kwargs.get('reverse', False) is True:
                self.assertListEqualByKey(
                    sort_list[::-1], actual, lambda x: x[1])
            else:
                self.assertListEqualByKey(sort_list, actual, lambda x: x[1])

    def __test_sort_in_range_with_custom_swap_only_property(
            self, sort, range_, **kwargs):
        for size in range_:
            shuffle_list = self.__get_random_embedded_node(size)
            sort_list = sorted(shuffle_list, key=lambda x: x.value)
            actual = []
            for node in shuffle_list:
                actual.append(node.copy())
            # test no-effect step1: append id to each node as its index of list
            for index in range(len(actual)):
                actual[index].id = index
            kwargs['swap_closure'] = swap_node_value
            kwargs['less_closure'] = lambda a, b: a.value < b.value
            sort(actual, **kwargs)
            if kwargs.get('reverse', False) is True:
                self.assertListEqualByKey(
                    sort_list[::-1], actual, lambda x: x.value)
            else:
                self.assertListEqualByKey(sort_list, actual, lambda x: x.value)
            # test no-effect step2: test node is not exchanged
            for index, node in enumerate(actual):
                self.assertEqual(index, node.id)

    def assertListEqualByKey(self, list1, list2, key_closure):
        self.assertEqual(len(list1), len(list2))
        for i in range(len(list1)):
            self.assertEqual(key_closure(list1[i]), key_closure(list2[i]))

    def __get_random_list(self, size):
        """
        size: int
        return: list[int]
        """
        list_ = []
        while len(list_) < size:
            # continuous
            if random() < 0.5:
                # duplicate
                while True and len(list_) < size:
                    list_.append(randint(0, size))
                    if random() < 0.5:
                        break
        return list_

    def __get_random_embedded_list(self, size):
        """
        size: int
        return: list[list[int]]
        """
        list_ = []
        while len(list_) < size:
            # continuous
            if random() < 0.5:
                # duplicate
                while True and len(list_) < size:
                    list_.append([randint(0, size), randint(0, size)])
                    if random() < 0.5:
                        break
        return list_

    def __get_random_embedded_node(self, size):
        """
        size: int
        return: list[Node]
        """
        list_ = []
        while len(list_) < size:
            # continuous
            if random() < 0.5:
                # duplicate
                while True and len(list_) < size:
                    list_.append(InfoNodeDecorator(Node(randint(0, size))))
                    if random() < 0.5:
                        break
        return list_


class InfoNodeDecorator(Decorator):

    def __init__(self, base):
        super().__init__(base)
        self.__id = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id_):
        self.__id = id_

    def copy(self):
        copied_node = self.decorated_class.copy()
        copied_node = InfoNodeDecorator(copied_node)
        copied_node.id = self.__id
        return copied_node


def swap_node_value(iterative, index_a, index_b):
    iterative[index_a].value, iterative[index_b].value = (
        iterative[index_b].value, iterative[index_a].value)
