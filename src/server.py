#!/usr/bin/env python3

"""RESTful server.
Create a RESTful server with some functionalities to interact with inventory.
Arguments:
    
ToDo:
    ~~~~NOW~~~~
    ~~~~CONSIDERATION~~~~
    ~~~~PERIODICALLY~~~~
"""

# ~~~~  IMPORTS  ~~~~ #
from asyncio import (
    get_event_loop
)
from sanic import (
    response,
    Sanic
)

from config import (
    config
)
from routes import (
    v1
)

# ~~~~  PRIVATE GLOBAL VARIABLES  ~~~~ #

# ~~~~  PUBLIC GLOBAL VARIABLES  ~~~~ #
app = Sanic(__name__)
app.blueprint(v1)

# ~~~~  PRIVATE CLASSES  ~~~~ #

# ~~~~  PUBLIC CLASSES  ~~~~ #

# ~~~~  PRIVATE FUNCTIONS  ~~~~ #

# ~~~~  PUBLIC FUNCTIONS  ~~~~ #
@app.route("/")
async def root(request):
    """Informational root endpoint.
    """

    return response.json(
        {
            "title": "Restaurant API",
            "description": (
                "A REST API service to support "
                "restaurant operations."
            ),
            "endpoints": {
                "/": [
                    {
                        "method": "GET",
                        "description": "base information",
                        "payload": None
                    }
                ],
                "v1/api/departments/kitchen/inventory/": [
                    {
                        "method": "GET",
                        "description": "get all items",
                        "payload": None
                    },
                    {
                        "method": "POST",
                        "description": "set all items",
                        "payload": "json of any number of 'new ingredient': 'number' pairings"
                    },
                    {
                        "method": "PUT",
                        "description": "update all items",
                        "payload": "json of any number of 'current ingredient': 'number' pairings"
                    }
                ],
                "v1/api/departments/kitchen/inventory/<item>": [
                    {
                        "method": "GET",
                        "description": "get an item",
                        "payload": None
                    },
                    {
                        "method": "POST",
                        "description": "set an item",
                        "payload": "json of a 'new ingredient': 'number' pairing"
                    },
                    {
                        "method": "PUT",
                        "description": "update an item",
                        "payload": "json of a 'current ingredient': 'number' pairing"
                    }
                ]
            }
        }
    )


# ~~~~  MAIN  ~~~~ #
if __name__ == "__main__":
    app.run(config.host, config.port)
    loop = get_event_loop()
    server = loop.run_until_complete(app)

# ~~~~  DEAD CODE  ~~~~ #
