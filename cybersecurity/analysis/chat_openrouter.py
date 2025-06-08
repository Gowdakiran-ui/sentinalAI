# chat_openrouter.py
import os
from langchain_openai import ChatOpenAI
from pydantic import Field, SecretStr
from langchain_core.utils.utils import secret_from_env

class ChatOpenRouter(ChatOpenAI):
    openai_api_key: SecretStr = Field(
        alias="api_key",
        default_factory=secret_from_env("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")
    )
    base_url: str = "https://openrouter.ai/api/v1"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
