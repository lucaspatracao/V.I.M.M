import tkinter as tk
import customtkinter
from PIL import ImageTk, Image
import sqlite3
import oauthlib

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("1080x720")
app.title('Login')

def login_user():
    email = email_entry.get()
    password = password_entry.get()

    if not all([email, password]):
        error_label.config(text="Preencha todos os campos!")
        return

    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE email=? AND password=?", (email, password))
    user = cursor.fetchone()

    if user:
        error_label.config(text="Login realizado com sucesso!")
        app.destroy()
        # import main_page
        # main_page.main()
    else:
        error_label.config(text="Email ou senha incorretos!")

    conn.close()

def login_user_google():
    # Código para entrar com Google
    pass

def login_user_microsoft():
    # Código para entrar com Microsoft
    pass

img1 = ImageTk.PhotoImage(Image.open("./files/fundobranco.jpg"))
l1 = customtkinter.CTkLabel(master=app, image=img1)
l1.pack(fill="both", expand=True)

frame = customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

l2 = customtkinter.CTkLabel(master=frame, text="Login", font=('Century Gothic', 20))
l2.place(x=50, y=45)

email_label = customtkinter.CTkLabel(master=frame, text="Email:", font=('Century Gothic', 14))
email_label.place(x=50, y=110)
email_entry = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Digite seu email')
email_entry.place(x=50, y=140)

password_label = customtkinter.CTkLabel(master=frame, text="Senha:", font=('Century Gothic', 14))
password_label.place(x=50, y=180)
password_entry = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Digite sua senha', show="*")
password_entry.place(x=50, y=210)

login_button = customtkinter.CTkButton(master=frame, text="Login", command=login_user, width=220, height=30, border_width=1, corner_radius=10)
login_button.place(x=50, y=250)

google_button = customtkinter.CTkButton(master=frame, text="Entrar com Google", command=login_user_google, width=220, height=30, border_width=1, corner_radius=10)
google_button.place(x=50, y=300)

microsoft_button = customtkinter.CTkButton(master=frame, text="Entrar com Microsoft", command=login_user_microsoft, width=220, height=30, border_width=1, corner_radius=10)
microsoft_button.place(x=50, y=350)

error_label = customtkinter.CTkLabel(master=frame, text="", font=('Century Gothic', 12), text_color="red")
error_label.place(x=50, y=390)

app.mainloop()