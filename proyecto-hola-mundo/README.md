# 1. Tutorial Hola Mundo con PySide 6
[Enlace de mi repositorio](https://github.com/JoelXD18/desarrollo-de-interfaces)
## Guía paso a paso
---
# 2. Objetivos
- Crear y activar un entorno virtual de Python
- Instalar dependencias con pip y generar un requirements.txt
- Ejecutar una ventana gráfica con QApplication y el bucle de eventos
- Separar la lógica de la interfaz (ventana.py) del punto de entrada (main.py)
---
# 3. Requisitos previos
- Python 3.11 o cualquier version que soporte PySide6:

  ***python --version***

- Sistema Operativo:

  ***Windows 11***

- Herramientas:

  ***GitHub y VScode***
---

# 4. Creación y activacion del entorno virtual

- Version de Python:
```bash
python --version
```
## Creacion:
```bash
python -m venv entorno
```
      
<img width="1465" height="197" alt="image" src="https://github.com/user-attachments/assets/e5b22609-14f4-4ff1-a409-c50da7510181" />



## Creacion:
```bash
cd entorno/Scripts
activate
```

  <img width="847" height="134" alt="image" src="https://github.com/user-attachments/assets/a28bb9ed-1af3-42cb-8053-59f26b65733c" />

---

# 5. Instalación de dependencias

## Instalar PySide6
```bash
pip install pyside6
```
<img width="1294" height="368" alt="image" src="https://github.com/user-attachments/assets/e0f3d719-fb08-4ddd-bb41-9b1f9964834e" />

## Generar el fichero requirements.txt

```bash
pip freeze > requirements.txt
```
<img width="1104" height="30" alt="image" src="https://github.com/user-attachments/assets/02901ffa-dafe-46d7-a4eb-00b35ed38841" />

---

# 6. Mi estrcutura

 proyecto-hola-mundo/
 ├─ src/
 │  ├─ main.py          # punto de entrada
 │  └─ ventana.py       # clase Ventana
 ├─ .gitignore
 ├─ requirements.txt
 └─ README.md

 ---

 # 7. Codigo fuente de la aplicación 

 ## main.py

 ```python
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
```

## ventana.py
```python
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
```
---

# 8. Ejecucion y prueba

Para ejecutar la aplicación, abre una terminal en la carpeta raíz del proyecto y entra a la carpeta `src`:

```bash
cd src
python main.py
```
<img width="1280" height="364" alt="image" src="https://github.com/user-attachments/assets/72119a02-24d9-48d6-a1da-61e61ac9b01b" />

