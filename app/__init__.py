from flask import Flask
from flask_uploads import UploadSet, configure_uploads

from logscanner import logscanner_page

log_upload = UploadSet('logs')


def create_app(config=None):
    app = Flask('log-scanner')

    app.config.from_object(config)

    # for uploading log file
    configure_uploads(app, log_upload)

    app.register_blueprint(logscanner_page)

    return app
