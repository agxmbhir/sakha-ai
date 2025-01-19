from typing import TypedDict, Optional

class ApiResponse(TypedDict):
    success: bool
    data: Optional[dict]
    error: Optional[str]
