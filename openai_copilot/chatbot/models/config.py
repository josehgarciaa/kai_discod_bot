from typing import Dict, Any

class ModelConfigBuilder:
    """Builder class to configure and create model instances."""

    def __init__(self) -> None:
        """Initialize default values for model parameters."""
        self.parameters = {}
        self._model_name: str = ""
        self._structured_output: bool = False
        self._temperature: float = 1.0
        self._internet_allowed: bool = False
        self._store_chat: bool = False
        self._reasoning_effort: str = "medium"
        self._metadata: Dict[str, Any] = {}
        self._frequency_penalty: float = 0
        self._logit_bias: Dict = {}
        self._logprobs: bool = False
        self._top_logprobs: int = 0
        self._max_completion_tokens: int = 0
        self._n: int = 1
        self._presence_penalty: float = 0
        self._seed: int = 0
        self._service_tier: str = "auto"
        self._stop: str = ""
        self._stream: bool = False
        self._stream_options: Dict = {}
        self._top_p: float = 1
        self._tools: Any = None
        self._tool_choice: str = ""
        self._parallel_tool_calls: bool = True
        self._user: str = ""

    def build(self):
        return self


    def set_model_name(self, model_name: str) -> "ModelBuilder":
        self._model_name = model_name
        return self

    def enable_structured_output(self, structured: bool) -> "ModelBuilder":
        self._structured_output = structured
        return self

    def set_temperature(self, temp: float) -> "ModelBuilder":
        self._temperature = temp
        return self

    def allow_internet_access(self, allow: bool) -> "ModelBuilder":
        self._internet_allowed = allow
        return self

    def store_chat(self, allow: bool) -> "ModelBuilder":
        self._store_chat = allow
        return self

    def set_reasoning_effort(self, effort: str) -> "ModelBuilder":
        self._reasoning_effort = effort
        return self

    def set_metadata(self, metadata: Dict[str, Any]) -> "ModelBuilder":
        self._metadata = metadata
        return self

    def set_frequency_penalty(self, penalty: float) -> "ModelBuilder":
        self._frequency_penalty = penalty
        return self

    def set_logit_bias(self, bias: Dict) -> "ModelBuilder":
        self._logit_bias = bias
        return self

    def enable_logprobs(self, logprobs: bool) -> "ModelBuilder":
        self._logprobs = logprobs
        return self

    def set_top_logprobs(self, top_logprobs: int) -> "ModelBuilder":
        self._top_logprobs = top_logprobs
        return self

    def set_max_completion_tokens(self, max_tokens: int) -> "ModelBuilder":
        self._max_completion_tokens = max_tokens
        return self

    def set_n(self, n: int) -> "ModelBuilder":
        self._n = n
        return self

    def set_presence_penalty(self, penalty: float) -> "ModelBuilder":
        self._presence_penalty = penalty
        return self

    def set_seed(self, seed: int) -> "ModelBuilder":
        self._seed = seed
        return self

    def set_service_tier(self, tier: str) -> "ModelBuilder":
        self._service_tier = tier
        return self

    def set_stop(self, stop: str) -> "ModelBuilder":
        self._stop = stop
        return self

    def enable_stream(self, stream: bool) -> "ModelBuilder":
        self._stream = stream
        return self

    def set_stream_options(self, options: Dict) -> "ModelBuilder":
        self._stream_options = options
        return self

    def set_top_p(self, top_p: float) -> "ModelBuilder":
        self._top_p = top_p
        return self

    def set_tools(self, tools: Any) -> "ModelBuilder":
        self._tools = tools
        return self

    def set_tool_choice(self, tool_choice: str) -> "ModelBuilder":
        self._tool_choice = tool_choice
        return self

    def enable_parallel_tool_calls(self, enable: bool) -> "ModelBuilder":
        self._parallel_tool_calls = enable
        return self

    def set_user(self, user: str) -> "ModelBuilder":
        self._user = user
        return self

    def build(self) -> "ModelBuilder":
        return self

    def get_parameters(self) -> Dict[str, Any]:
        """Return a dictionary of all set parameters."""
        return {
            "model_name": self._model_name,
            "structured": self._structured_output,
            "temperature": self._temperature,
            "internet_allowed": self._internet_allowed,
            "store_chat": self._store_chat,
            "reasoning_effort": self._reasoning_effort,
            "metadata": self._metadata,
            "frequency_penalty": self._frequency_penalty,
            "logit_bias": self._logit_bias,
            "logprobs": self._logprobs,
            "top_logprobs": self._top_logprobs,
            "max_completion_tokens": self._max_completion_tokens,
            "n": self._n,
            "presence_penalty": self._presence_penalty,
            "seed": self._seed,
            "service_tier": self._service_tier,
            "stop": self._stop,
            "stream": self._stream,
            "stream_options": self._stream_options,
            "top_p": self._top_p,
            "tools": self._tools,
            "tool_choice": self._tool_choice,
            "parallel_tool_calls": self._parallel_tool_calls,
            "user": self._user,
        }

