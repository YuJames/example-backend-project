from enum import (
    Enum
)

from .base import (
    EnumBase
)


class AppEnv(Enum, metaclass=EnumBase):
    """Describes the application environment.
    """

    PROD = "production"
    DEV = "development"
