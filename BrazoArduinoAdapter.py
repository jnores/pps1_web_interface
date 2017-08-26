from Brazo import Brazo
import socket;

class BrazoArduinoAdapter(Brazo):
    """docstring for BrazoArduinoAdapter."""
    # UDP_IP_ARDUINO = "127.0.0.1";
    UDP_IP_ARDUINO = "192.168.0.33";
    UDP_PORT_ARDUINO = 8108;

    def __init__(self):
        super(BrazoArduinoAdapter, self).__init__()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); # UDP = SOCK_DGRAM
        self.server_address = (self.UDP_IP_ARDUINO, self.UDP_PORT_ARDUINO);

    def mover(self,servo_id,desplazamiento):
        """ Implementacion del metodo de movimiento.
        En esta clase, la solicitud de movimiento se envia por udp a la
        aplicacion Unity que tiene el server corriendo.
        """
        print("Arduino mover ",servo_id," => ",desplazamiento)
        command="ROTAR("+str(servo_id)+","+str(desplazamiento)+")"
        self.sock.sendto(command.encode("utf8"),self.server_address);
