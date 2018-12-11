# 02_create_schema.py
import sqlite3


def criarBD():
  # conectando...
  conn = sqlite3.connect('clientes.db')
  # definindo um cursor
  cursor = conn.cursor()

  # criando a tabela (schema)
  try:
    cursor.execute("""
    CREATE TABLE clientes (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            matricula TEXT NOT NULL,
            senha TEXT NOT NULL
    );
    """)
  except:
    pass
  # desconectando...
  conn.close()