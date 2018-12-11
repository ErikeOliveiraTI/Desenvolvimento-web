from atividade import Atividade


class AtividadeDAO:
    def __init__(self, conn):
        self.conn = conn

    def connect(self):
        # definindo um cursor
        cursor = self.conn.cursor()
        return cursor

    def getAll(self, email_aluno):
        sql = """
          SELECT * FROM atividades WHERE email_aluno=?;
          """
        values = (email_aluno)
        cursor = self.connect()
        rows = cursor.execute(sql, values).fetchall()
        cursor.close()
        return rows

    def inserirAtividade(self, email_aluno, nome, professor, assunto):
        cursor = self.connect()
        sql = """
                  INSERT INTO disciplinas (email_aluno, nome, professor, assunto) 
                  VALUES (?,?,?,?)
                  """

        values = (email_aluno, nome, professor, assunto)

        cursor.execute(sql, values)

        # Certificar que os dados foram persistidos.
        self.conn.commit()

        print("Atividade inserida")
        return True

    def deletarAtividade(self, nome):
        cursor = self.connect()
        sql = """
                          DELETE FROM atividades WHERE nome=?
                          """

        values = (nome)

        cursor.execute(sql, values)

        # Certificar que os dados foram persistidos.
        self.conn.commit()

        print("Atividade apagada")
        return True
