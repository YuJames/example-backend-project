from enum import (
    Enum
)

from .base import (
    EnumBase
)


class PublicEnvKeys(Enum, metaclass=EnumBase):
    """Describes the application's public environment keys.
    """

    BUILD = "BUILD_NUMBER"
    ENV = "ENVIRONMENT"
    APP_HOST = "APP_HOST"
    APP_PORT = "APP_PORT"
