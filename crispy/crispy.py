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

    def add_variable(self, name: str, var_type: Type[str | bool | int | float]):
        if name in self.variables:
            raise DuplicateNameException(f"crispy: variable with name '{name}' is present! Choose something else.")
        if self.accept_shortform:
            short_lower = f"-{name[0].lower()}"
            short_upper = f"-{name[0].upper()}"
            if short_lower not in self.accepted_keys:
                self.variables[name] = var_type
                self.accepted_keys[short_lower] = name
            elif short_upper not in self.accepted_keys:
                self.variables[name] = var_type
                self.accepted_keys[short_upper] = name
            else:
                raise ValueError(f"crispy: cannot add variable due to unavailable shortform!'-{short_lower}' "
                                 f"and '-{short_upper}' is reserved for other variables.")
        if self.accept_longform:
            self.variables[name] = var_type
            self.accepted_keys[f"--{name}"] = name
