import time
from bottle import Bottle, route, run
from relaycontroller import RelayController

class WebServer:

    def __init__(self, host, port, relay_controller):
        self._host = host
        self._port = port
        self._app = Bottle()
        self._route()
        self._relay_controller = relay_controller

    def _route(self):
        self._app.route('/sesame-open', callback=self._open)
        self._app.route('/sesame-open/<seconds>', callback=self._open_with_time)


    def start(self):
        self._app.run(host=self._host, port=self._port)

    def _open(self):
        self._relay_controller.activate_relay(activation_time=5)
        return 'Sesame Opening'

    def _open_with_time(self, seconds):
        self._relay_controller.activate_relay(activation_time=int(seconds))
        return_string = ('Sesame Opening for {0} seconds'.format(seconds))
        return return_string