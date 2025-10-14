import sys
from PySide6.QtWidgets import QApplication
from ventana import Ventana

# creo la app, si no no funciona nada
app = QApplication(sys.argv)

# creo mi ventana
ventana = Ventana()

# la muestro en pantalla
ventana.show()

# esto es para que la app siga abierta hasta que la cierre
sys.exit(app.exec())
