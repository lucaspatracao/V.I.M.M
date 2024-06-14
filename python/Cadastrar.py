# Importar bibliotecas necessárias
import sqlite3
from customtkinter import *  # Biblioteca para criar interfaces gráficas
from PIL import Image  # Biblioteca para trabalhar com imagens
import webbrowser  # Biblioteca para abrir links na internet
import hashlib  # Biblioteca para criptografar senhas
from Entrar import App as LoginApp  # Importar a classe App do módulo Entrar

# Constantes
ARQUIVO_DB = "usuarios.db"  # Nome do arquivo de banco de dados
NOME_TABELA = "usuarios"  # Nome da tabela de usuários
FAMILIA_FONTE = "Montserrat"  # Família de fonte usada na interface
TAMANHO_FONTE_TITULO = 24  # Tamanho da fonte do título
TAMANHO_FONTE_SUBTITULO = 12  # Tamanho da fonte do subtítulo
TAMANHO_FONTE_ROTULO = 14  # Tamanho da fonte dos rótulos
TAMANHO_FONTE_BOTAO = 10  # Tamanho da fonte dos botões

# Funções de banco de dados
def criar_banco_de_dados():
    # Cria um banco de dados SQLite se ele não existir
    conexao = sqlite3.connect(ARQUIVO_DB)  # Conectar ao banco de dados
    cursor = conexao.cursor()  # Criar um cursor para executar comandos
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {NOME_TABELA} (
            email TEXT PRIMARY KEY,
            senha TEXT
        )
    """)  # Criar tabela de usuários se não existir
    conexao.close()  # Fechar conexão com o banco de dados

def armazenar_usuario(email, senha):
    # Armazena um usuário no banco de dados
    conexao = sqlite3.connect(ARQUIVO_DB)  # Conectar ao banco de dados
    cursor = conexao.cursor()  # Criar um cursor para executar comandos
    cursor.execute(f"SELECT 1 FROM {NOME_TABELA} WHERE email =?", (email,))  # Verificar se o email já existe
    if cursor.fetchone():  # Se o email já existe
        print("Email já cadastrado!")  # Mostrar mensagem de erro
    else:
        cursor.execute(f"INSERT INTO {NOME_TABELA} (email, senha) VALUES (?,?)", (email, hashlib.sha256(senha.encode()).hexdigest()))  # Inserir usuário no banco de dados
        conexao.commit()  # Confirmar alterações
    conexao.close()  # Fechar conexão com o banco de dados

# Classe App
class App(CTk):
    def __init__(self):
        super().__init__()  # Inicializar a classe pai
        self.geometry("1280x800")  # Definir tamanho da janela
        self.resizable(True, True)  # Permitir redimensionamento da janela

        # Criar imagem de fundo
        background_image = CTkImage(light_image=Image.open("img/fundoroxo.jpg"), size=(1920, 1080))
        background_label = CTkLabel(master=self, image=background_image)
        background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Criar frame de cadastro
        self.frame_cadastro = CTkFrame(master=self, fg_color="#ffffff", corner_radius=10)
        self.frame_cadastro.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.5, relheight=0.6)

        self.criar_widgets()  # Criar widgets de cadastro

    def criar_widgets(self):
        # Criar widgets de cadastro
        self.rotulo_titulo = CTkLabel(master=self.frame_cadastro, text="Bem-Vindo!", text_color="#601E88", anchor="center", justify="center", font=(FAMILIA_FONTE, TAMANHO_FONTE_TITULO))
        self.rotulo_titulo.place(relx=0.5, rely=0.2, anchor="center")

        self.rotulo_subtitulo = CTkLabel(master=self.frame_cadastro, text="Cadastre-se com sua conta", text_color="#7E7E7E", anchor="center", justify="center", font=(FAMILIA_FONTE, TAMANHO_FONTE_SUBTITULO))
        self.rotulo_subtitulo.place(relx=0.5, rely=0.3, anchor="center")

        # Criar ícone de email
        self.icone_email = CTkImage(dark_image=Image.open("img/email-icon.png"), light_image=Image.open("img/email-icon.png"), size=(20,20))
        self.rotulo_email = CTkLabel(master=self.frame_cadastro, text="  Email:", text_color="#601E88", anchor="center", justify="left", font=(FAMILIA_FONTE, TAMANHO_FONTE_ROTULO), image=self.icone_email, compound="left")
        self.rotulo_email.place(relx=0.1, rely=0.4, anchor="w")

        # Criar entrada de email
        self.entrada_email = CTkEntry(master=self.frame_cadastro, width=250, height=30, corner_radius=10, fg_color="#EEEEEE", text_color="#7E7E7E", font=(FAMILIA_FONTE, 10))
        self.entrada_email.place(relx=0.5, rely=0.4, anchor="center")

        # Criar ícone de senha
        self.icone_senha = CTkImage(dark_image=Image.open("img/password-icon.png"), light_image=Image.open("img/password-icon.png"), size=(17,17))
        self.rotulo_senha = CTkLabel(master=self.frame_cadastro, text="  Senha:", text_color="#601E88", anchor="center", justify="left", font=(FAMILIA_FONTE, TAMANHO_FONTE_ROTULO), image=self.icone_senha, compound="left")
        self.rotulo_senha.place(relx=0.1, rely=0.5, anchor="w")

        # Criar entrada de senha
        self.entrada_senha = CTkEntry(master=self.frame_cadastro, width=250, height=30, corner_radius=10, fg_color="#EEEEEE", text_color="#7E7E7E", font=(FAMILIA_FONTE, 10), show="*")
        self.entrada_senha.place(relx=0.5, rely=0.5, anchor="center")

        # Criar botão de cadastro
        self.botao_cadastrar = CTkButton(master=self.frame_cadastro, text="Cadastre-se", fg_color="#601E88", hover_color="#601E88", font=(FAMILIA_FONTE, TAMANHO_FONTE_BOTAO), text_color="#FFFFFF", width=180, command=lambda: self.cadastrar_usuario())
        self.botao_cadastrar.place(relx=0.5, rely=0.6, anchor="center")

        # Criar botão de login com Microsoft
        self.icone_microsoft = CTkImage(dark_image=Image.open("img/microsoft-logo.png"), light_image=Image.open("img/microsoft-logo.png"), size=(20,20))
        self.botao_microsoft = CTkButton(master=self.frame_cadastro, text="Cadastrar-se com Microsoft", fg_color="#EEEEEE", hover_color="#EEEEEE", font=(FAMILIA_FONTE, TAMANHO_FONTE_BOTAO), text_color="#601E88", width=180, image=self.icone_microsoft, command=lambda: self.login_com_microsoft())
        self.botao_microsoft.place(relx=0.5, rely=0.7, anchor="center")

        #Criar label de já tem uma conta
        self.rotulo_ja_tem_conta = CTkLabel(master=self.frame_cadastro, text="Já tem uma conta? ", text_color="#7E7E7E", anchor="center", justify="center", font=(FAMILIA_FONTE, 10))
        self.rotulo_ja_tem_conta.place(relx=0.48, rely=0.75, anchor="center")

        # Criar label de login (clicável)
        self.rotulo_login = CTkLabel(master=self.frame_cadastro, text="Entre", text_color="purple", anchor="center", justify="center", font=(FAMILIA_FONTE, 10, "underline"))
        self.rotulo_login.place(relx=0.58, rely=0.75, anchor="center")
        self.rotulo_login.bind("<Button-1>", lambda e: self.abrir_login())

    def cadastrar_usuario(self):
        # Obter email e senha do usuário
        email = self.entrada_email.get()
        senha = self.entrada_senha.get()

        # Verificar se os campos estão preenchidos
        if email and senha:
            # Verificar se o email já existe
            if self.verificar_usuario_existe(email):
                self.rotulo_erro.configure(text="Email já cadastrado!")
                self.abrir_login()
            # Verificar se o email e senha são válidos
            elif self.validar_email(email) and self.validar_senha(senha):
                armazenar_usuario(email, senha)
                self.rotulo_erro.configure(text="Usuário cadastrado com sucesso!")
                self.abrir_login()
            else:
                self.rotulo_erro.configure(text="Email ou senha inválidos!")
        else:
            self.rotulo_erro.configure(text="Preencha todos os campos!")

    def login_com_microsoft(self):
        # Abrir link de login com Microsoft
        webbrowser.open("https://login.microsoftonline.com/")

    def abrir_login(self):
        # Abrir janela de login
        self.destroy()
        login_app = LoginApp()
        login_app.mainloop()

    def verificar_usuario_existe(self, email):
        # Verificar se o usuário já existe no banco de dados
        conexao = sqlite3.connect(ARQUIVO_DB)
        cursor = conexao.cursor()
        cursor.execute(f"SELECT 1 FROM {NOME_TABELA} WHERE email =?", (email,))
        if cursor.fetchone():
            return True
        else:
            return False

    def validar_email(self, email):
        # Validar email
        if "@" in email and "." in email:
            return True
        else:
            return False

    def validar_senha(self, senha):
        # Validar senha
        if len(senha) >= 8:
            return True
        else:
            return False

if __name__ == "__main__":
    criar_banco_de_dados()
    app = App()
    app.mainloop()