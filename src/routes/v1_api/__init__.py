from sanic import (
    Blueprint
)

from .inventory import (
    inventory_bp
)


__v1_features = Blueprint.group(inventory_bp, url_prefix="/departments")
__v1_api = Blueprint.group(__v1_features, url_prefix="/api")
v1 = Blueprint.group(__v1_api, url_prefix="/v1")
