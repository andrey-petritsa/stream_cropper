import unittest

import refactor.language.module


class ImportantClass():
    def __init__(self):
        self.__state = refactor.language.module.state

    def get_state(self):
        return self.__state

class Increment():
    counter = 0

    def increment(self):
        self.counter += 1
        return self.counter

class ListInClass():
    def __init__(self):
        self.list = []

class StringInClass():
    def __init__(self):
        self.string = 'hello'

class SayHello():
    def say(self):
        return 'hello'

class SayBye():
    def say(self):
        return 'bye'


class TestMutate(unittest.TestCase):
    def test_mutate(self):
        obj = ImportantClass()
        refactor.language.module.state = 'hello 123'

        self.assertEqual('hello', obj.get_state())

    def test_pointers(self):
        p1 = 1
        p2 = p1
        p2 = 5
        self.assertEqual(p2, 1)

    def test_list(self):
        a = ['hello']
        b = a
        b.append('world')

        self.assertEqual(2, len(a))

    def test_list_in_class(self):
        a = ListInClass()
        a.list.append('hello')
        b = a
        b.list.append('world')

        self.assertEqual(['hello', 'world'], a.list)

    def test_string_in_class(self):
        a = StringInClass()
        b = a
        a = ListInClass()
        b.string = 'hello world'

        self.assertEqual("hello world", b.string)

    def test_var_replace(self):
        a = "RealWebClient()"
        b = a
        a = "MockWebClient"

        self.assertEqual("MockWebClient", b)

    def test_2_var_replace(self):
        a = ["RealWebClient"]
        b = a
        a[0] = 'MockWebClient'

        self.assertEqual("MockWebClient", b[0])

    def test_3_var_replace(self):
        a = SayHello()
        b = a
        a = SayBye()

        self.assertEqual("bye", b.say())






