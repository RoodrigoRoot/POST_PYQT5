# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inicioSesion.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import logging
import funcBaseDatos
import funcGrales

logging.basicConfig(
    level=logging.DEBUG
)

INIT_COL_USUARIO = 2
INIT_COL_USUARIO_ROL = 3

def fnArchivoExiste(sArchivo):
    return os.path.isfile(sArchivo)


class Ui_dlgSesion(object):
      
    def setupUi(self, dlgSesion):
        dlgSesion.setObjectName("dlgSesion")
        dlgSesion.resize(427, 370)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/bill.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dlgSesion.setWindowIcon(icon)
        dlgSesion.setModal(False)
        self.gbSesion = QtWidgets.QGroupBox(dlgSesion)
        self.gbSesion.setGeometry(QtCore.QRect(0, 10, 421, 281))
        self.gbSesion.setObjectName("gbSesion")
        self.lblUsuario = QtWidgets.QLabel(self.gbSesion)
        self.lblUsuario.setGeometry(QtCore.QRect(30, 60, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblUsuario.setFont(font)
        self.lblUsuario.setObjectName("lblUsuario")
        self.lblPassword = QtWidgets.QLabel(self.gbSesion)
        self.lblPassword.setGeometry(QtCore.QRect(30, 100, 131, 17))
        #font = QtGui.QFont()
        #font.setPointSize(14)
        self.lblPassword.setFont(font)
        self.lblPassword.setObjectName("lblPassword")
        self.lblNombre = QtWidgets.QLabel(self.gbSesion)
        self.lblNombre.setGeometry(QtCore.QRect(30, 140, 131, 17))
        #font = QtGui.QFont()
        #font.setPointSize(14)
        self.lblNombre.setFont(font)
        self.lblNombre.setObjectName("lblNombre")
        self.lblRol = QtWidgets.QLabel(self.gbSesion)
        self.lblRol.setGeometry(QtCore.QRect(30, 190, 131, 17))
        #font = QtGui.QFont()
        #font.setPointSize(14)
        self.lblRol.setFont(font)
        self.lblRol.setObjectName("lblRol")
        self.leUsuario = QtWidgets.QLineEdit(self.gbSesion)
        self.leUsuario.setGeometry(QtCore.QRect(160, 50, 211, 31))
        #font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.leUsuario.setFont(font)
        self.leUsuario.setInputMask("")
        self.leUsuario.setMaxLength(10)
        self.leUsuario.setObjectName("leUsuario")
        self.leUsuario.returnPressed.connect(self.fnProcesarEnter)
        self.leUsuario.keyPressEvent = self.KeyPressEvent
        self.leUsuario.textChanged.connect(self.fnProcesarCambioText)
        
        
        self.lePassword = QtWidgets.QLineEdit(self.gbSesion)
        self.lePassword.setGeometry(QtCore.QRect(160, 100, 211, 31))
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lePassword.setFont(font)
        self.lePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lePassword.setObjectName("lePassword")
        self.lePassword.returnPressed.connect(self.fnProcesarEnter)
        self.lePassword.keyPressEvent = self.KeyPressEvent
        self.lePassword.textChanged.connect(self.fnProcesarCambioText)
        
        
        self.leNombre = QtWidgets.QLineEdit(self.gbSesion)
        self.leNombre.setEnabled(False)
        self.leNombre.setGeometry(QtCore.QRect(160, 150, 211, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.leNombre.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.leNombre.setFont(font)
        self.leNombre.setReadOnly(True)
        self.leNombre.setObjectName("leNombre")
        self.leRol = QtWidgets.QLineEdit(self.gbSesion)
        self.leRol.setEnabled(False)
        self.leRol.setGeometry(QtCore.QRect(160, 200, 211, 31))
        self.leRol.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.leRol.setFont(font)
        self.leRol.setObjectName("leRol")
        self.pbAceptar = QtWidgets.QPushButton(dlgSesion)
        self.pbAceptar.setGeometry(QtCore.QRect(250, 310, 131, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbAceptar.setIcon(icon1)
        self.pbAceptar.setIconSize(QtCore.QSize(64, 64))
        self.pbAceptar.setObjectName("pbAceptar")
        self.pbAceptar.setAutoDefault(False)
        self.pbAceptar.keyPressEvent = self.KeyPressEvent
        self.pbAceptar.clicked.connect(self.fnProcesaClickAceptar)
        
        self.pbCancelar = QtWidgets.QPushButton(dlgSesion)
        self.pbCancelar.setGeometry(QtCore.QRect(110, 310, 121, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbCancelar.setIcon(icon2)
        self.pbCancelar.setIconSize(QtCore.QSize(32, 32))
        self.pbCancelar.setObjectName("pbCancelar")
        self.pbCancelar.setAutoDefault(False)
        self.retranslateUi(dlgSesion)
        QtCore.QMetaObject.connectSlotsByName(dlgSesion)

    def retranslateUi(self, dlgSesion):
        _translate = QtCore.QCoreApplication.translate
        dlgSesion.setWindowTitle(_translate("dlgSesion", "Usuario y Password"))
        self.gbSesion.setTitle(_translate("dlgSesion", "Inicio de Sesión"))
        self.lblUsuario.setText(_translate("dlgSesion", "Usuario:"))
        self.lblPassword.setText(_translate("dlgSesion", "Contraseña:"))
        self.lblNombre.setText(_translate("dlgSesion", "Nombre"))
        self.lblRol.setText(_translate("dlgSesion", "Rol:"))
        self.leUsuario.setToolTip(_translate("dlgSesion", "Ingresa tu Usuario"))
        self.lePassword.setToolTip(_translate("dlgSesion", "Ingresa tu contraseña"))
        self.leNombre.setText(_translate("dlgSesion", "Desconocido"))
        self.leRol.setText(_translate("dlgSesion", "Desconocido"))
        self.pbAceptar.setText(_translate("dlgSesion", "Aceptar"))
        self.pbCancelar.setText(_translate("dlgSesion", "Cancelar"))

    def fnProcesarEnter(self):
        print("has presionado enter")
        if self.leUsuario.hasFocus():
            print("Foco a password")
            self.lePassword.setFocus()
        else:
            print("Foco a aceptar")
            self.pbAceptar.setFocus()

    def fnProcesarCambioText(self):
        if self.leUsuario.hasFocus():
            pass
            #print(self.leUsuario.text())
        else:
            pass
            #print(self.lePassword.text())
    
    def KeyPressEvent(self, event):
        if self.leUsuario.hasFocus():
            if event.text() != 5:
                return QtWidgets.QLineEdit.keyPressEvent(self.leUsuario,event)
        elif self.lePassword.hasFocus():
            if event.text != 7:
                return QtWidgets.QLineEdit.keyPressEvent(self.lePassword,event)
        else:
            print("Se presiono aceptar")
            self.pbAceptar.hasFocus()
            if (event.key == QtCore.Qt.Key_Return):
                if self.fnValidaDAtos():
                    funcBaseDatos.fnConexionDB(self)
    
    def fnValidaDAtos(self):
        sMensaje = ""
        if len(self.leUsuario.text()) == 0:
            sMensaje = "El Usuario\n"
            self.leUsuario.hasFocus()
        if len(self.lePassword.text()) == 0:
            if len(sMensaje) == 0:
                self.lePassword.hasFocus()
            sMensaje = sMensaje + "El Password"
        if len(sMensaje)>0:
            sMensaje = "Revise los siguientes datos\n" + sMensaje
            funcGrales.fnMensaje(sMensaje, "El usuario y password no pueden quedar vacios")
            return False
        else:
            funcGrales.fnMensaje("Los datos están Correctos", "Intentaremos el acceso")
            return True
            
        
    
    def fnProcesaClickAceptar(self):
        if self.fnValidaDAtos():
            funcBaseDatos.fnConexionDB(self)
       

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlgSesion = QtWidgets.QDialog()
    ui = Ui_dlgSesion()
    ui.setupUi(dlgSesion)
    dlgSesion.show()
    sys.exit(app.exec_())
