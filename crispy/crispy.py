#
#       Ferit Yiğit BALABAN,    <fybalaban@fybx.dev>
#       crispy                  2023
#
#       crispy.py
from typing import List, Dict, Type

from crispy.missing_value_exception import MissingValueException
from crispy.no_arguments_exception import NoArgumentsException
from crispy.unexpected_argument_exception import UnexpectedArgumentException
from crispy.duplicate_name_exception import DuplicateNameException


class Crispy:
    def __init__(self, accept_shortform=True, accept_longform=True):
        self.accepted_keys: Dict[str, str] = {}
        self.variables: Dict[str, Type[str | bool | int | float]] = {}

        if not (accept_shortform or accept_longform):
            raise ValueError("crispy: At least one form must be accepted!")
        self.accept_shortform = accept_shortform
        self.accept_longform = accept_longform
