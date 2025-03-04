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


    @staticmethod
    def python_programmer() -> Model:
        """
        Create and return a default-configured Model instance.

        :return: A fully built Model with default settings.
        """
        return (
            Model()
            .set_model_type("gpt-4o")
            .set_developer_instruction("You are a python programming expert that is overviewing the software of the user. You should use a direct language with short ammount of words and provide the information about lack of consistency, lack of documentation, problems with PEP compliance and check for common pitfall ocurring when programming with python. readibily and maintanibily should be priorities")
            .build()
        )
