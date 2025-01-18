import reflex as rx
from ..components.chat import chat, navbar, agent_modal

@rx.page("/")
def dashboard() -> rx.Component:
    """The main dashboard page."""
    return rx.vstack(
        navbar(),
        chat(),
        agent_modal(),
        height="100vh",
        background_color=rx.color("mauve", 1),
        color=rx.color("mauve", 12),
        spacing="0",
    )