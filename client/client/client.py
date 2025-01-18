import reflex as rx
from .pages.dashboard import dashboard
from .state import State

app = rx.App()
app.add_page(dashboard)