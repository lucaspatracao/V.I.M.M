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

        self.configure(bg_color="#ffffff")

        background_image = CTkImage(light_image=Image.open("img/fundoroxo.jpg"), size=(1920, 1080))
        background_label = CTkLabel(master=self, image=background_image)
        background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.frame_de_login = CTkFrame(master=self, fg_color="#ffffff", corner_radius=10)  # Arredondar bordas
        self.frame_de_login.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.5, relheight=0.6)  # Posicionar frame de login no centro e diminuir tamanho

        self.criar_widgets()

    def criar_widgets(self):
        # Criar widgets de login
        self.rotulo_de_titulo = CTkLabel(master=self.frame_de_login, text="Bem-Vindo de Volta!", text_color="#601E88", anchor="center", justify="center", font=("Arial Bold", 24))
        self.rotulo_de_titulo.place(relx=0.5, rely=0.1, anchor="center")

        self.rotulo_de_subtitulo = CTkLabel(master=self.frame_de_login, text="Faça login com sua conta", text_color="#7E7E7E", anchor="center", justify="center", font=("Arial Bold", 12))
        self.rotulo_de_subtitulo.place(relx=0.5, rely=0.17, anchor="center")

        self.icone_de_email = CTkImage(dark_image=Image.open("img/email-icon.png"), light_image=Image.open("img/email-icon.png"), size=(20,20))
        self.rotulo_de_email = CTkLabel(master=self.frame_de_login, text="  Email:", text_color="#601E88", anchor="center", justify="left", font=("Arial Bold", 14), image=self.icone_de_email, compound="left")
        self.rotulo_de_email.place(relx=0.5, rely=0.25, anchor="center")

        self.entrada_de_email = CTkEntry(master=self.frame_de_login, width=180, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
        self.entrada_de_email.place(relx=0.5, rely=0.35, anchor="center")

        self.icone_de_senha = CTkImage(dark_image=Image.open("img/password-icon.png"), light_image=Image.open("img/password-icon.png"), size=(17,17))
        self.rotulo_de_senha = CTkLabel(master=self.frame_de_login, text="  Senha:", text_color="#601E88", anchor="center", justify="left", font=("Arial Bold", 14), image=self.icone_de_senha, compound="left")
        self.rotulo_de_senha.place(relx=0.5, rely=0.45, anchor="center")

        self.entrada_de_senha = CTkEntry(master=self.frame_de_login, width=180, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*")
        self.entrada_de_senha.place(relx=0.5, rely=0.55, anchor="center")

        self.botao_de_login = CTkButton(master=self.frame_de_login, text="Login", command=self.verificar_login, width=180, height=40, fg_color="#601E88", hover_color="#7E7E7E", text_color="#FFFFFF", corner_radius=10)
        self.botao_de_login.place(relx=0.5, rely=0.65, anchor="center")

    def verificar_login(self):
        # Verificar se o usuário existe no banco de dados
        email = self.entrada_de_email.get()
        senha = self.entrada_de_senha.get()
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()

        conn = sqlite3.connect(ARQUIVO_DB)
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {NOME_TABELA} WHERE email =? AND senha =?", (email, senha_hash))
        usuario = cursor.fetchone()

        if usuario:
            print("Login realizado com sucesso!")
        else:
            print("Email ou senha incorretos!")

        conn.close()

if __name__ == "__main__":
    app = App()
    app.mainloop()