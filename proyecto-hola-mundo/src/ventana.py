from PySide6.QtWidgets import QWidget, QLabel

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        # le pongo un titulo a la ventana
        self.setWindowTitle("Hola Mundo con PySide6")

        # creo una etiqueta para mostrar texto
        etiqueta = QLabel("¡Hola Mundo!", self)

        # la muevo un poco para que no quede en la esquina
        etiqueta.move(50, 50)

        # le doy un tamaño inicial a la ventana
        self.resize(300, 200)
