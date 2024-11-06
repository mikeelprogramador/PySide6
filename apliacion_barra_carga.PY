import sys
import time
from PySide6 import QtWidgets, QtCore

class VentanaDeCarga(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cargando...")
        self.setGeometry(100, 100, 300, 100)

        # Crear una barra de progreso
        self.progress_bar = QtWidgets.QProgressBar(self)
        self.progress_bar.setRange(0, 100)  # Rango de 0 a 100
        self.progress_bar.setValue(0)  # Iniciar con 0%
        self.progress_bar.setTextVisible(True)  # No mostrar el texto de porcentaje
        self.progress_bar.setFormat("Cargando... %p%")  # Muestra el texto y el porcentaje
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.progress_bar)

        # Iniciar la tarea
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.actualizarProgreso)
        self.timer.start(50)  # Actualizar cada 50 ms

        self.progreso = 0  # Inicializamos el progreso en 0

    def actualizarProgreso(self):
        self.progreso += 1  # Aumentamos el progreso
        self.progress_bar.setValue(self.progreso)

        # Simulamos un proceso largo
        if self.progreso >= 100:
            self.timer.stop()  # Detener el temporizador
            self.cargarVentanaPrincipal()  # Llamar a la función para cargar la ventana principal

    def cargarVentanaPrincipal(self):
        # Una vez que la barra de carga haya llegado al 100%, cerramos esta ventana y mostramos la principal
        self.close()
        self.ventana_principal = Aplicacion()
        self.ventana_principal.show()

class Aplicacion(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.conteo = 0
        self.setWindowTitle("Reten app")
        self.resize(400,300)

        self.layout = QtWidgets.QVBoxLayout()

        self.label = QtWidgets.QLabel("")
        self.button = QtWidgets.QPushButton("Contar clic")

        self.layout.addWidget(self.label)  # Agregar la etiqueta al layout
        self.layout.addWidget(self.button)  # Agregar el botón al layout

        self.setLayout(self.layout)  # Asignar el layout a la ventana principal

        self.button.clicked.connect(self.contarClic)

        self.botonCerrarApliacion = QtWidgets.QPushButton("Cerrar aplaicion")
        self.layout.addWidget(self.botonCerrarApliacion)
        self.botonCerrarApliacion.clicked.connect(self.close)

    def contarClic(self):
        self.conteo += 1
        self.label.setText(f"Has echo clic {self.conteo}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # Mostrar la ventana de carga al principio
    ventana_de_carga = VentanaDeCarga()
    ventana_de_carga.show()

    sys.exit(app.exec())  # Ejecutar el ciclo de eventos de la aplicación
