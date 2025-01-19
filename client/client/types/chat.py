from typing import TypedDict, Literal, Optional
from datetime import datetime

class Message(TypedDict):
    content: str
    role: Literal["user", "assistant"]
    timestamp: str
    status: Literal["sending", "sent", "error"]
    error_message: str