from starlette.config import (
    Config,
)  # This class is used to manage configuration settings from environment variables or .env files.

from starlette.datastructures import (
    Secret,
)  # This class is used to handle sensitive data that should not be displayed in logs or error messages.


try:
    config = Config(".env")  # Load environment variables from a .env file
except FileNotFoundError:
    # If the .env file is not found (FileNotFoundError is raised), create a Config instance without a .env file.
    # In this case, the Config instance will only use environment variables.
    config = Config()

# Get the value of the DATABASE_URL environment variable or from the .env file, cast it as a Secret.
# If DATABASE_URL is not found, an error will be raised.
DATABASE_URL = config("DATABASE_URL", cast=Secret)
