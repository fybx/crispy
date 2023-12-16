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


class Test_Try_Parse(TestCase):
    def test_try_parse_case1(self):
        expected = "string"
        actual = Crispy.try_parse("string", str)
        self.assertEqual(expected, actual)

    def test_try_parse_case2(self):
        expected = True
        actual = Crispy.try_parse("true", bool)
        self.assertEqual(expected, actual)

    def test_try_parse_case3(self):
        expected = False
        actual = Crispy.try_parse("false", bool)
        self.assertEqual(expected, actual)

    def test_try_parse_case4(self):
        expected = "false"
        actual = Crispy.try_parse("false", str)
        self.assertEqual(expected, actual)
