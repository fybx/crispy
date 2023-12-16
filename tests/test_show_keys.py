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


class Test_Show_Keys(TestCase):
    def test_show_keys_case1(self):
        c = Crispy()
        c.add_variable("name", str)
        expected = "-n, --name: name\n"
        actual = c.show_keys()
        self.assertEqual(expected, actual)

    def test_show_keys_case2(self):
        c = Crispy(accept_shortform=False)
        c.add_variable("name", str)
        expected = "--name: name\n"
        actual = c.show_keys()
        self.assertEqual(expected, actual)

    def test_show_keys_case3(self):
        c = Crispy(accept_longform=False)
        c.add_variable("name", str)
        expected = "-n: name\n"
        actual = c.show_keys()
        self.assertEqual(expected, actual)
