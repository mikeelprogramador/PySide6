import sys 
from PySide6 import QtWidgets

class aplicacion(QtWidgets.QWidget):
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
    window = aplicacion()
    window.show()
    sys.exit(app.exec())


#recordatorio, layout  es el cuerpo del programa no se puede cambiar el nombre es el nombre de la libreria, no se puede modificar