from PyQt5.QtWidgets import QMessageBox

def fnMensaje(sMensaje, sInformacion):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setInformativeText(sInformacion)
    msg.setWindowTitle("¡Aviso!")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()
    return

if __name__ == "__main__":
    import sys
    from PyQt5 import QtCore, QtGui, QtWidgets
    app = QtWidgets.QApplication(sys.argv)
    fnMensaje("Ventana Lista", "Prueba Exitosa")