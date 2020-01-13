from os import (
    environ
)

from enums import (
    DEV, PROD,
    APP_HOST, APP_PORT, ENV
)
from logger import (
    logger
)


class Config:
    """App-wide configurations.
    """

    def __init__(self):
        """
        Args:
            N/A
        """

        try:
            self.host = self.get_env(APP_HOST)
            self.port = self.get_env(APP_PORT)

            env_value = self.get_env(ENV)
            if env_value == PROD:
                self.env = PROD
            elif env_value == DEV:
                self.env = DEV
            else:
                self.env = DEV
                logger.warning(
                    f"Warning in Config.__init__: "
                    f"Unexpected env key ({ENV}), value ({env_value}). "
                    f"Defaulting to {self.env}."
                )

        except Exception as e:
            logger.error(f"Error in Config.__init__: {e}")

            raise

    @staticmethod
    def get_env(key):
        """Get environment variable.

        Args:
            key (str): variable name
        Returns:
            (str): variable value
        """

        try:
            return str(environ[key])
        except Exception as e:
            logger.error(f"Error in Config.get_env: {e}")

            raise
