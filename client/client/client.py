import reflex as rx
from .pages.dashboard import dashboard
from .state.chat import ChatState

app = rx.App()
app.add_page(dashboard)