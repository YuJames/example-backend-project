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
    return response.json(
        {
            "title": "Restaurant API",
            "description": (
                "A REST API service to support "
                "resturant operations."
            )
        }
    )


# ~~~~  MAIN  ~~~~ #
if __name__ == "__main__":
    app.run(config.host, config.port)
    loop = get_event_loop()
    server = loop.run_until_complete(app)

# ~~~~  DEAD CODE  ~~~~ #
