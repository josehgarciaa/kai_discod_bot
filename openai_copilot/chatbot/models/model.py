# model.py
# -*- coding: utf-8 -*-

"""
Defines a builder-style Model class, allowing for fluent (chained) configuration
of various parameters such as administrator, modalities, audio settings, and more.
"""

from typing import Any, Dict, List, Optional


class Model:
    """
    A builder-style class for configuring model parameters such as output types,
    streaming options, and more. Each setter returns the current instance to
    support chained method calls.
    """

    def __init__(self) -> None:
        """
        Initialize default values for all configurable fields. These defaults
        can be overridden by calling the provided setter methods.
        """
        self.developer: str = "You are a useful assistant"
        self.type: str = "gpt-4o-mini"
        self.modalities: Optional[List[str]] = ["text"]
        self.audio: Optional[Dict[str, Any]] = None
        self.response_format: Optional[Dict[str, Any]] = None
        self.stream: bool = False
        self.stream_options: Optional[Dict[str, Any]] = None
        self.tools: Optional[List[Any]] = None
        self.parallel_tool_calls: bool = True
        self.user: str = ""

    def set_administrator(self, administrator: str) -> "Model":
        """
        Set the administrator identifier for this model configuration.

        :param administrator: The admin or owner responsible for this model.
        :return: The current Model instance (for fluent chaining).
        """
        self.administrator = administrator
        return self

    def set_model_type(self, administrator: str) -> "Model":
        """
        Set the administrator identifier for this model configuration.

        :param administrator: The admin or owner responsible for this model.
        :return: The current Model instance (for fluent chaining).
        """
        self.administrator = administrator
        return self


    def set_modalities(self, modalities: List[str]) -> "Model":
        """
        Specify one or more output modalities the model should generate.
        Typical values could be ["text"] or ["text", "audio"].

        :param modalities: A list of desired output modalities.
        :return: The current Model instance (for fluent chaining).
        """
        self.modalities = modalities
        return self

    def set_audio(self, audio: Dict[str, Any]) -> "Model":
        """
        Provide configuration for audio output parameters.

        :param audio: A dictionary with audio-related configuration, 
                      e.g. codec or audio format settings.
        :return: The current Model instance (for fluent chaining).
        """
        self.audio = audio
        return self

    def set_response_format(self, response_format: Dict[str, Any]) -> "Model":
        """
        Specify the desired output format (e.g., JSON schema).

        :param response_format: A dictionary defining the output format.
        :return: The current Model instance (for fluent chaining).
        """
        self.response_format = response_format
        return self

    def set_stream(self, stream: bool) -> "Model":
        """
        Toggle streaming mode for partial token outputs in real time.

        :param stream: True to enable streaming, False otherwise.
        :return: The current Model instance (for fluent chaining).
        """
        self.stream = stream
        return self

    def set_stream_options(self, stream_options: Dict[str, Any]) -> "Model":
        """
        Configure additional streaming options.

        :param stream_options: A dictionary with stream-related parameters.
        :return: The current Model instance (for fluent chaining).
        """
        self.stream_options = stream_options
        return self

    def set_tools(self, tools: List[Any]) -> "Model":
        """
        Provide a list of tools (functions) the model may call.

        :param tools: A list of tool definitions (up to 128).
        :return: The current Model instance (for fluent chaining).
        """
        self.tools = tools
        return self

    def enable_parallel_tool_calls(self, enable: bool) -> "Model":
        """
        Allow or disallow parallel calls to multiple tools.

        :param enable: True to enable parallel tool calls, False to disable.
        :return: The current Model instance (for fluent chaining).
        """
        self.parallel_tool_calls = enable
        return self

    def set_user(self, user: str) -> "Model":
        """
        Assign a unique user identifier. Useful for tracking or analytics.

        :param user: A string identifying the end-user.
        :return: The current Model instance (for fluent chaining).
        """
        self.user = user
        return self

    def build(self) -> "Model":
        """
        Finalize and return the fully configured Model object. Implement
        any validation or post-processing here if needed.

        :return: The current Model instance (for fluent chaining).
        """
        # Example validation (optional):
        # if self.stream and not self.stream_options:
        #     raise ValueError("Stream options must be set if streaming is enabled.")
        return self

    def __repr__(self) -> str:
        """
        Provide a concise string representation of the model configuration.
        """
        return (
            f"<Model administrator={self.administrator}, "
            f"modalities={self.modalities}, stream={self.stream}, ...>"
        )
