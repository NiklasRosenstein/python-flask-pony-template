import flask
from . import config

app = flask.Flask(__name__split('.')[0])

from . import models, views

def run(*args, **kwargs):
  return app.run(*args, **kwargs)