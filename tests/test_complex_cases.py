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


class Test_Complex_Cases(TestCase):
    def setUp(self) -> None:
        self.c = Crispy()
        self.c.add_subcommand("add", "Adds two numbers")
        self.c.add_subcommand("subtract", "Subtracts two numbers")
        self.c.add_variable("number1", int)
        self.c.add_variable("number2", int)
    
    def test_add_numbers(self):
        expected = ("add", {"number1": 5, "number2": 3})
        actual = self.c.parse_string("add --number1=5 -N 3")
        self.assertEqual(expected, actual)
    
    def test_subtract_numbers(self):
        expected = ("subtract", {"number1": 5, "number2": 3})
        actual = self.c.parse_string("subtract --number1 5 -N=3")
        self.assertEqual(expected, actual)
    
    def test_subcommand_in_middle(self):
        expected = ("add", {"number1": 5, "number2": 3})
        actual = self.c.parse_string("--number1=5 add -N 3")
        self.assertEqual(expected, actual)
        
    def test_subcommand_at_end(self):
        expected = ("add", {"number1": 5, "number2": 3})
        actual = self.c.parse_string("--number1=5 -N 3 add")
        self.assertEqual(expected, actual)
    
    def test_graceful_error(self):
        with self.assertRaises(ParsingException) as context:
            # --number15 is not a valid key
            self.c.parse_string("add --number1 --number2=3")
        self.assertEqual("int type value", context.exception.expected)
        self.assertEqual(2, context.exception.at_position)
        self.assertEqual("--number2=3", context.exception.found)
    
    def test_graceful_error2(self):
        with self.assertRaises(ParsingException) as context:
            self.c.parse_string("subtract -n =5 --number2=3")
        self.assertEqual("int type value", context.exception.expected)
        self.assertEqual(2, context.exception.at_position)
        self.assertEqual("=5", context.exception.found)
