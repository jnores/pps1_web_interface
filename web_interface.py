#!/usr/bin/python3
import argparse
from BrazoServer import BrazoServer
from Brazo import Brazo
from BrazoContainer import BrazoContainer
from BrazoUnityAdapter import BrazoUnityAdapter
from BrazoArduinoAdapter import BrazoArduinoAdapter
from BrazoWebController import BrazoWebController

DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 8081

def run(ip, port):
	print('starting server...(',ip,':',str(port),')')

	# Server settings
	# Choose port 8080, for port 80, which is normally used for a http server, you need root access

	server_address = (ip, port)

	brazo = BrazoContainer()
	brazo.addBrazo(BrazoUnityAdapter())
	brazo.addBrazo(BrazoArduinoAdapter())

	httpd = BrazoServer(server_address, BrazoWebController,brazo)
	print('running server...')
	httpd.serve_forever()


# MAIN
# Se configuran los parametros disponibles y se procesa la entrada.
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--port','-p', type=int, default=DEFAULT_PORT,
                   help='numero de puerto (default: '+str(DEFAULT_PORT)+')')
parser.add_argument('--ip', default=DEFAULT_HOST,
                   help='ip de trabajo (default: '+str(DEFAULT_HOST)+')')
args = parser.parse_args()
# print(args)
#Inicia el server con los parametros pasados o los valores por default.
run(args.ip, args.port)
