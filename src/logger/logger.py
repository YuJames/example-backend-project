from datetime import (
    datetime
)
from logging import (
    basicConfig,
    getLogger,
    INFO
)

logger = getLogger()
_file_name = datetime.now().strftime("log_%Y_%m_%d")
basicConfig(
    filename="./logs/" + _file_name,
    format="%(asctime)s %(levelname)s %(message)s",
    filemode="a"
)
logger.setLevel(INFO)
