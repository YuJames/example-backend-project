from json import (
    loads
)

from sanic import (
    response
)
from sanic.blueprints import (
    Blueprint
)


# api routes
inventory_bp = Blueprint("inventory_bp", url_prefix="/kitchen")

next_unique_id = 1
inventory = {}

"""Expecting HTTP body.

{
    group: [],      # optional; rep code (e.g. client_A, e.g. client_B)
    user: [],       # optional; username of alert creator (e.g. employee@client.com)
    role: [],       # optional; user role (e.g. admin, regular)
    type: []        # optional; alert type (e.g. usage, weather)
}
"""


@inventory_bp.route("/inventory", methods=["GET"])
async def get_inventory_all(request):
    """Get the inventory of all items.
    """

    try:
        return response.json(
            inventory
        )
    except Exception as e:
        return response.json(
            {"error": str(e)},
            status=500
        )


@inventory_bp.route("/inventory/<item>", methods=["GET"])
async def get_inventory(request, item):
    """Get the inventory of a specific item.
    """

    try:
        if item in inventory.keys():
            return response.json(
                {item: inventory[item]},
                status=200
            )
        else:
            raise Exception(f"Error: resource {item} does not exist.")
    except Exception as e:
        return response.json(
            {"error": str(e)},
            status=500
        )


@inventory_bp.route("/inventory", methods=["POST"])
async def set_inventory_all(request):
    """Set the inventory of all items, if they don't exist.
    """

    try:
        inv_check = [
            i for i in request.json.keys() if i in inventory.keys()
        ]

        if len(inv_check) > 0:
            raise Exception(
                f"Error: resources {inv_check} already exist."
            )

        inventory.update(request.json)

        return response.json(
            loads((await get_inventory_all(request)).body),
            status=201
        )
    except Exception as e:
        return response.json(
            {"error": str(e)},
            status=500
        )


@inventory_bp.route("/inventory/<item>", methods=["POST"])
async def set_inventory(request, item):
    """Set the inventory of a specific item, if it does not exist.
    """

    try:
        payload = request.json

        if item not in payload.keys() or len(payload.keys()) > 1:
            raise Exception(
                f"Error: uri item {item} does not match payload {payload}."
            )
        elif item in inventory.keys():
            raise Exception(
                f"Error: resource {item} already exists."
            )

        inventory[item] = payload[item]

        return response.json(
            loads((await get_inventory(request, item)).body),
            status=201
        )
    except Exception as e:
        return response.json(
            {"error": str(e)},
            status=500
        )


@inventory_bp.route("/inventory", methods=["PUT"])
async def update_inventory_all(request):
    """Update the inventory of all items, if they exist.
    """

    try:
        payload = request.json

        inv_check = [i for i in payload.keys() if i not in inventory.keys()]

        if len(inv_check) > 0:
            raise Exception(
                f"Error: resources {inv_check} don't exist."
            )

        inventory.update(request.json)

        return response.json(
            loads((await get_inventory(request)).body),
            status=200
        )
    except Exception as e:
        return response.json(
            {"error": str(e)},
            status=500
        )


@inventory_bp.route("/inventory/<item>", methods=["PUT"])
async def update_inventory(request, item):
    """Update the inventory of a specific item, if it exists.
    """

    try:
        payload = request.json

        if item not in payload.keys() or len(payload.keys()) > 1:
            raise Exception(
                f"Error: uri item {item} does not match payload {payload}."
            )
        elif item not in inventory.keys():
            raise Exception(
                f"Error: resource {item} does not exist."
            )

        inventory[item] = payload[item]

        return response.json(
            loads((await get_inventory(request, item)).body),
            status=200
        )
    except Exception as e:
        return response.json(
            {"error": str(e)},
            status=500
        )

# @alerts.route("/<id>")
# async def get(request, id):
#     try:
#         collection = mongo.connect(True, True)

#         result = await collection.find_one({"_id": ObjectId(id)})
#         if result is not None:
#             result["_id"] = str(result["_id"])

#         return response.json(result)
#     except Exception as e:
#         return response.text(
#             f"{e}",
#             status=500
#         )


# @alerts.route("/", methods=["POST"])
# async def post(request):
#     try:
#         body = request.json
#         body["date"] = f"{datetime.utcnow()}"

#         collection = mongo.connect(True, True)

#         result = (await gather(
#             collection.insert_one(body)
#         ))[0].inserted_id

#         return response.text(f"Success; mongo id: {result}")
#     except Exception as e:
#         return response.text(
#             f"{e}",
#             status=500
#         )


# @alerts.route("/<id>", methods=["PUT"])
# async def put(request, id):
#     try:
#         body = request.json
#         body["date"] = f"{datetime.utcnow()}"

#         collection = mongo.connect(True, True)

#         result = (await collection.update_one(
#             {"_id": ObjectId(id)},
#             {"$set": {i: j for i, j in body.items()}}
#         )).modified_count

#         if result != 1:
#             return response.text(
#                 "Failure",
#                 status=400
#             )
#         else:
#             return response.text("Success")
#     except Exception as e:
#         return response.text(
#             f"{e}",
#             status=500
#         )


# @alerts.route("/<id>", methods=["DELETE"])
# async def delete(request, id):
#     try:
#         collection = mongo.connect(True, True)

#         result = (await collection.delete_one(
#             {"_id": ObjectId(id)}
#         )).deleted_count

#         if result != 1:
#             return response.text(
#                 "Failure",
#                 status=400
#             )
#         else:
#             return response.text("Success")
#     except Exception as e:
#         return response.text(
#             f"{e}",
#             status=500
#         )
