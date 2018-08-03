import requests
from .util import value_error_if


class StationClient:

    def __init__(self, host: str):
        def fail_init_if(test, msg):
            value_error_if(test, "Failed to instantiate StationClient. {}".format(msg))

        fail_init_if(host is None, "Host is None")
        fail_init_if('/' in host, "Hostname contains invalid character '/'")
        fail_init_if(host.startswith("https"), "HTTPS Protocol not supported!")
        http_prefix = "http://"

        if not host.startswith(http_prefix):
            host = http_prefix + host
        self.host = host

    def _route(self, route):
        if not route.startswith('/'):
            route = '/' + route
        return self.host + route

    def request_name(self):
        route = self._route("name")
        return requests.get(route).content.decode().strip()

    def request_data(self, target_file):
        route = self._route("data")
        data = requests.get(route).content
        with open(target_file, 'wb') as f:
            f.write(data)
