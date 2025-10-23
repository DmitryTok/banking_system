from flask import Flask
from flask_restful import Api
from flasgger import Swagger

from app.logger import logger_config
from app.routes import api_routes
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec",
            "route": "/apispec.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/",
}

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Banking System API",
        "description": "Auto-generated API documentation",
        "version": "1.0.0",
    },
    "basePath": "/",
}


def create_app() -> Flask:
    logger_config()

    app = Flask(__name__)
    api = Api(app, prefix="/api/v1")
    Swagger(app, template=swagger_template, config=swagger_config)

    Limiter(
        key_func=get_remote_address, app=app, default_limits=["10 per hour"]
    )

    api_routes(api)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True, use_reloader=True)
