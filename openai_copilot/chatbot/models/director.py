# default_director.py
# -*- coding: utf-8 -*-

"""
Defines a Director class (DefaultDirector) responsible for building a default
Model configuration using the builder methods from the Model class.
"""

from models import Model


class Director:
    """
    The Director in the Builder pattern, responsible for providing
    a default (preset) configuration of the Model.
    """

    @staticmethod
    def default_model() -> Model:
        """
        Create and return a default-configured Model instance.

        :return: A fully built Model with default settings.
        """
        return (
            Model().build()
        )
