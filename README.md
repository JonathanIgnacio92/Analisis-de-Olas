# Sistema de Monitoreo de Olas Costeras 🌊

Este es un programa interactivo desarrollado en Python diseñado para evaluar las condiciones marítimas (altura de olas y velocidad del viento) y determinar si el entorno es apto y seguro para la práctica de surf, además de entregar alertas preventivas.

El proyecto está estructurado bajo un enfoque de **modularización**, dividiendo la lógica de negocio, los cálculos y la interfaz de consola en archivos separados para mejorar la mantenibilidad del código.

## 📁 Estructura del Proyecto

El sistema se compone de los siguientes módulos:

* **`main.py`**: El punto de entrada de la aplicación. Gestiona el menú interactivo, la captura de datos del usuario y coordina los flujos de las demás funciones.
* **`calculos.py`**: Contiene la lógica analítica del sistema, evaluando si las olas son surfeables, si el viento representa un peligro y los límites obligatorios de temperatura para el equipamiento.
* **`pantalla.py`**: Encargado exclusivamente de la presentación visual y elementos estéticos de los menús en la consola.

## 🚀 Cómo ejecutar el proyecto

1. Asegúrate de tener instalado **Python 3.x**.
2. Clona o descarga este repositorio en tu máquina.
3. Abre una terminal en la carpeta del proyecto.
4. Ejecuta el archivo principal utilizando el siguiente comando:
   ```bash
   python main.py
