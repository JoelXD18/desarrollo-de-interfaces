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

