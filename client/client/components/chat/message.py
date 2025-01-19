# components/chat/message.py
import reflex as rx
from typing import Dict
from ...types.chat import Message
from ...styles.colors import colors, styles

def message_bubble(message: Message) -> rx.Component:
    """Individual message bubble."""
    return rx.box(
        rx.vstack(
            # Message content
            rx.text(
                message["content"],
                color=colors["text"]["primary"]
            ),
            
            # Error message if status is error
            rx.cond(
                message["status"] == "error",
                rx.text(
                    rx.cond(
                        message["error_message"] != "",  # Check if error message exists
                        message["error_message"],  # Show error message if it exists
                        "Error sending message"  # Default error message
                    ),
                    color=colors["error"],
                    font_size="sm",
                ),
            ),
            
            # Timestamp
            rx.text(
                message["timestamp"],
                color=colors["text"]["secondary"],
                font_size="xs",
                align_self="flex-end",
            ),
            align_items="flex-start",
            spacing="1",
        ),
        background=rx.cond(
            message["role"] == "user",
            colors["primary"]["100"],
            colors["background"]
        ),
        margin_left=rx.cond(
            message["role"] == "user",
            "auto",
            "0"
        ),
        margin_right=rx.cond(
            message["role"] == "user",
            "0",
            "auto"
        ),
        border=f"1px solid {colors['border']}",
        **styles["message"],
    )