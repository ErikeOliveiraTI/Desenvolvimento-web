import sqlite3
from usuario import Usuario

class UsuarioDAO():

    def __init__(self, conn):
        self.conn = conn

    def connect(self):
        # definindo um cursor
        cursor = self.conn.cursor()
        return cursor

    def login(self, email, senha):
        cursor = self.connect()
        sql = """
        SELECT * FROM clientes WHERE email = ? and senha = ?
    """

        val = (email, senha)

        row = cursor.execute(sql).fetchone()
        cursor.close()
        return row

    def getAll(self):
        sql = """
          SELECT * FROM clientes;
          """
        cursor = self.connect()
        row = cursor.execute(sql).fetchall()
        cursor.close()
        return row

    def insertUsuario(self, usuario):
        cursor = self.connect()
        sql = """
          INSERT INTO clientes (nome, email, matricula, senha) 
          VALUES (?,?,?,?)
          """

        values = (usuario.nome, usuario.email, usuario.matricula, usuario.senha)

        cursor.execute(sql, values)

        last_id = cursor.lastrowid
        p = self.getAll()
        print(p)
        # Certificar que os dados foram persistidos.
        self.conn.commit()

        print("Usuário inserido ")
        return last_id

    def montar_aluno(self, email):
        cursor = self.connect()
        sql = """
        SELECT * FROM clientes WHERE email=?"""
        values = (email)
        cursor.execute(sql, values)
        aluno = cursor.fecthone()
        aluno = Usuario(aluno[0], aluno[1], aluno[2], aluno[3])
        return aluno
