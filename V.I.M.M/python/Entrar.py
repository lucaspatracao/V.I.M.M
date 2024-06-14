from customtkinter import *
from PIL import Image, ImageTk
import sqlite3
import os
import hashlib

# Constantes
ARQUIVO_DB = "usuarios.db"
NOME_TABELA = "usuarios"

class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x800")
        self.resizable(True, True)  # Permitir que a janela seja redimensionada

        imagem_de_fundo = CTkImage(light_image=Image.open("V.I.M.M\\img\\fundoroxo.jpg"), size=(1920, 1080))
        label_de_fundo = CTkLabel(master=self, image=imagem_de_fundo)
        label_de_fundo.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.frame_de_login = CTkFrame(master=self, fg_color="#ffffff", corner_radius=10)  # Arredondar bordas
        self.frame_de_login.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.5, relheight=0.6)  # Posicionar frame de login no centro e diminuir tamanho

        self.criar_widgets()

        self.configure(bg_color="#ffffff", bg_image=Image.open("V.I.M.M\\img\\fundobranco.jpg"), bg_opacity=0.5)

    def criar_widgets(self):
        # Criar widgets de login
        self.rotulo_de_titulo = CTkLabel(master=self.frame_de_login, text="Bem-Vindo de Volta!", text_color="#601E88", anchor="center", justify="center", font=("Arial Bold", 24))
        self.rotulo_de_titulo.place(relx=0.5, rely=0.1, anchor="center")

        self.rotulo_de_subtitulo = CTkLabel(master=self.frame_de_login, text="Faça login com sua conta", text_color="#7E7E7E", anchor="center", justify="center", font=("Arial Bold", 12))
        self.rotulo_de_subtitulo.place(relx=0.5, rely=0.17, anchor="center")

        self.icone_de_email = CTkImage(dark_image=Image.open("V.I.M.M\\img\\email-icon.png"), light_image=Image.open("V.I.M.M\\img\\email-icon.png"), size=(20,20))
        self.rotulo_de_email = CTkLabel(master=self.frame_de_login, text="  Email:", text_color="#601E88", anchor="center", justify="left", font=("Arial Bold", 14), image=self.icone_de_email, compound="left")
        self.rotulo_de_email.place(relx=0.5, rely=0.25, anchor="center")

        self.entrada_de_email = CTkEntry(master=self.frame_de_login, width=180, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
        self.entrada_de_email.place(relx=0.5, rely=0.35, anchor="center")

        self.icone_de_senha = CTkImage(dark_image=Image.open("V.I.M.M\\img\\password-icon.png"), light_image=Image.open("V.I.M.M\\img\\password-icon.png"), size=(17,17))
        self.rotulo_de_senha = CTkLabel(master=self.frame_de_login, text="  Senha:", text_color="#601E88", anchor="center", justify="left", font=("Arial Bold", 14), image=self.icone_de_senha, compound="left")
        self.rotulo_de_senha.place(relx=0.5, rely=0.45, anchor="center")

        self.entrada_de_senha = CTkEntry(master=self.frame_de_login, width=180, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*")
        self.entrada_de_senha.place(relx=0.5, rely=0.55, anchor="center")

        self.botao_de_login = CTkButton(master=self.frame_de_login, text="Login", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=180, command=lambda: self.logar_usuario())
        self.botao_de_login.place(relx=0.5, rely=0.65, anchor="center")

        self.rotulo_de_erro = CTkLabel(master=self.frame_de_login, text="", text_color="red", anchor="center", justify="center", font=("Arial Bold", 10))
        self.rotulo_de_erro.place(relx=0.5, rely=0.75, anchor="center")

        self.rotulo_de_cadastro = CTkLabel(master=self.frame_de_login, text="Não tem conta? Cadastre-se", text_color="#601E88", anchor="center", justify="center", font=("Arial Bold", 9), fg_color="#EEEEEE")
        self.rotulo_de_cadastro.place(relx=0.5, rely=0.85, anchor="center")

        self.rotulo_de_cadastro.bind("<Button-1>", lambda event: self.abrir_cadastro())

    def logar_usuario(self):
        email = self.entrada_de_email.get()
        senha = self.entrada_de_senha.get()
        if email and senha:
            if self.verificar_usuario_existe(email):
                conexao = sqlite3.connect(ARQUIVO_DB)
                cursor = conexao.cursor()
                cursor.execute(f"SELECT senha FROM {NOME_TABELA} WHERE email =?", (email,))
                stored_senha = cursor.fetchone()[0]
                if self.hash_password(senha) == stored_senha:
                    # Logar usuário
                    self.rotulo_de_erro.configure(text="Login realizado com sucesso!")
                else:
                    self.rotulo_de_erro.configure(text="Email ou senha inválidos!")
            else:
                self.rotulo_de_erro.configure(text="Usuário não encontrado!")
        else:
            self.rotulo_de_erro.configure(text="Preencha todos os campos!")

    def verificar_usuario_existe(self, email):
        # Verificar se o usuário existe no banco de dados
        conexao = sqlite3.connect(ARQUIVO_DB)
        cursor = conexao.cursor()
        cursor.execute(f"SELECT 1 FROM {NOME_TABELA} WHERE email =?", (email,))
        if cursor.fetchone():
            return True
        return False

    def hash_password(self, password):
        # Hash the password
        return hashlib.sha256(password.encode()).hexdigest()

    def abrir_cadastro(self):
        # Fechar a janela atual e abrir a janela de cadastro
        self.destroy()
        tela_cadastro = CadastrarApp()
        tela_cadastro.mainloop()

if __name__ == "__main__":
    app = App()
    app.mainloop()