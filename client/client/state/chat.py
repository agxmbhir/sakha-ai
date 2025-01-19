# state/chat.py
import reflex as rx
from datetime import datetime
from typing import List, Optional
from ..types.chat import Message
from ..constants import DEFAULT_ERROR_MESSAGE, DEFAULT_GREETING

class ChatState(rx.State):
    """State for chat functionality."""
    
    # Chat messages
    messages: List[Message] = []
    
    # Current message being typed
    current_message: str = ""
    
    # Loading state
    is_sending: bool = False
    
    def __init__(self, *args, **kwargs):
        """Initialize the chat state."""
        super().__init__(*args, **kwargs)
        
        # Only initialize messages if they're empty
        if not self.messages:
            self.messages = [
                {
                    "content": DEFAULT_GREETING,
                    "role": "assistant",
                    "timestamp": datetime.now().strftime("%H:%M"),
                    "status": "sent",
                    "error_message": ""
                }
            ]
    
    @rx.var(cache=True)
    def can_send(self) -> bool:
        """Check if a message can be sent."""
        return bool(self.current_message.strip()) and not self.is_sending
    
    def create_message(self, content: str, role: str, status: str = "sent", error_message: str = "") -> Message:
        """Create a new message with current timestamp.
        
        Args:
            content: Message content
            role: Message role ("user" or "assistant")
            status: Message status
            error_message: Optional error message
        """
        return {
            "content": content,
            "role": role,
            "timestamp": datetime.now().strftime("%H:%M"),
            "status": status,
            "error_message": error_message
        }
    
    @rx.event
    async def send_message(self):
        """Send the current message."""
        if not self.can_send:
            return
            
        # Get message content and clear input
        content = self.current_message
        self.current_message = ""
        self.is_sending = True
        
        # Add user message
        self.messages.append(
            self.create_message(content, "user", "sending")
        )
        
        # Simulate API response
        await self.sleep(1)
        
        # Add response
        self.messages.append(
            self.create_message(f"Echo: {content}", "assistant")
        )
        
        self.is_sending = False
    
    @rx.event
    async def clear_chat(self):
        """Clear all messages except the greeting."""
        initial_message = self.create_message(DEFAULT_GREETING, "assistant")
        self.messages = [initial_message]