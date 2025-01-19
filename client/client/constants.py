from typing import Final

# API Configuration
API_BASE_URL: Final = "https://api.sakhaai.com/v1"
API_TIMEOUT: Final = 10  # seconds

# UI Constants
MAX_MESSAGES_DISPLAYED: Final = 50
MESSAGE_PAGE_SIZE: Final = 20

# Chat Configuration
TYPING_INDICATOR_DELAY: Final = 1.0
RETRY_ATTEMPTS: Final = 3

# Default Messages
DEFAULT_ERROR_MESSAGE: Final = "Something went wrong. Please try again."
DEFAULT_GREETING: Final = "Hi! I'm your AI assistant. How can I help you today?"