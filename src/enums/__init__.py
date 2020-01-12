from .env import (
    AppEnv
)
from .public_env import (
    PublicEnvKeys
)

DEV = AppEnv["DEV"]
PROD = AppEnv["PROD"]

ENV = PublicEnvKeys["ENV"]
APP_HOST = PublicEnvKeys["APP_HOST"]
APP_PORT = PublicEnvKeys["APP_PORT"]