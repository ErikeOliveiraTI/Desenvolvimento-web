from disciplina import Disciplina

class DisciplinaDAO:
    def __init__(self, conn):
        self.conn = conn

    def connect(self):
        # definindo um cursor
        cursor = self.conn.cursor()
        return cursor

    def getAll(self, email_aluno):
        sql = """
          SELECT * FROM disciplinas WHERE email_aluno=?;
          """
        values = (email_aluno,)
        cursor = self.connect()
        rows = cursor.execute(sql, values).fetchall()
        cursor.close()
        return rows

    def inserirDisciplina(self, email_aluno, nome):
        cursor = self.connect()
        sql = """
                  INSERT INTO disciplinas (email_aluno, nome) 
                  VALUES (?,?)
                  """

        values = (email_aluno, nome)

        cursor.execute(sql, values)

        # Certificar que os dados foram persistidos.
        self.conn.commit()


        return True
