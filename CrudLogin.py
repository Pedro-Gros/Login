from BancoDados import Conexao

class Login(object):

    def __init__(self, usuario = "", senha = "", nomeUser = "", nivel =""):
        self.usuario = usuario
        self.senha = senha
        self.nomeUser = nomeUser
        self.nivel = nivel

    def conf_user(usuario):
        login = Conexao().consulta("user")
        y = len(login)
        aux = False
        for x in (0,y-1):
            if usuario == login[x][0]:
                aux = True
        return aux

    def logar(self, user, senha):
        if Login.conf_user(user):
            try:
                senha_bd = Conexao().consulta_where("senha", f"user = '{user}'")
            except:
                print("ERRO")

            if senha == senha_bd[0][0]:
                return 0
            else:
                return 2
        else:
            return 1