import json

from flask import Flask

from event_queue import EventQueue
from tasks import LightsOnTask
from tasks import LightsOffTask
from tasks import QueryOpenWeatherMapApiTaskMedellin

app = Flask(__name__)
queue = EventQueue()

TEXT = { 'success' : True }
CODE = 200
TYPE = { 'ContentType':'application/json' } 


def _success_response():
    """Returns a default response indicating successful task submission.

    """
    return json.dumps(TEXT), CODE, TYPE


@app.route('/lights_on')
def lights_on():
    task = LightsOnTask()
    queue.enqueue(task)
    return _success_response()


@app.route('/lights_off')
def lights_off():
    task = LightsOffTask()
    queue.enqueue(task)
    return _success_response()


@app.route('/query_weather_medellin')
def query_weather_medellin():
    task = QueryOpenWeatherMapApiTaskMedellin()
    queue.enqueue(task)
    return _success_response()