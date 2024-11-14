from PySide6 import QtWidgets,QtCore
from lobi import Lobi


class VentanaCarga(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cargando la aplicacion")
        self.resize(400,300)

        self.barra_progreso = QtWidgets.QProgressBar(self)
        self.barra_progreso.setRange(0,100)
        self.barra_progreso.setValue(0)
        self.barra_progreso.setTextVisible(True)
        self.barra_progreso.setFormat("Cargando ..%p%")
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.barra_progreso)

        self.tiempo = QtCore.QTimer(self)
        self.tiempo.timeout.connect(self.actualizarProgreso)
        self.tiempo.start(50)

        self.progreso = 0 

    def actualizarProgreso(self):
        self.progreso  += 1
        self.barra_progreso.setValue(self.progreso)

        if self.progreso >= 100:
            self.tiempo.stop()
            self.cargarVentanaPrincipal()

    def cargarVentanaPrincipal(self):
        self.close()
        self.ventanaPrincipal = Lobi()
        self.ventanaPrincipal.show()


