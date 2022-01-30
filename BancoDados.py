import mysql.connector


class Conexao:
    def __init__(self, host="localhost",
                 user="root",
                 passwd="ksopri72",
                 database="tela_login"):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database

    def conecta(self):
        self.con = mysql.connector.connect(host=self.host,
                                           user=self.user,
                                           passwd=self.passwd,
                                           database=self.database)
        self.cur = self.con.cursor()

    def desconecta(self):
        self.con.close()

    def consulta(self, dado):
        self.conecta()
        sql = f"SELECT {dado} FROM usuarios"
        self.cur.execute(sql)
        x = self.cur.fetchall()
        self.desconecta()
        return x

    def consulta_where(self,dado,condicao):
        self.conecta()
        sql = f"SELECT {dado} FROM usuarios WHERE {condicao}"
        self.cur.execute(sql)
        x = self.cur.fetchall()
        self.desconecta()
        return x

    def insert(self, sql):
        self.conecta()
        self.cur.execute(f"INSERT INTO usuarios VALUES ({sql})")
        self.con.commit()

    def delete(self,sql):
        self.conecta()
        self.cur.execute(sql)
        self.con.commit()
        ### delete("DELETE FROM usuarios WHERE user = PedroG")