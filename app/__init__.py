from flask import Flask


def create_app(config=None):
    app = Flask('log-scanner')

    app.config.from_object(config)

    return app
