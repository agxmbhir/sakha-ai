# state.py
import reflex as rx
from typing import List, Dict
import os

class QA(rx.Base):
    """A question and answer pair."""
    question: str
    answer: str

DEFAULT_AGENTS = {
    "Customer Service": [],
    "Sales Agent": [],
    "Technical Support": []
}

class State(rx.State):
    """The main dashboard state."""
    
    # A dict from the agent name to the list of questions and answers
    agents: Dict[str, List[QA]] = DEFAULT_AGENTS

    # The current selected agent
    current_agent: str = "Customer Service"

    # The current question
    question: str = ""

    # Whether we are processing the question
    processing: bool = False

    # For modal/new agent
    new_agent_name: str = ""
    modal_open: bool = False
    
    @rx.event
    def toggle_modal(self):
        """Toggle the modal open/closed."""
        self.modal_open = not self.modal_open

    def create_agent(self):
        """Create a new agent."""
        if not self.new_agent_name.strip():
            return
        self.current_agent = self.new_agent_name
        self.agents[self.new_agent_name] = []
        self.modal_open = False
        self.new_agent_name = ""

    def delete_agent(self):
        """Delete the current agent."""
        if self.current_agent in DEFAULT_AGENTS:
            return  # Don't delete default agents
        del self.agents[self.current_agent]
        self.current_agent = list(self.agents.keys())[0]

    def set_agent(self, agent_name: str):
        """Set the current agent.

        Args:
            agent_name: The name of the agent.
        """
        self.current_agent = agent_name

    @rx.var
    def agent_list(self) -> List[str]:
        """Get the list of agent names.

        Returns:
            The list of agent names.
        """
        return list(self.agents.keys())

    async def process_question(self, form_data: Dict[str, str]):
        """Process a question from the user.

        Args:
            form_data: A dict with the current question.
        """
        # Get the question from the form
        question = form_data.get("question", "")
        if not question.strip():
            return

        # Create a new QA pair
        qa = QA(question=question, answer="")
        self.agents[self.current_agent].append(qa)

        # Start processing
        self.processing = True
        yield

        # Simulate agent response (replace with actual agent logic)
        await self.sleep(1)
        self.agents[self.current_agent][-1].answer = f"Response from {self.current_agent}: {question}"
        
        # Done processing
        self.processing = False