# components/chat.py
import reflex as rx
from ..state import State, QA

def message(qa: QA) -> rx.Component:
    """A single question/answer message.

    Args:
        qa: The question/answer pair.

    Returns:
        A component displaying the question/answer pair.
    """
    return rx.box(
        rx.box(
            rx.markdown(
                qa.question,
                background_color=rx.color("mauve", 4),
                color=rx.color("mauve", 12),
                display="inline-block",
                padding="1em",
                border_radius="8px",
                max_width="30em"
            ),
            text_align="right",
            margin_top="1em",
        ),
        rx.box(
            rx.markdown(
                qa.answer,
                background_color=rx.color("accent", 4),
                color=rx.color("accent", 12),
                display="inline-block",
                padding="1em",
                border_radius="8px",
                max_width="30em"
            ),
            text_align="left",
            padding_top="1em",
        ),
        width="100%",
    )

def chat() -> rx.Component:
    """The main chat interface."""
    return rx.vstack(
        rx.box(
            rx.foreach(
                State.agents[State.current_agent],
                message
            ),
            width="100%",
            height="600px",
            overflow_y="auto",
            padding="4px",
        ),
        rx.form(
            rx.hstack(
                rx.input(
                    placeholder="Type your message...",
                    id="question",
                    width="100%",
                ),
                rx.button(
                    rx.cond(
                        State.processing,
                        rx.spinner(),
                        rx.text("Send")
                    ),
                    type_="submit",
                ),
            ),
            on_submit=State.process_question,
            width="100%",
        ),
        width="100%",
        height="100%",
        padding="4em",
        spacing="4",
    )

def navbar() -> rx.Component:
    """The top navigation bar."""
    return rx.hstack(
        rx.hstack(
            rx.heading("Sakha AI", size="3"),
            rx.select(
                State.agent_list,
                value=State.current_agent,
                on_change=State.set_agent,
                width="200px",
            ),
        ),
        rx.hstack(
            rx.button(
                "New Agent",
                on_click=State.toggle_modal
            ),
            rx.button(
                "Delete Agent",
                on_click=State.delete_agent,
                color_scheme="red",
            ) ,
        ),
        justify_content="space-between",
        width="100%",
        padding="1em",
        border_bottom="1px solid",
        border_color=rx.color("mauve", 3),
    )

def agent_modal() -> rx.Component:
    """Modal for creating a new agent."""
    return rx.dialog.root(
        rx.dialog.content(
            rx.vstack(
                rx.heading("Create New Agent", size="4"),
                rx.input(
                    placeholder="Agent Name",
                    on_change=State.set_new_agent_name,
                    value=State.new_agent_name,
                ),
                rx.hstack(
                    rx.dialog.close(
                        rx.button("Cancel")
                    ),
                    rx.button(
                        "Create",
                        on_click=State.create_agent,
                    ),
                ),
                padding="4",
                spacing="4",
            ),
        ),
        open=State.modal_open,
    )