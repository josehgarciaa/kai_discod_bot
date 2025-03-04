# director.py
# -*- coding: utf-8 -*-

"""
This module defines a Director class for constructing preset ModelConfig
instances. The Director orchestrates the configuration steps needed for
standard or specialized configurations.
"""

from typing import Any
from models import Config

class ConfigDirector:
    """
    The Director in the Builder pattern. Responsible for creating
    preset configurations for Config.
    """

    @staticmethod
    def Default() -> Config:
        """
        Build and return a ModelConfig instance with default values.

        :return: A ModelConfig instance using its own defaults.
        """
        # If you want to override any defaults, chain the setter methods here.
        # For now, this simply returns a freshly built config as-is.
        return Config().build()
