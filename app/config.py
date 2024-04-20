import os

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Determine the current running environment
environment = os.getenv("ENVIRONMENT", "dev")