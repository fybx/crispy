#
#       Ferit Yiğit BALABAN,    <fybalaban@fybx.dev>
#       crispy                  2023
#
#       test_add_variable.py
from unittest import TestCase
from crispy.crispy import Crispy
from crispy.duplicate_name_exception import DuplicateNameException


class Test_Add_Variable(TestCase):
    def setUp(self) -> None:
        self.c = Crispy()
        self.c.add_variable("name", str)
        self.c.add_variable("age", int)
        self.c.add_variable("addr", str)

    def test_add_variable_with_unique_name(self):
        self.assertEqual(self.c.variables["name"], str)
        self.assertEqual(self.c.accepted_keys["--name"], "name")

