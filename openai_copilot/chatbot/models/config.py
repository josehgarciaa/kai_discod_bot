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
        # Optional (with documented defaults or None)
        self.store: bool = False
        self.reasoning_effort: str = None
        self.metadata: Dict[str, str] = None
        self.frequency_penalty: float = 0.0
        self.logit_bias: Dict[str, float] = None
        self.logprobs: bool = False
        self.top_logprobs: int = None
        self.max_completion_tokens: int = None
        self.n: int = 1
        self.prediction: Dict[str, Any] = None
        self.presence_penalty: float = 0.0
        self.seed: int = None
        self.service_tier: str = "auto"
        self.stop: Union[str, List[str], None] = None
        self.temperature: float = 1.0
        self.top_p: float = 1.0
        self.tool_choice: Union[str, Dict[str, Any]] = "none"

        #output types
        #self.modalities: List[str] = None
        #Output types that you would like the model to generate for this request. Most models are capable of generating text, which is the default:
        #["text"]
        # The gpt-4o-audio-preview model can also be used to generate audio. To request that this model generate both text and audio responses, you can use:
        # ["text", "audio"]
        #self.audio: Dict[str, Any] = None
        #self.response_format: Dict[str, Any] = None
        #self.stream: bool = False
        #self.stream_options: Dict[str, Any] = None
        #self.tools: List[Any] = None
        #self.parallel_tool_calls: bool = True
        #self.user: str = ""
        

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

    def set_presence_penalty(self, penalty: float) -> "ModelConfig":
        """
        Penalize tokens based on whether they appear in the text so far.

        :param penalty: A float between -2.0 and 2.0. Positive values encourage
                        the model to avoid repetition.
        :return: The current ModelConfig instance.
        """
        self.presence_penalty = penalty
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
