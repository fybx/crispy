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


class Test_Add_Variable(TestCase):
    def setUp(self) -> None:
        self.c = Crispy()
        self.c.add_variable("name", str)
        self.c.add_variable("age", int)
        self.c.add_variable("addr", str)

    def test_add_variable_with_unique_name(self):
        self.assertEqual(self.c.variables["name"], str)
        self.assertEqual(self.c.accepted_keys["--name"], "name")

    def test_add_variable_with_duplicate_name(self):
        with self.assertRaises(DuplicateNameException):
            self.c.add_variable("name", str)

    def test_add_variable_with_unique_shortform(self):
        self.assertEqual(self.c.variables["name"], str)
        self.assertEqual(self.c.accepted_keys["-n"], "name")

    def test_add_variable_with_duplicate_shortform(self):
        expected = {"-A": "addr", "--addr": "addr", "-a": "age", "--age": "age", "-n": "name", "--name": "name"}
        self.assertEqual(expected, self.c.accepted_keys)

    def test_add_variable_without_accepting_shortform(self):
        self.c = Crispy(accept_shortform=False)
        self.c.add_variable("name", str)
        self.assertDictEqual(self.c.accepted_keys, {"--name": "name"})

    def test_add_variable_without_accepting_longform(self):
        self.c = Crispy(accept_longform=False)
        self.c.add_variable("name", str)
        self.assertDictEqual(self.c.accepted_keys, {"-n": "name"})
