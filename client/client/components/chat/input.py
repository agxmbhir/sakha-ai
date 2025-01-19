import reflex as rx
from datetime import datetime
from ...types.chat import Message
from ...styles.colors import colors, styles

def chat_input() -> rx.Component:
    """Chat input component."""
    from ...state.chat import ChatState
    
    return rx.form(
        rx.hstack(
            rx.input(
                placeholder="Type a message...",
                value=ChatState.current_message,
                on_change=ChatState.set_current_message,
                **styles["input"],
            ),
            rx.button(
                rx.cond(
                    ChatState.is_sending,
                    rx.spinner(),
                    rx.text("Send"),
                ),
                type_="submit",
                color=colors["text"]["primary"],
                background=colors["primary"]["500"],
                _hover={"background": colors["primary"]["600"]},
                disabled=~ChatState.can_send,
            ),
            width="100%",
            padding="4",
        ),
        on_submit=ChatState.send_message,
    )
