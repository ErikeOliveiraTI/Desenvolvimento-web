# 02_create_schema.py
import sqlite3
conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()
def criarBD():
  # conectando...

  # definindo um cursor

  # criando a tabela (schema)
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR NOT NULL,
            email VARCHAR NOT NULL,
            matricula VARCHAR NOT NULL,
            senha VARCHAR NOT NULL
    );
    
    """)

  # desconectando...
  conn.commit()
  conn.close()

def criar_disciplina():
  cursor.execute('''CREATE TABLE IF NOT EXISTS disciplinas (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            email_aluno VARCHAR NOT NULL,
            nome VARCHAR NOT NULL,
            FOREIGN KEY (email_aluno) REFERENCES clientes(email)
    );''')
  conn.commit()

def criar_atividade():

  cursor.execute('''
    CREATE TABLE IF NOT EXISTS atividades (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            email_aluno VARCHAR NOT NULL,
            nome VARCHAR NOT NULL,
            professor VARCHAR NOT NULL,
            assunto TEXT NOT NULL,
            FOREIGN KEY (email_aluno) REFERENCES clientes(email)
    );''')
  conn.commit()
criar_disciplina()
criar_atividade()


