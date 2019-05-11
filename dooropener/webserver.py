class WebServer:

    # Load libraries
    import time
    from bottle import Bottle, route, run

    def __init__(self, host, port, relay_controller):
        self._host = host
        self._port = port
        self._app = Bottle()
        self._route()
        self._relay_controller = relay_controller

    def _route(self):
        self._app.route('/sesame-open', callback=self._open)

    def start(self):
        self._app.run(host=self._host, port=self._port)

    def _open(self):
        relay_controller.activate_relay(5)
        return 'Sesame Opening'

