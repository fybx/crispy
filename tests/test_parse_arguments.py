#
#   This file is part of the crispy-parser library.
#   Copyright (C) 2023  Ferit Yiğit BALABAN
#
#   This library is free software; you can redistribute it and/or
#   modify it under the terms of the GNU Lesser General Public
#   License as published by the Free Software Foundation; either
#   version 2.1 of the License, or (at your option) any later version.
#   
#   This library is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#   Lesser General Public License for more details.
#   
#   You should have received a copy of the GNU Lesser General Public
#   License along with this library; if not, write to the Free Software
#   Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
#   USA.


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

    def test_parse_arguments_case1(self):
        expected = {"name": "foo", "sex": False}
        actual = self.c.parse_arguments(["-n=foo"])
        self.assertEqual(expected, actual[1])

    def test_parse_arguments_case2(self):
        with self.assertRaises(UnexpectedArgumentException):
            self.c.parse_arguments(["--bool", "True"])

    def test_parse_arguments_case3(self):
        self.c = Crispy()
        self.c.add_variable("flag", bool)
        expected = {"flag": True}
        actual = self.c.parse_arguments(["--flag"])
        self.assertEqual(expected, actual[1])
        actual = self.c.parse_arguments(["-f"])
        self.assertEqual(expected, actual[1])

    def test_parse_arguments_case4(self):
        expected = {"name": "crispy", "sex": False}
        actual = self.c.parse_arguments(["--name", "crispy"])
        self.assertEqual(expected, actual[1])

    def test_parse_arguments_case5(self):
        expected = {"sex": False, "name": "John"}
        actual = self.c.parse_arguments(["-n=John"])
        self.assertEqual(expected, actual[1])

    def test_parse_arguments_case6(self):
        expected = {"sex": True, "name": "John", "age": 15}
        actual = self.c.parse_arguments(["--name", "John", "--age=15", "-s"])
        self.assertEqual(expected, actual[1])

    def test_parse_arguments_case7(self):
        expected = {"sex": False, "name": "John"}
        actual = self.c.parse_arguments(["--sex=False", "--name=John"])
        self.assertEqual(expected, actual[1])

    def test_parse_arguments_case8(self):
        expected = {"sex": True, "name": "John", "age": 15}
        actual = self.c.parse_arguments(["-n=John", "-s=True", "--age=15"])
        self.assertEqual(expected, actual[1])

    def test_parse_arguments_case9(self):
        expected = {"sex": True, "name": "John", "age": 15}
        actual = self.c.parse_arguments(["--name", "John", "-s", "--age=15"])
        self.assertEqual(expected, actual[1])

    def test_parse_arguments_case10(self):
        expected = {"sex": True, "name": "John", "age": 15}
        actual = self.c.parse_arguments(["-s", "--name", "John", "--age=15"])
        self.assertEqual(expected, actual[1])

    def test_parse_arguments_case11(self):
        expected = {"sex": True, "name": "John", "age": 14}
        actual = self.c.parse_arguments(["-a", "14", "-n=John", "-s"])
        self.assertEqual(expected, actual[1])

    def test_parse_arguments_case12(self):
        expected = {"sex": True, "name": "John", "age": 14}
        actual = self.c.parse_arguments(["-s", "-a", "14", "-n=John"])
        self.assertEqual(expected, actual[1])

    def test_parse_arguments_case13(self):
        expected = {"sex": True, "name": "John", "age": 14}
        actual = self.c.parse_arguments(["-n=John", "-s", "-a", "14"])
        self.assertEqual(expected, actual[1])

    def test_parse_arguments_case14(self):
        expected = {"name": "foo", "sex": False}
        actual = self.c.parse_arguments(["--name=foo"])
        self.assertEqual(expected, actual[1])

    def test_parse_arguments_case15(self):
        expected = {"name": "crispy", "sex": False}
        actual = self.c.parse_arguments(["-n", "crispy"])
        self.assertEqual(expected, actual[1])

    def test_parse_arguments_case16(self):
        with self.assertRaises(MissingValueException):
            self.c.parse_arguments(["--name", "-s"])

    def test_parse_arguments_case17(self):
        with self.assertRaises(MissingValueException):
            self.c.parse_arguments(["-a=15", "--name", "-s"])

    def test_parse_arguments_case18(self):
        with self.assertRaises(MissingValueException):
            self.c.parse_arguments(["-a", "--name", "-s"])
