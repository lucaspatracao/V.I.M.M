import tkinter as tk
import customtkinter
from PIL import ImageTk, Image
import sqlite3
import os
import google.oauth2
from google.oauth2 import service_account, id_token
import msal
import requests
import webbrowser

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("1080x720")
app.title('Cadastro')

GOOGLE_CLIENT_ID = 'YOUR_GOOGLE_CLIENT_ID_HERE'
MICROSOFT_CLIENT_ID = 'YOUR_MICROSOFT_CLIENT_ID_HERE'

def register_user():
    email = email_entry.get()
    password = password_entry.get()
    cargo = cargo_entry.get()

    if not all([email, password, cargo]):
        error_label.configure(text="Preencha todos os campos!")
        return

    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                      (email TEXT PRIMARY KEY, password TEXT, cargo TEXT)''')

    cursor.execute("INSERT INTO usuarios (email, password, cargo) VALUES (?,?,?)", (email, password, cargo))
    conn.commit()

    error_label.configure(text="Cadastro realizado com sucesso!")

    conn.close()

def register_user_google():
    # Crie um flow de autenticação com o client ID
    flow = service_account.Credentials.from_service_account_file(
        'path/to/your/service_account_key.json',
        scopes=['openid', 'email', 'profile']
    )

    # Redirecione o usuário para a página de autenticação do Google
    auth_url, _ = flow.authorization_url()
    webbrowser.open(auth_url, new=2)  # Abre a URL em um novo navegador

    # Aguarde o usuário autorizar o acesso
    auth_response = input("Enter the authorization code: ")

    # Troque o código de autorização por um token de acesso
    token_response = flow.fetch_token(code=auth_response)
    credentials = token_response.credentials

    # Verifique o token de acesso
    request = requests.Request()
    id_info = id_token.verify_oauth2_token(
        token_response.id_token,
        request,
        audience=GOOGLE_CLIENT_ID
    )

    # Extrai as informações do usuário do token de acesso
    email = id_info['email']
    name = id_info['name']

    # Crie um novo usuário com as informações do Google
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (email, password, cargo) VALUES (?,?,?)", (email, '', ''))
    conn.commit()
    conn.close()

    error_label.configure(text="Cadastro realizado com sucesso!")

def register_user_microsoft():
    # Crie um aplicativo de autenticação com o client ID
    app = msal.PublicClientApplication(
        client_id=MICROSOFT_CLIENT_ID,
        authority="https://login.microsoftonline.com/consumers"
    )

    # Redirecione o usuário para a página de autenticação da Microsoft
    flow = app.acquire_token_interactive(scopes=["openid", "email", "profile"])
    auth_url = flow.authorization_uri()
    webbrowser.open(auth_url, new=2)  # Abre a URL em um novo navegador

    # Aguarde o usuário autorizar o acesso
    result = flow.execute_pending()

    # Extrai as informações do usuário do token de acesso
    email = result['id_token_claims']['email']
    name = result['id_token_claims']['name']

    # Crie um novo usuário com as informações da Microsoft
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (email, password, cargo) VALUES (?,?,?)", (email, '', ''))
    conn.commit()
    conn.close()

    error_label.configure(text="Cadastro realizado com sucesso!")

img1 = ImageTk.PhotoImage(Image.open("D:\\GITHUB\\V.I.M.M\\V.I.M.M\img\\fundobranco.jpg"))
l1 = customtkinter.CTkLabel(master=app, image=img1)
l1.pack(fill="both", expand=True)

frame = customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

l2 = customtkinter.CTkLabel(master=frame, text="Cadastro", font=('Century Gothic', 20))
l2.place(x=50, y=45)

email_label = customtkinter.CTkLabel(master=frame, text="Email:", font=('Century Gothic', 14))
email_label.place(x=50, y=110)

email_entry = customtkinter.CTkEntry(master=frame, 
                                     width=200, 
                                     height=30, 
                                     border_width=1, 
                                     corner_radius=10)
email_entry.place(x=50, y=140)

password_label = customtkinter.CTkLabel(master=frame, 
                                        text="Senha:", 
                                        font=('Century Gothic', 14))
password_label.place(x=50, y=180)

password_entry = customtkinter.CTkEntry(master=frame, 
                                        width=200, 
                                        height=30, 
                                        border_width=1, 
                                        corner_radius=10, 
                                        show="*")
password_entry.place(x=50, y=210)

cargo_label = customtkinter.CTkLabel(master=frame, 
                                     text="Cargo:", 
                                     font=('Century Gothic', 14))
cargo_label.place(x=50, y=250)

cargo_entry = customtkinter.CTkEntry(master=frame, 
                                     width=200, 
                                     height=30, 
                                     border_width=1, 
                                     corner_radius=10)
cargo_entry.place(x=50, y=280)

register_button = customtkinter.CTkButton(master=frame, 
                                          text="Cadastrar", 
                                          command=register_user, 
                                          width=100, 
                                          height=30, 
                                          border_width=1, 
                                          corner_radius=10)
register_button.place(x=50, y=320)

google_button = customtkinter.CTkButton(master=frame, 
                                        text="Cadastrar com Google", 
                                        command=register_user_google, 
                                        width=150, 
                                        height=30, 
                                        border_width=1, 
                                        corner_radius=10)
google_button.place(x=50, y=360)

microsoft_button = customtkinter.CTkButton(master=frame, 
                                           text="Cadastrar com Microsoft", 
                                           command=register_user_microsoft, 
                                           width=150, 
                                           height=30, 
                                           border_width=1, 
                                           corner_radius=10)
microsoft_button.place(x=50, y=400)

error_label = customtkinter.CTkLabel(master=frame, 
                                     text="", 
                                     font=('Century Gothic', 12), 
                                     text_color="red")
error_label.place(x=50, y=440)

app.mainloop()