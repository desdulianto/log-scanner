import flask_uploads
from flask import Blueprint, render_template, request, flash, redirect, url_for

import app

logscanner_page = Blueprint('log_scanner_page', __name__,
                            template_folder='templates')


@logscanner_page.route('/', endpoint='index')
def index():
    return render_template('index.html')


@logscanner_page.route('/upload', methods=['GET', 'POST'], endpoint='upload')
def upload():
    if request.method == 'POST':
        log_file = request.files.get('log_file', None)
        if log_file is None:
            flash('Log file not found!')
            return redirect(request.url)

        try:
            filename = app.log_upload.save(log_file)
            flash('Log uploaded. Scanning...')
            return redirect(url_for('.index'))
        except flask_uploads.UploadNotAllowed:
            flash('File not allowed for upload')
    return render_template('index.html')
