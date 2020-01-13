from .env import (
    AppEnv
)
from .public_env import (
    PublicEnvKeys
)
from logger import (
    logger
)


try:
    DEV = AppEnv["DEV"]
    PROD = AppEnv["PROD"]

    ENV = PublicEnvKeys["ENV"]
    APP_HOST = PublicEnvKeys["APP_HOST"]
    APP_PORT = PublicEnvKeys["APP_PORT"]
except Exception as e:
    logger.error(f"Error initializing enums package: {e}")

    raise
