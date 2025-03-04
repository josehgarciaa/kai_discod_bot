# default_director.py
# -*- coding: utf-8 -*-

"""
Defines a Director class (DefaultDirector) responsible for building a default
Model configuration using the builder methods from the Model class.
"""

from model import Model


class DefaultDirector:
    """
    The Director in the Builder pattern, responsible for providing
    a default (preset) configuration of the Model.
    """

    @staticmethod
    def build_default() -> Model:
        """
        Create and return a default-configured Model instance.

        :return: A fully built Model with default settings.
        """
        return (
            Model()
            # If you have certain "default" overrides, set them here:
            .set_administrator("admin_user")      # example default
            .set_modalities(["text"])             # typical single-modality default
            .set_stream(False)                    # no streaming by default
            .enable_parallel_tool_calls(True)      # allow parallel tool calls
            # Etc. add any fields you want to customize for "default"
            .build()
        )
