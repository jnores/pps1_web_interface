from Brazo import Brazo

class BrazoContainer(Brazo):
    """docstring for BrazoContainer."""

    def __init__(self):
        super(BrazoContainer, self).__init__()
        self.arrBrazos=[]

    def addBrazo(self, brazo):
        """ Se agrega un brazo al container para ser manipulado de manera
        sincronizada con otros brazos.
        """
        if brazo not in self.arrBrazos:
            self.arrBrazos.append(brazo);
    def removeBrazo(self, brazo):
        """ Se quita un brazo al container para ser manipulado de manera
        sincronizada con otros brazos.
        """
        if brazo in self.arrBrazos:
            self.arrBrazos.remove(brazo);

    def mover(self,servo_id,desplazamiento):
        """ Implementacion del metodo de movimiento.
        En esta clase, la solicitud de movimiento se ejecuta en cada Brazo que
        se haya agergado al container.
        """
        print("Container mover ",servo_id," => ",desplazamiento)
        for brazo in self.arrBrazos:
            try:
                brazo.mover(servo_id,desplazamiento)
            except Exception as e:
                print (e)
                pass
