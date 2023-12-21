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

class TestDeduceType(TestCase):
    def setUp(self) -> None:
        self.c = Crispy()
        return super().setUp()
    
    def test_deduce_type_returns_bool_for_true(self):
        result = self.c.deduce_type("true")
        self.assertEqual(result, bool)

    def test_deduce_type_returns_bool_for_false(self):
        result = self.c.deduce_type("false")
        self.assertEqual(result, bool)

    def test_deduce_type_returns_int_for_integer(self):
        result = self.c.deduce_type("123")
        self.assertEqual(result, int)

    def test_deduce_type_returns_float_for_float(self):
        result = self.c.deduce_type("3.14")
        self.assertEqual(result, float)

    def test_deduce_type_returns_str_for_other_values(self):
        result = self.c.deduce_type("hello")
        self.assertEqual(result, str)
