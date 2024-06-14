from tkinter import Toplevel
from tkcalendar import Calendar
import customtkinter as ctk
from datetime import datetime

def on_add_button_click():
    add_window = ctk.CTkToplevel()
    add_window.title("Adicionar Tarefa")
    add_window.geometry("300x200")
    add_window.config(bg='white')

    name_label = ctk.CTkLabel(add_window, text="Nome:")
    name_label.pack()
    name_entry = ctk.CTkEntry(add_window, width=200, height=30)
    name_entry.pack()

    desc_label = ctk.CTkLabel(add_window, text="Descrição:")
    desc_label.pack()
    desc_entry = ctk.CTkEntry(add_window, width=200, height=30)
    desc_entry.pack()

    time_label = ctk.CTkLabel(add_window, text="Hora:")
    time_label.pack()
    time_entry = ctk.CTkEntry(add_window, width=200, height=30)
    time_entry.pack()

    def add_task():
        name = name_entry.get()
        desc = desc_entry.get()
        time = time_entry.get()
        # Adicionar a tarefa à lista de tarefas

    add_button = ctk.CTkButton(add_window, text="Adicionar", fg_color="purple", hover_color="purple", command=add_task, border_width=2, border_color="purple")
    add_button.pack()

def on_remove_button_click():
    remove_window = ctk.CTkToplevel()
    remove_window.title("Remover Tarefa")
    remove_window.geometry("300x200")
    remove_window.config(bg='white')

    name_label = ctk.CTkLabel(remove_window, text="Nome:")
    name_label.pack()
    name_entry = ctk.CTkEntry(remove_window, width=200, height=30)
    name_entry.pack()

    def remove_task():
        name = name_entry.get()
        # Remover a tarefa da lista de tarefas

    remove_button = ctk.CTkButton(remove_window, text="Remover", fg_color="purple", hover_color="purple", command=remove_task, border_width=2, border_color="purple")
    remove_button.pack()

def on_view_button_click():
    view_window = ctk.CTkToplevel()
    view_window.title("Visualizar Tarefas")
    view_window.geometry("300x400")
    view_window.config(bg='white')

    task_listbox = ctk.CTkListbox(view_window, width=250, height=300)
    task_listbox.pack()

    # Exibir as tarefas na lista

root = ctk.CTk()
root.geometry("1260x800")
root.config(bg='white')

frame = ctk.CTkFrame(root, fg_color="white", bg_color="white", corner_radius=10, border_width=2, border_color="purple")
frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.85)

cal = Calendar(frame, selectmode='day', locale='pt_BR', disabledforeground='red', cursor="hand2", background="white", foreground="purple", selectbackground="purple", selectforeground="white")
cal.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.75)

# Destacar as datas que possuem uma tarefa
cal.calevent_create(datetime.strptime('2023-03-15', '%Y-%m-%d').date(), text='', tags='task')
cal.tag_config('task', background='red', foreground='white')

button_frame = ctk.CTkFrame(frame, fg_color="white", bg_color="white", corner_radius=10, border_width=2, border_color="white")
button_frame.place(relx=0.05, rely=0.8, relwidth=0.9, relheight=0.15)

add_button = ctk.CTkButton(button_frame, text="Adicionar Tarefa", fg_color="purple", hover_color="purple", command=on_add_button_click, border_width=2, border_color="purple")
add_button.pack(side='left', padx=10, pady=10)

remove_button = ctk.CTkButton(button_frame, text="Remover Tarefa", fg_color="purple", hover_color="purple", command=on_remove_button_click, border_width=2, border_color="purple")
remove_button.pack(side='left', padx=10, pady=10)

view_button = ctk.CTkButton(button_frame, text="Visualizar Tarefas", fg_color="purple", hover_color="purple", command=on_view_button_click, border_width=2, border_color="purple")
view_button.pack(side='left', padx=10, pady=10)

root.mainloop()