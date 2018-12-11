class Postit:
    def __init__(self, nome, tag, deadline):
        self.nome = nome
        self.tag = tag
        self.deadline = deadline

    def getnome(self):
        return self.nome

    def gettag(self):
        return self.tag

    def getdeadline(self):
        return self.deadline

    def setnome(self, nome):
        self.nome = nome

    def settag(self, tag):
        self.tag = tag

    def setdeadline(self, deadline):
        self.deadline = deadline



class Usuario:
    def __init__(self, nome, email, matricula, senha):
        self.nome = nome
        self.email = email
        self.matricula = matricula
        self.senha = senha
        self.logado = False

    def fazer_login(self ,email):
        if email in s.usuarios:
            self.logado = True
            return "Bem vindo de volta"



    def getnome(self):
        return self.nome

    def setsenha(self, senha):
        self.senha = senha

    '''
    def cadastrar_usuario(self, nome,email, matricula, senha):
  
      #aplicando usuario cadastrado na lista de users
      s.usuarios.append(usuario.nome)
      print("Usuario cadastrado !!!"+"\n")
      time.sleep(2)
    '''

    def cadastrar_disciplina(self ,nome ,email, matricula, senha):
        from main import s
        if usuario in s.usuarios:
            print("Usuario já existe")
        if len(senha ) <6:
            raise SenhaMenor6Exception("A senha deve conter no minimo 6 caracteres")
        else:
            novo_usuario= Usuario(nome, matricula, senha)
            self.usuarios.inserir(novo_usuario)
            self.matriculas.append(matricula)
            novo_usuario= Usuario(nome, matricula, senha)
            self.usuarios.append(novo_usuario)
            print("Usuario cadastrado na disciplina com sucesso")


    def cadastrar_postit(self, nome, matricula, tag, disciplina):
        postit = Postit(nome, tag ,deadline)

        # def arquivar_postit(self, nome, matricula, tag, disciplina,  deadline):

        # def editar_informacoes(self, nome, matricula, tag, deadline):

        # def salvar_informacoes_postit(self, nome, disciplina, matricula):


    def excluir_postit(self, matricula, disciplina):
        if usuario in self.usuario:
            print(matricula)
            self.disciplina = self.buscar_postit
            if disciplina in self.disciplina:
                if matricula.disciplina == self.postit:
                    self.disciplina = self.excluir_postit

# ------------------------------------------------------------------------#
