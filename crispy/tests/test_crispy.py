#
#       Ferit Yiğit BALABAN,    <fybalaban@fybx.dev>
#       crispy                  2023
#
#       test_crispy.py
from unittest import TestCase
from crispy.crispy import Crispy


class TestCrispy(TestCase):
    def test_init_accepts_shortform_and_longform(self):
        c = Crispy(accept_shortform=True, accept_longform=True)
        self.assertTrue(c.accept_shortform)
        self.assertTrue(c.accept_longform)
