from PySide6 import QtWidgets

class Lobi(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sitio principal")
        self.resize(400,300)

        self.layout = QtWidgets.QVBoxLayout()

        self.texto = QtWidgets.QLabel("Ingresa el valor para decidir la retencion")
        self.layout.addWidget(self.texto)

        self.retencion = QtWidgets.QLineEdit()
        self.layout.addWidget(self.retencion)

        self.botonCalcular = QtWidgets.QPushButton("Clacular impuesto")
        self.layout.addWidget(self.botonCalcular)

        self.botonCalcular.clicked.connect(self.calcularRetencion)

        self.erro = QtWidgets.QLabel("")

        self.setLayout(self.layout)

    def calcularRetencion(self):
        if not self.erro.isVisible():
            self.layout.addWidget(self.erro)  
            self.erro.setVisible(True)
                  
        if not self.retencion.text(): 
            self.erro.setText("No se puede calcular la retención.")
        else:
            try:
                valor = float(self.retencion.text())
                self.texto.setText(f"La retención que tienes que pagar de esta factura es de {valor * 0.025}")
                self.erro.setVisible(False)  
            except ValueError:
                self.erro.setText("Por favor, ingrese un número válido.")
                




