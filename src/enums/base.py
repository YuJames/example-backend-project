from enum import (
    EnumMeta
)

from logger import (
    logger
)


class EnumBase(EnumMeta):
    """Base class for all enums, to enable improved access to enum values.
    """

    def __getitem__(self, name):
        try:
            return super().__getitem__(name.upper()).value
        except Exception as e:
            logger.debug(f"Exception in EnumBase.__getitem__: {e}")
