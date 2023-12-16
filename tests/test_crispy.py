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


class TestCrispy(TestCase):
    def test_init_accepts_shortform_and_longform(self):
        c = Crispy(accept_shortform=True, accept_longform=True)
        self.assertTrue(c.accept_shortform)
        self.assertTrue(c.accept_longform)

    def test_init_accepts_only_shortform(self):
        c = Crispy(accept_shortform=True, accept_longform=False)
        self.assertTrue(c.accept_shortform)
        self.assertFalse(c.accept_longform)

    def test_init_accepts_only_longform(self):
        c = Crispy(accept_shortform=False, accept_longform=True)
        self.assertFalse(c.accept_shortform)
        self.assertTrue(c.accept_longform)

    def test_init_raises_error_without_acceptance(self):
        with self.assertRaises(ValueError):
            Crispy(accept_shortform=False, accept_longform=False)
