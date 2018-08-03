import requests
from .util import value_error_if


class StationClient:

    def __init__(self, host: str):
        def fail_init_if(test, msg):
            value_error_if(test, "Failed to instantiate StationClient. {}".format(msg))

        fail_init_if(host is None, "Host is None")
        fail_init_if('/' in host, "Hostname contains invalid character '/'")
        fail_init_if(host.startswith("https"), "HTTPS Protocol not supported!")

        if not host.startswith("http"):
            host = "http://" + host
        self.host = host

    def _route(self, route):
        if not route.startswith('/'):
            route = '/' + route
        return self.host + route

    def request_name(self):
        route = self._route("name")
        return requests.get(route).content.decode().strip()
