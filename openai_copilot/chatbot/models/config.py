from typing import Any, Dict, List, Optional, Union

class ModelConfig:
    """
    A builder-style class for configuring model parameters.
    Each setter returns self, allowing fluent (chained) calls.
    """

    def __init__(self):
        # Required
        self.messages: List[Any] = []
        self.model: str = ""

        # Optional
        self.store: Optional[bool] = False
        self.reasoning_effort: Optional[str] = "medium"   # e.g. "low", "medium", "high"
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

    # Fluent setters
    def set_messages(self, messages: List[Any]) -> "ModelConfig":
        self.messages = messages
        return self

    def set_model(self, model: str) -> "ModelConfig":
        self.model = model
        return self

    def set_store(self, store: bool) -> "ModelConfig":
        self.store = store
        return self

    def set_reasoning_effort(self, effort: str) -> "ModelConfig":
        self.reasoning_effort = effort
        return self

    def set_metadata(self, metadata: Dict[str, str]) -> "ModelConfig":
        self.metadata = metadata
        return self

    def set_frequency_penalty(self, penalty: float) -> "ModelConfig":
        self.frequency_penalty = penalty
        return self

    def set_logit_bias(self, bias: Dict[str, float]) -> "ModelConfig":
        self.logit_bias = bias
        return self

    def set_logprobs(self, log_probs: bool) -> "ModelConfig":
        self.logprobs = log_probs
        return self

    def set_top_logprobs(self, top_logprobs: int) -> "ModelConfig":
        self.top_logprobs = top_logprobs
        return self

    def set_max_completion_tokens(self, max_tokens: int) -> "ModelConfig":
        self.max_completion_tokens = max_tokens
        return self

    def set_n(self, n: int) -> "ModelConfig":
        self.n = n
        return self

    def set_modalities(self, modalities: List[str]) -> "ModelConfig":
        self.modalities = modalities
        return self

    def set_prediction(self, prediction: Dict[str, Any]) -> "ModelConfig":
        self.prediction = prediction
        return self

    def set_audio(self, audio: Dict[str, Any]) -> "ModelConfig":
        self.audio = audio
        return self

    def set_presence_penalty(self, penalty: float) -> "ModelConfig":
        self.presence_penalty = penalty
        return self

    def set_response_format(self, fmt: Dict[str, Any]) -> "ModelConfig":
        self.response_format = fmt
        return self

    def set_seed(self, seed: int) -> "ModelConfig":
        self.seed = seed
        return self

    def set_service_tier(self, tier: str) -> "ModelConfig":
        self.service_tier = tier
        return self

    def set_stop(self, stop: Union[str, List[str]]) -> "ModelConfig":
        self.stop = stop
        return self

    def set_stream(self, stream: bool) -> "ModelConfig":
        self.stream = stream
        return self

    def set_stream_options(self, options: Dict[str, Any]) -> "ModelConfig":
        self.stream_options = options
        return self

    def set_temperature(self, temperature: float) -> "ModelConfig":
        self.temperature = temperature
        return self

    def set_top_p(self, top_p: float) -> "ModelConfig":
        self.top_p = top_p
        return self

    def set_tools(self, tools: List[Any]) -> "ModelConfig":
        self.tools = tools
        return self

    def set_tool_choice(self, choice: Union[str, Dict[str, Any]]) -> "ModelConfig":
        self.tool_choice = choice
        return self

    def enable_parallel_tool_calls(self, enable: bool) -> "ModelConfig":
        self.parallel_tool_calls = enable
        return self

    def set_user(self, user: str) -> "ModelConfig":
        self.user = user
        return self

    # Deprecated
    def set_function_call(self, fn_call: Any) -> "ModelConfig":
        self.function_call = fn_call
        return self

    def set_functions(self, functions: Any) -> "ModelConfig":
        self.functions = functions
        return self

    def build(self) -> "ModelConfig":
        """
        If you need a final validation or transformation step,
        do it here. Then return self (or a new immutable object).
        """
        # Example of final checks (optional):
        if self.n < 1:
            raise ValueError("`n` must be >= 1")

        return self

    def __repr__(self) -> str:
        return (f"<ModelConfig model={self.model}, temperature={self.temperature}, "
                f"messages={len(self.messages)} messages, ...>")
