# services/api.py
import httpx
from typing import Optional, Dict, Any
from ..types.api import ApiResponse
from ..constants import API_BASE_URL, API_TIMEOUT, RETRY_ATTEMPTS

async def send_message(message: str, retries: int = RETRY_ATTEMPTS) -> ApiResponse:
    """Send a message to the API.
    
    Args:
        message: The message to send
        retries: Number of retry attempts
        
    Returns:
        ApiResponse with success status and data/error
    """
    async with httpx.AsyncClient(timeout=API_TIMEOUT) as client:
        try:
            response = await client.post(
                f"{API_BASE_URL}/chat/message",
                json={"message": message},
            )
            response.raise_for_status()
            return {
                "success": True,
                "data": response.json(),
                "error": None
            }
        except httpx.HTTPError as e:
            if retries > 0:
                return await send_message(message, retries - 1)
            return {
                "success": False,
                "data": None,
                "error": str(e)
            }
        except Exception as e:
            return {
                "success": False,
                "data": None,
                "error": str(e)
            }