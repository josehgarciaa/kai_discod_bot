# my_model_config.py
# -*- coding: utf-8 -*-

"""
This module defines a builder-style class for configuring chat completion
parameters. The class provides fluent setter methods, each returning self,
making it simple to chain multiple configurations in one statement.

PEP 8 compliance note:
- Line length is kept at or below 79 characters (per PEP 8 recommendations).
- Docstrings include brief descriptions of each method, referencing the
  relevant API parameters as described in the specification.
"""

from typing import Any, Dict, List, Optional, Union


class ModelConfig:
    """
    A builder-style class for configuring chat completion parameters.

    Each setter returns the current instance (self) to allow method chaining.
    The final configuration can be used directly or validated further if needed.
    """

    def __init__(self) -> None:
        """
        Initializes default values for all parameters. These defaults reflect
        either the documented API defaults or typical starting points.
        """
        # Required
        self.messages: List[Any] = []
        self.model: str = ""

        # Optional (with documented defaults or None)
        self.store: Optional[bool] = False
        self.reasoning_effort: Optional[str] = "medium"
        self.metadata: Dict[str, str] = {}
        self.frequency_penalty: float = 0.0
        self.logit_bias: Dict[str, float] = {}
        self.logprobs: Optional[bool] = False
        self.top_logprobs: Optional[int] = None
        self.max_completion_tokens: Optional[int] = None
        self.n: int = 1
        self.modalities: Optional[List[str]] = None
        self.prediction: Optional[Dict[str, Any]] = None
        self.audio: Optional[Dict[str, Any]] = None
        self.presence_penalty: float = 0.0
        self.response_format: Optional[Dict[str, Any]] = None
        self.seed: Optional[int] = None
        self.service_tier: Optional[str] = "auto"
        self.stop: Union[str, List[str], None] = None
        self.stream: Optional[bool] = False
        self.stream_options: Optional[Dict[str, Any]] = None
        self.temperature: float = 1.0
        self.top_p: float = 1.0
        self.tools: Optional[List[Any]] = None
        self.tool_choice: Union[str, Dict[str, Any]] = "none"
        self.parallel_tool_calls: bool = True
        self.user: str = ""

        # Deprecated
        self.function_call: Any = None
        self.functions: Any = None

    def set_messages(self, messages: List[Any]) -> "ModelConfig":
        """
        Set the conversation messages for the model.

        :param messages: A list of messages (array) representing the
                         conversation so far. Can include text, images, or audio
                         elements depending on the model's capabilities.
        :return: The current ModelConfig instance.
        """
        self.messages = messages
        return self

    def set_model(self, model: str) -> "ModelConfig":
        """
        Set the model ID to use.

        :param model: Required. The model identifier (e.g., "gpt-4").
        :return: The current ModelConfig instance.
        """
        self.model = model
        return self

    def set_store(self, store: bool) -> "ModelConfig":
        """
        Specify whether to store the output for use in model distillation.

        :param store: Optional (defaults to False).
        :return: The current ModelConfig instance.
        """
        self.store = store
        return self

    def set_reasoning_effort(self, effort: str) -> "ModelConfig":
        """
        Constrain the reasoning effort for compatible models.

        :param effort: Optional (defaults to "medium"). Valid values are
                       "low", "medium", or "high" for o1/o3-mini models only.
        :return: The current ModelConfig instance.
        """
        self.reasoning_effort = effort
        return self

    def set_metadata(self, metadata: Dict[str, str]) -> "ModelConfig":
        """
        Attach additional metadata as key-value pairs.

        :param metadata: A dictionary with up to 16 key-value pairs,
                         keys up to 64 chars, values up to 512 chars.
        :return: The current ModelConfig instance.
        """
        self.metadata = metadata
        return self

    def set_frequency_penalty(self, penalty: float) -> "ModelConfig":
        """
        Adjust repetition penalty based on token frequency.

        :param penalty: A float between -2.0 and 2.0. Positive values penalize
                        repeating tokens, reducing verbatim repetition.
        :return: The current ModelConfig instance.
        """
        self.frequency_penalty = penalty
        return self

    def set_logit_bias(self, bias: Dict[str, float]) -> "ModelConfig":
        """
        Modify the likelihood of specified tokens appearing.

        :param bias: A dictionary mapping token IDs to bias values
                     (-100 to 100). Large positive/negative values can ban
                     or force tokens.
        :return: The current ModelConfig instance.
        """
        self.logit_bias = bias
        return self

    def set_logprobs(self, log_probs: bool) -> "ModelConfig":
        """
        Specify whether to return log probabilities of output tokens.

        :param log_probs: Optional (defaults to False). If True, each output
                          token's log probability will be included.
        :return: The current ModelConfig instance.
        """
        self.logprobs = log_probs
        return self

    def set_top_logprobs(self, top_logprobs: int) -> "ModelConfig":
        """
        Specify how many top tokens to return in log probabilities.

        :param top_logprobs: Integer (0 to 20). Must have logprobs=True
                             for this to take effect.
        :return: The current ModelConfig instance.
        """
        self.top_logprobs = top_logprobs
        return self

    def set_max_completion_tokens(self, max_tokens: int) -> "ModelConfig":
        """
        Set the maximum number of tokens to generate.

        :param max_tokens: Upper bound on tokens for both visible output and
                           internal reasoning. This is preferred over
                           the deprecated max_tokens parameter.
        :return: The current ModelConfig instance.
        """
        self.max_completion_tokens = max_tokens
        return self

    def set_n(self, n: int) -> "ModelConfig":
        """
        Set how many chat completion choices to generate.

        :param n: Defaults to 1. Increasing this will generate multiple
                  responses but will cost more tokens.
        :return: The current ModelConfig instance.
        """
        self.n = n
        return self

    def set_modalities(self, modalities: List[str]) -> "ModelConfig":
        """
        Specify which output types the model should generate.

        :param modalities: E.g., ["text"] or ["text", "audio"] if using
                           an audio-capable model.
        :return: The current ModelConfig instance.
        """
        self.modalities = modalities
        return self

    def set_prediction(self, prediction: Dict[str, Any]) -> "ModelConfig":
        """
        Provide configuration for a Predicted Output.

        :param prediction: Enhances response times if large parts of
                           the model response are pre-known.
        :return: The current ModelConfig instance.
        """
        self.prediction = prediction
        return self

    def set_audio(self, audio: Dict[str, Any]) -> "ModelConfig":
        """
        Configure audio output parameters.

        :param audio: Required if audio output is requested with
                      modalities=["audio"].
        :return: The current ModelConfig instance.
        """
        self.audio = audio
        return self

    def set_presence_penalty(self, penalty: float) -> "ModelConfig":
        """
        Penalize tokens based on whether they appear in the text so far.

        :param penalty: A float between -2.0 and 2.0. Positive values encourage
                        the model to avoid repetition.
        :return: The current ModelConfig instance.
        """
        self.presence_penalty = penalty
        return self

    def set_response_format(self, fmt: Dict[str, Any]) -> "ModelConfig":
        """
        Specify the format for the model's output.

        :param fmt: An object describing the output format, such as
                    {"type": "json_schema", "json_schema": {...}} or
                    {"type": "json_object"} for JSON-mode responses.
        :return: The current ModelConfig instance.
        """
        self.response_format = fmt
        return self

    def set_seed(self, seed: int) -> "ModelConfig":
        """
        Set a seed for best-effort deterministic sampling.

        :param seed: An integer seed. Repeated requests with identical
                     parameters and seed may produce the same output.
        :return: The current ModelConfig instance.
        """
        self.seed = seed
        return self

    def set_service_tier(self, tier: str) -> "ModelConfig":
        """
        Specify the service tier for processing the request.

        :param tier: Defaults to "auto". If set to "auto" and the project
                     is scale-tier enabled, scale-tier credits are used.
        :return: The current ModelConfig instance.
        """
        self.service_tier = tier
        return self

    def set_stop(self, stop: Union[str, List[str]]) -> "ModelConfig":
        """
        Define one or more sequences that will stop token generation.

        :param stop: A string or a list of up to 4 strings to halt generation.
        :return: The current ModelConfig instance.
        """
        self.stop = stop
        return self

    def set_stream(self, stream: bool) -> "ModelConfig":
        """
        Toggle streaming mode for partial token outputs.

        :param stream: Defaults to False. If True, tokens are returned
                       as data-only server-sent events until done.
        :return: The current ModelConfig instance.
        """
        self.stream = stream
        return self

    def set_stream_options(self, options: Dict[str, Any]) -> "ModelConfig":
        """
        Specify additional streaming response options.

        :param options: Only relevant if stream=True.
        :return: The current ModelConfig instance.
        """
        self.stream_options = options
        return self

    def set_temperature(self, temperature: float) -> "ModelConfig":
        """
        Control randomness in sampling between 0 and 2.

        :param temperature: Defaults to 1.0. Higher values increase
                            randomness, lower values make output more
                            deterministic.
        :return: The current ModelConfig instance.
        """
        self.temperature = temperature
        return self

    def set_top_p(self, top_p: float) -> "ModelConfig":
        """
        Use nucleus sampling, considering tokens up to top_p probability.

        :param top_p: Defaults to 1.0. If 0.1, only the tokens comprising
                      the top 10% probability mass are considered.
        :return: The current ModelConfig instance.
        """
        self.top_p = top_p
        return self

    def set_tools(self, tools: List[Any]) -> "ModelConfig":
        """
        Supply a list of tools (functions) the model may call.

        :param tools: A list of up to 128 functions. The model can generate
                      JSON inputs for these functions if tool_choice allows it.
        :return: The current ModelConfig instance.
        """
        self.tools = tools
        return self

    def set_tool_choice(
        self, choice: Union[str, Dict[str, Any]]
    ) -> "ModelConfig":
        """
        Control if and how the model calls tools.

        :param choice: "none", "auto", "required", or a dict specifying
                       a specific tool. Defaults to "none" if no tools are set.
        :return: The current ModelConfig instance.
        """
        self.tool_choice = choice
        return self

    def enable_parallel_tool_calls(self, enable: bool) -> "ModelConfig":
        """
        Enable or disable parallel tool calls.

        :param enable: Defaults to True. If True, the model may call
                       multiple tools in parallel.
        :return: The current ModelConfig instance.
        """
        self.parallel_tool_calls = enable
        return self

    def set_user(self, user: str) -> "ModelConfig":
        """
        Attach a unique user identifier for analytics or abuse detection.

        :param user: A string identifying the end user. Helps monitor
                     usage patterns.
        :return: The current ModelConfig instance.
        """
        self.user = user
        return self

    def set_function_call(self, fn_call: Any) -> "ModelConfig":
        """
        Deprecated in favor of tool_choice. Controls which function is called.

        :param fn_call: Allows specifying none, auto, or a particular function.
        :return: The current ModelConfig instance.
        """
        self.function_call = fn_call
        return self

    def set_functions(self, functions: Any) -> "ModelConfig":
        """
        Deprecated in favor of tools. A list of functions the model may call.

        :param functions: Similar to tools, but older usage.
        :return: The current ModelConfig instance.
        """
        self.functions = functions
        return self

    def build(self) -> "ModelConfig":
        """
        Optionally finalize this configuration.

        Perform validations or transformations if necessary, then
        return the fully configured instance.

        :return: The current ModelConfig instance (fully configured).
        """
        # Example validation check:
        if self.n < 1:
            raise ValueError("Parameter 'n' must be >= 1.")
        return self

    def __repr__(self) -> str:
        """
        Return a concise string representation of the configuration.
        """
        return (
            f"<ModelConfig model={self.model}, temperature={self.temperature}, "
            f"messages={len(self.messages)} messages, ...>"
        )
