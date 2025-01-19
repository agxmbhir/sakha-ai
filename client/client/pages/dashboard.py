# pages/dashboard.py
import reflex as rx
from ..components.chat.container import chat_container
from ..styles.colors import colors
from ..state.chat import ChatState
    
def navbar() -> rx.Component:
    """Navigation bar."""
    return rx.hstack(
        rx.heading("Sakha AI Chat", size="6"),
        rx.spacer(),
        rx.button(
            "Clear Chat",
            on_click=lambda: ChatState.clear_chat(),
            variant="outline",
            color=colors["text"]["secondary"],
        ),
        width="100%",
        padding="4",
        border_bottom=f"1px solid {colors['border']}",
        background=colors["background"],
        position="sticky",
        top="0",
        z_index="100",
    )

@rx.page(
    route="/",
    title="Sakha AI - Chat",
    description="Chat with AI assistants",
)
def dashboard() -> rx.Component:
    """Main dashboard page."""
    return rx.vstack(
        navbar(),
        chat_container(),
        min_height="100vh",
        background=colors["surface"],
        spacing="0",
    )