import logging
from flask import render_template, Flask, has_request_context, request
from flask import g, request
from rfc3339 import rfc3339
import flask_login
import os
import datetime
import time

class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
            record.url = request.url
            record.request_method = request.method
            record.request_path = request.path
            record.ip = request.headers.get('X-Forwarded-For', request.remote_addr)
            record.host = request.host.split(':', 1)[0]
            record.args = dict(request.args)
            now = time.time()
            record.duration = round(now - g.start, 2)
            dt = datetime.datetime.fromtimestamp(now)
            record.time = rfc3339(dt, utc=True)
            
        else:
            record.url = None
            record.remote_addr = None

        return super().format(record)

