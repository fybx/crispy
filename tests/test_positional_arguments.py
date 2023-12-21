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


class TestPositionalArguments(TestCase):
    def setUp(self) -> None:
        c = Crispy()
        c.add_positional("name", str, 0)
        c.add_positional("age", int, 1)
        return super().setUp()

    def test_correct_order(self):
        pass
    
    def test_type_mismatch(self):
        pass
    
    def test_with_keys(self):
        pass
    
    def test_with_subcommand(self):
        pass
    
    def test_fail_with_keys_and_subcommand(self):
        pass
    
    def test_pass_with_keys_and_subcommand(self):
        pass