import time
from usuario import Usuario
import sqlite3
from CriarBD import criarBD
from UsuarioDAO import UsuarioDAO
from disciplinaDAO import DisciplinaDAO
from atividadeDAO import AtividadeDAO
#import  psycopg2


class SenhaMenor6Exception(Exception):
    pass


# ---------------------------------------------------------------------#


class Sistema:
    def __init__(self):
        self.nome = "Locus ad operadium"
        self.usuarios = []
        self.postits = []
        self.matriculas = []
        #self.conexao = psycopg2.connect(host="localhost", database="a_tarion", user="postgres", password="123")
        self.conn = sqlite3.connect('clientes.db')
        criarBD()

        self.usuarioDAO = UsuarioDAO(self.conn)
        self.disciplinaDAO = DisciplinaDAO(self.conn)
        self.atividadeDAO = AtividadeDAO(self.conn)
        # self.usuarioDAO.insertUsuario(Usuario('nome', 'email', 'mat', 'senha'))
        # print(self.usuarioDAO.getAll())

    def login(self, email, senha):
        sql = """
        SELECT * FROM clientes WHERE email = ? and senha = ?
    """

        val = (email, senha)

        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM clientes WHERE email = ? and senha = ?", (email, senha,))
        resultado = cursor.fetchone()
        cursor.close()
        return resultado

    def getusuario(self,email,senha):
        usuario_logado = self.login(email,senha)
        return usuario_logado

    def cadastrarDisciplina(self, email_aluno, nome):
        self.disciplinaDAO.inserirDisciplina(email_aluno, nome)
        print('Disciplina cadastrada\n')

    def visualizarDisciplinas(self, email_aluno):
        disciplinas = self.disciplinaDAO.getAll(email_aluno)
        print('Disciplinas\n'
              '')
        for disciplina in disciplinas:
            print('Nome: ' + disciplina[2]+'\n'
                                           '')

    def adicionarAtividade(self, email_aluno, nome, professor, assunto):
        self.atividadeDAO.inserirAtividade(email_aluno, nome, professor, assunto)
        print('Atividade cadastrada')

    def visualizarAtividades(self, email_aluno):
        atividades = self.atividadeDAO.getAll(email_aluno)
        print('Atividades\n'
              '')
        for atividade in atividades:
            print('Nome: ' + atividade[2])
            print('Professor: ' + atividade[3])
            print('Assunto: ' + atividade[4])
            print('')

    def getpostit(self):
        return self.postit

    def get_emails(self):
        return self.emails

    def buscar_atividade(self, matricula):
        for disciplina in self.disciplina:
            if disciplina.matricula == postit:
                return (atividade)
            else:
                pass

    def tela_inicial(self):
        print("Seja bem vindo!\n")
        print("R - Registrar")
        print("E - Entrar")
        # convertendo valores para maiusculo
        op = input("voce deseja? ").upper()
        if op == "R":
            nome = input("Digite seu nome:")
            email = input("Informe seu email:")
            matricula = input("Digite a matricula:")
            senha = input("Digite a senha, deve conter no minimo 6 caracteres:")
            if len(senha) < 6:
                print("Senha muito pequena, refaça-a!")
                while len(senha) < 6:
                    senha = input("Digite a senha, deve conter no minimo 6 caracteres:")
            else:
                usuario = Usuario(nome,email,matricula,senha)
                self.usuarioDAO.insertUsuario(usuario)
                print("Usuario cadastrado com sucesso!\n")
                time.sleep(1)
                self.tela_inicial()
                # usuario.login()


        elif op == "E":
            email = input("Informe seu email:")
            senha = input("Digite a senha:")
            logado = self.login(email,senha)
            if logado:
                user = self.usuarioDAO.montar_aluno(email)
                print("Usuario " + logado[1] + " logado!\n")
                time.sleep(1)
                self.menu(user)
            else:
                print("Dados incorretos")
                time.sleep(1)
                self.tela_inicial()

            # usuario vai logar no sistema

    def cadastrar_usuario(self, usuario):
        # aplicando usuario cadastrado na lista de users
        self.usuarios.append(usuario.email)

        self.usuarioDAO.insertUsuario(usuario)
        print("Usuario cadastrado !!!" + "\n")
        print(self.usuarios)
        time.sleep(2)
        self.usuarioDAO.montar_aluno(usuario.email)
        s.menu()

    def menu(self, user):
        print("☝ BEM-VINDO", user.nome, "✌")
        opcao = -1
        while (opcao is not 'x'):
            print("1- Cadastrar disciplina")
            print("2- Cadastrar atividade")
            print("3- Visualizar disciplinas")
            print("4- Visualizar atividades")
            print("5- Excluir atividade")
            print('x- Sair')
            opcao = input("Digite a opção:")

            if opcao == '1':
                nome = input('Digite o nome da disciplina: ')
                self.cadastrarDisciplina(user.email, nome)

            if opcao == '2':
                nome = input("nome da atividade: ").upper()
                professor = input("Qual o nome do professor: ")
                assunto = input("Assunto: ")
                self.adicionarAtividade(user.email, nome, professor, assunto)

            if opcao == '3':
                self.visualizarDisciplinas(user.email)

            if opcao == '4':
                self.visualizarAtividades(user.email)

            if opcao == '5':
                nome = input("qual atividade: ").upper()
                self.atividadeDAO.deletarAtividade(nome, user.email)
                pass

            '''if opçao == '1':
              nome= input("Digite seu nome:")
              email = input("Informe seu email:")
              matricula= input("Digite a matricula:")
              senha= input("Digite a senha, deve conter no minimo 6 caracteres")
              try:
                usuario = Usuario(nome,email,matricula,senha)
                s.cadastrar_usuario(usuario)
              except SenhaMenor6Exception as s:
                print('O usuário não foi cadastrado. Erro:', s)

            if opçao == '2':
                tag = input("QUE TIPO DE TAG[prova/seminario...]?:")
                matricula= input("Digite a matricula:")
                senha= input("Digite a senha:")
                disciplina= self.disciplina(matricula,senha)
                
                deadline = input("entregar quando?")

                # print(disciplina)

            if opçao == '3':
                matricula = input("Digite a matricula:")
                
                1º criar função "criar_postit"
                2º inserir postist na lista de postits criados
                
                postit = self.postits()

            if opçao == '4':
                matricula = input("Digite a matricula:")
                self.mostrar_usuarios()
                self.editar_informacoes()

            if opçao == '5':
                matricula = input("Digite a matricula:")
                print(self.buscar_postit(matricula))

            if opçao == '6':
                print(self.buscar_postit(matricula))
                self.excluir_postit()

            elif opçao == 'x':
                pass'''


s = Sistema()
s.tela_inicial()
# --------------------------------------------------------------------------#
'''Zclass Usuario:
  def __init__(self, nome, email, matricula, senha):
    self.nome = nome
    self.email = email
    self.matricula = matricula
    self.senha = senha

  def getnome(self):
    return self.nome

  def setsenha(self, senha):
    self.senha = senha


  def cadastrar_usuario(self, nome,email, matricula, senha):

    #aplicando usuario cadastrado na lista de users
    s.usuarios.append(usuario.nome)
    print("Usuario cadastrado !!!"+"\n")
    time.sleep(2)


  def cadastrar_disciplina(self,nome,email, matricula, senha):
    if usuario in s.usuarios:
      print("Usuario já existe")
    if len(senha)<6:
      raise SenhaMenor6Exception("A senha deve conter no minimo 6 caracteres")
    else:
      novo_usuario= Usuario(nome, matricula, senha)
      self.usuarios.inserir(novo_usuario)
      self.matriculas.append(matricula)
      novo_usuario= Usuario(nome, matricula, senha)
      self.usuarios.append(novo_usuario)
      print("Usuario cadastrado na disciplina com sucesso")


  def cadastrar_postit(self, nome, matricula, tag, disciplina):
    postit = Postit(nome, tag,deadline)



    #def arquivar_postit(self, nome, matricula, tag, disciplina,  deadline):


    #def editar_informacoes(self, nome, matricula, tag, deadline):


    #def salvar_informacoes_postit(self, nome, disciplina, matricula):


  def excluir_postit(self, matricula, disciplina):
    if usuario in self.usuario:
      print(matricula)
      self.disciplina = self.buscar_postit
      if disciplina in self.disciplina:
        if matricula.disciplina == self.postit:
          self.disciplina = self.excluir_postit

#------------------------------------------------------------------------#
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

'''