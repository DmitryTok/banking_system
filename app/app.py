from flask import Flask
from flask_restful import Api
from flasgger import Swagger

from app.config import SWAGGER_CONFIG, SWAGGER_TEMPLATE
from app.logger import logger_config
from app.routes import api_routes
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


def create_app() -> Flask:
    logger_config()

    app = Flask(__name__)
    api = Api(app, prefix="/api/v1")
    Swagger(app, template=SWAGGER_TEMPLATE, config=SWAGGER_CONFIG)

    Limiter(
        key_func=get_remote_address, app=app, default_limits=["10 per hour"]
    )

    api_routes(api)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True, use_reloader=True)
