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
from crispy.duplicate_name_exception import DuplicateNameException
from crispy.too_many_subcommands_exception import TooManySubcommandsException

class Test_Subcommands(TestCase):
    def setUp(self):
        self.c = Crispy()
        self.c.add_subcommand('add', 'adds two numbers given by keys -a and -b')
        self.c.add_subcommand('test', 'to test toomanysubcommands exception')
        self.c.add_variable('a', int)
        self.c.add_variable('b', int)

    def test_add_subcommand(self):
        self.c.add_subcommand('test2', 'description of subcommand test')
        self.assertEqual(self.c.subcommands['test2'], 'description of subcommand test')

    def test_add_duplicate_subcommand(self):
        with self.assertRaises(DuplicateNameException):
            self.c.add_subcommand('add', 'the description can change')

    def test_parse_subcommand_from_list(self):
        actual = self.c.parse_arguments(['add', '-a=5', '-b=10'])
        self.assertEqual(actual[0], 'add')
        self.assertDictEqual(actual[1], {'a': 5, 'b': 10})
    
    def test_parse_subcommand_from_string(self):
        actual = self.c.parse_string('add -a=5 -b=10')
        self.assertEqual(actual[0], 'add')
        self.assertDictEqual(actual[1], {'a': 5, 'b': 10})

    def test_parse_none(self):
        actual = self.c.parse_string('-a=5 -b=10')
        self.assertEqual(actual[0], '')
        self.assertDictEqual(actual[1], {'a': 5, 'b': 10})

    def test_deny_many_subcommands(self):
        with self.assertRaises(TooManySubcommandsException):
            self.c.parse_arguments(['add', 'test', '-a=5', '-b=10'])
    

