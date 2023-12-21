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
from crispy.parsing_exception import ParsingException


class TestPositionalArguments(TestCase):
    def setUp(self) -> None:
        self.c = Crispy()
        self.c.add_positional("name", str, 0)
        self.c.add_positional("age", int, 1)
        self.c.add_variable("is_student", bool)
        self.c.add_variable("height", float)
        self.c.add_subcommand("create", "creates the user")
        return super().setUp()

    def test_correct_order(self):
        expected = ("", {
            "name": "Ferit",
            "age": 21,
            "is_student": False
        })
        actual = self.c.parse_string("Ferit 21")
        self.assertEqual(expected, actual)
        
    
    def test_type_mismatch(self):
        with self.assertRaises(ParsingException) as context:
            self.c.parse_string("21 Ferit")
        self.assertEqual(context.exception.expected, str)
        self.assertEqual(context.exception.at_position, 0)
        self.assertEqual(context.exception.found, int)
    
    def test_with_keys(self):
        expected = ("", {
            "name": "Ferit",
            "age": 21,
            "is_student": True,
            "height": 1.86
            })
        actual1 = self.c.parse_string("Ferit 21 --is_student --height=1.86")
        actual2 = self.c.parse_string("--is_student --height=1.86 Ferit 21")
        actual3 = self.c.parse_string("--height 1.86 Ferit -i 21")
        actual4 = self.c.parse_string("-h 1.86 Ferit 21 -i")
        self.assertEqual(expected, actual1)
        self.assertEqual(expected, actual2)
        self.assertEqual(expected, actual3)
        self.assertEqual(expected, actual4)
    
    def test_with_subcommand(self):
        pass
    
    def test_fail_with_keys_and_subcommand(self):
        pass
    
    def test_pass_with_keys_and_subcommand(self):
        pass