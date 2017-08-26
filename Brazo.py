class Brazo(object):
    SERVO_BASE = 0
    SERVO_HOMBRO = 1
    SERVO_CODO = 2
    SERVO_MUNIECA = 3
    SERVO_PINZA = 4

    def mover(self,servo_id,desplazamiento):
        """ Metodo encargado de procesar la solicitud de movimiento de uno de
        sus servos.
        :param servo_id: numero de servo a mover, segun las constantes definidas
        :param desplazamiento: delta de rotacion.
        """
        raise NotImplementedError("The method not implemented")
