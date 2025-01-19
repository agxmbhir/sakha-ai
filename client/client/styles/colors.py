import reflex as rx

# Color scheme
colors = {
    "primary": {
        "50": "#f0f9ff",
        "100": "#e0f2fe",
        "200": "#bae6fd",
        "300": "#7dd3fc",
        "400": "#38bdf8",
        "500": "#0ea5e9",
        "600": "#0284c7",
        "700": "#0369a1",
        "800": "#075985",
        "900": "#0c4a6e",
    },
    "background": "#ffffff",
    "surface": "#f8fafc",
    "border": "#e2e8f0",
    "text": {
        "primary": "#1e293b",
        "secondary": "#64748b",
        "accent": "#0ea5e9",
    },
    "success": "#22c55e",
    "error": "#ef4444",
    "warning": "#f59e0b",
}

# Common styles
styles = {
    "chat_container": dict(
        width="100%",
        max_width="4xl",
        height="calc(100vh - 4rem)",
        margin_x="auto",
        padding="4",
        background=colors["surface"],
        border=f"1px solid {colors['border']}",
        border_radius="lg",
    ),
    "message": dict(
        padding="4",
        border_radius="lg",
        max_width="80%",
        box_shadow="sm",
    ),
    "input": dict(
        border=f"1px solid {colors['border']}",
        border_radius="lg",
        padding="3",
        width="100%",
        _focus=dict(
            border_color=colors["primary"]["500"],
            ring="2",
            ring_color=f"{colors['primary']['500']}20",
        ),
    ),
}