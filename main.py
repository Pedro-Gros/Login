from telnetlib import LOGOUT
from PyQt6 import uic,QtWidgets
from CrudLogin import Login

def login():
    tela_login.frame_erro.hide()
    usuario = tela_login.lineedit_user.text()
    senha = tela_login.lineedit_senha.text()

    if Login().logar(usuario, senha) == 0:
        tela_login.close()
        tela_main.show()
        
    elif Login().logar(usuario, senha) == 1:
        tela_login.frame_erro.show()
        tela_login.label_erro.setText("Usuario Incorreto")
    else:
        tela_login.frame_erro.show()
        tela_login.label_erro.setText("Senha Incorreta")

def logout():
    tela_login.lineedit_user.clear()
    tela_login.lineedit_senha.clear()
    tela_main.close()
    tela_login.show()


app = QtWidgets.QApplication([])
tela_login = uic.loadUi("Login.ui")
tela_main = uic.loadUi("Main.ui")
tela_login.pushButton_entrar.clicked.connect(login)
tela_main.bt_sair.clicked.connect(logout)
tela_login.frame_erro.hide()

tela_login.show()
app.exec()