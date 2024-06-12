import tkinter as tk
import customtkinter
from PIL import ImageTk, Image
import sqlite3

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("1080x720")
app.title('Esqueceu a Senha')

def recover_password():
    email = email_entry.get()

    if not email:
        error_label.config(text="Preencha o campo de email!")
        return

    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE email=?", (email,))
    user = cursor.fetchone()

    if user:
        # Envia email de recuperação de senha
        print(f"Email de recuperação de senha enviado para {email}!")
        error_label.config(text="Email de recuperação de senha enviado!")
    else:
        error_label.config(text="Email não encontrado!")

    conn.close()

img1 = ImageTk.PhotoImage(Image.open("./files/fundobranco.jpg"))
l1 = customtkinter.CTkLabel(master=app, image=img1)
l1.pack(fill="both", expand=True)

frame = customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

l2 = customtkinter.CTkLabel(master=frame, text="Esqueceu a Senha", font=('Century Gothic', 20))
l2.place(x=50, y=45)

email_label = customtkinter.CTkLabel(master=frame, text="Email:", font=('Century Gothic', 14))
email_label.place(x=50, y=110)
email_entry = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Digite seu email')
email_entry.place(x=50, y=140)

recover_button = customtkinter.CTkButton(master=frame, text="Recuperar Senha", command=recover_password, width=220, height=30, border_width=1, corner_radius=10)
recover_button.place(x=50, y=200)

error_label = customtkinter.CTkLabel(master=frame, text="", font=('Century Gothic', 12), text_color="red")
error_label.place(x=50, y=250)

app.mainloop()