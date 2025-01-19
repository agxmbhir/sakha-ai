import reflex as rx
from datetime import datetime
from ...types.chat import Message
from ...styles.colors import colors, styles

from .input import chat_input
from .message import message_bubble
def chat_container() -> rx.Component:
    """Main chat container."""
    from ...state.chat import ChatState
    
    return rx.vstack(
        # Messages area
        rx.box(
            rx.vstack(
                rx.foreach(
                    ChatState.messages,
                    message_bubble,
                ),
                spacing="4",
                align_items="stretch",
            ),
            flex="1",
            overflow_y="auto",
            padding="4",
        ),
        
        # Input area
        chat_input(),
        
        **styles["chat_container"],
    )