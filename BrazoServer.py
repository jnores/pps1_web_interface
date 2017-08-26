from http.server import HTTPServer
from Brazo import Brazo

class BrazoServer(HTTPServer):
    """docstring for BrazoServer."""
    def __init__(self, server_address, requestHandlerClass,brazo):
        HTTPServer.__init__(self,server_address, requestHandlerClass)
        self.brazo = brazo
