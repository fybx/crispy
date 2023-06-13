#
#       Ferit Yiğit BALABAN,    <fybalaban@fybx.dev>
#       crispy                  2023
#
#       test_parse_arguments.py
from unittest import TestCase
from crispy.crispy import Crispy
from crispy.missing_value_exception import MissingValueException
from crispy.unexpected_argument_exception import UnexpectedArgumentException


class Test_Parse_Arguments(TestCase):
    def setUp(self) -> None:
        self.c = Crispy()
        self.c.add_variable("name", str)
        self.c.add_variable("age", int)
        self.c.add_variable("sex", bool)
