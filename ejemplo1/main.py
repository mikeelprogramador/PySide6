from barra_cargar import VentanaCarga
from PySide6 import QtWidgets,QtCore
import sys

if __name__ ==  "__main__":
    app = QtWidgets.QApplication(sys.argv)

    ver_ventana = VentanaCarga()
    ver_ventana.show()

    sys.exit(app.exec())