import tkinter as tk
from tkinter import messagebox
import gspread
from google.oauth2.service_account import Credentials
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Configuração do Google Sheets API
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SERVICE_ACCOUNT_FILE = "path/to/your/service_account.json" # Substitua pelo caminho do seu arquivo de credenciais
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
gc = gspread.authorize(creds)
sheet = gc.open_by_url('your_sheet_url').sheet1 # Substitua pela URL da sua planilha

# Interface gráfica
window = tk.Tk()
window.title('Cadastro de Alunos')

# Campos de entrada
tk.Label(window, text='Nome:').grid(row=0, column=0)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1)

tk.Label(window, text='Endereço:').grid(row=1, column=0)
address_entry = tk.Entry(window)
address_entry.grid(row=1, column=1)

tk.Label(window, text='Matrícula:').grid(row=2, column=0)
id_entry = tk.Entry(window)
id_entry.grid(row=2, column=1)

tk.Label(window, text='Telefone:').grid(row=3, column=0)
phone_entry = tk.Entry(window)
phone_entry.grid(row=3, column=1)

# Funções para as operações CRUD
def create_student():
    name = name_entry.get()
    address = address_entry.get()
    id = id_entry.get()
    phone = phone_entry.get()
    sheet.append_row([name, address, id, phone])
    messagebox.showinfo('Sucesso', 'Aluno cadastrado com sucesso!')

def read_students():
    students = sheet.get_all_values()
    # Implemente a lógica para exibir os alunos na interface
    print(students)

def update_student():
    # Implemente a lógica para atualizar um aluno
    pass

def delete_student():
    # Implemente a lógica para deletar um aluno
    pass

def generate_pdf():
    students = sheet.get_all_values()
    c = canvas.Canvas('alunos.pdf', pagesize=letter)
    y = 750
    for student in students:
        c.drawString(100, y, f'Nome: {student[0]}, Endereço: {student[1]}, Matrícula: {student[2]}, Telefone: {student[3]}')
        y -= 20
    c.save()
    messagebox.showinfo('Sucesso', 'Relatório gerado com sucesso!')

# Botões
tk.Button(window, text='Cadastrar', command=create_student).grid(row=4, column=0)
tk.Button(window, text='Listar', command=read_students).grid(row=4, column=1)
tk.Button(window, text='Atualizar', command=update_student).grid(row=5, column=0)
tk.Button(window, text='Deletar', command=delete_student).grid(row=5, column=1)
tk.Button(window, text='Gerar PDF', command=generate_pdf).grid(row=6, column=0, columnspan=2)

window.mainloop()