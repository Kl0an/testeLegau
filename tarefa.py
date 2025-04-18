import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

# Criando a janela principal
janela = tk.Tk()
janela.title("tarefa.py Python - Interface Gráfica")
janela.geometry("600x500")

# Criando um notebook para abas
notebook = ttk.Notebook(janela)
notebook.pack(expand=True, fill="both")

# Criando frames para cada aba
frame_idade = ttk.Frame(notebook)
frame_listas = ttk.Frame(notebook)
frame_login = ttk.Frame(notebook)
frame_admin = ttk.Frame(notebook)  # Aba administrativa

notebook.add(frame_idade, text="Cálculo de Idade")
notebook.add(frame_listas, text="Listas e Desejos")
notebook.add(frame_login, text="Login")

# ---- Aba de Cálculo de Idade ----
hoje = date.today()

def calcular_idade():
    try:
        nome = entrada_nome.get()
        ano = int(entrada_ano.get())
        mes = int(entrada_mes.get())
        dia_nascimento = int(entrada_dia.get())

        meuDia = date(ano, mes, dia_nascimento)
        calcular = hoje - meuDia

        idade = hoje.year - meuDia.year
        dias_restantes = (90 - idade) * 365

        resultado_idade.config(text=f"Bem-vindo {nome.title()}!\n"
                                    f"{calcular.days} dias vividos.\n"
                                    f"Você tem {dias_restantes} dias até os 90 anos, aproximadamente.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira uma data válida.")

tk.Label(frame_idade, text="Digite seu nome:").pack(pady=5)
entrada_nome = tk.Entry(frame_idade)
entrada_nome.pack()

tk.Label(frame_idade, text=f"Hoje é {hoje.day}/{hoje.month}/{hoje.year}").pack()

tk.Label(frame_idade, text="Ano de nascimento:").pack()
entrada_ano = tk.Entry(frame_idade, width=10)
entrada_ano.pack()

tk.Label(frame_idade, text="Mês de nascimento:").pack()
entrada_mes = tk.Entry(frame_idade, width=5)
entrada_mes.pack()

tk.Label(frame_idade, text="Dia de nascimento:").pack()
entrada_dia = tk.Entry(frame_idade, width=5)
entrada_dia.pack()

tk.Button(frame_idade, text="Calcular Idade", command=calcular_idade).pack(pady=10)
resultado_idade = tk.Label(frame_idade, text="")
resultado_idade.pack()

# ---- Aba de Listas ----
def listar_desejos():
    desejos = ["nadar", "trabalhar", "namorar", "programar", "desenhar"]
    messagebox.showinfo("Lista de Desejos", "\n".join([f"Gostaria de um dia poder {desejo.title()}." for desejo in desejos]))

def listar_comidas():
    comidas = ["banana", "pippo's", "laranja", "monster", "fígado"]
    comidas[comidas.index("fígado")] = "frango"
    messagebox.showinfo("Lista de Comidas", "\n".join([f"Eu irei comer {comida}" for comida in comidas]))

def verificar_pares():
    numeros = [1, 3, 7, 80, 23, 11, 24, 48]
    pares = [str(numero) for numero in numeros if numero % 2 == 0]
    messagebox.showinfo("Números Pares", f"Pares encontrados:\n{', '.join(pares)}")

tk.Button(frame_listas, text="Listar Desejos", command=listar_desejos).pack(pady=5)
tk.Button(frame_listas, text="Listar Comidas", command=listar_comidas).pack(pady=5)
tk.Button(frame_listas, text="Verificar Números Pares", command=verificar_pares).pack(pady=5)

# ---- Aba de Login ----
def validar_login():
    usuario = entrada_usuario.get().strip()
    senha = entrada_senha.get().strip()

    if usuario.lower() == "daniel" and senha.lower() == "daniel":
        messagebox.showinfo("Login", "Bem-vindo Daniel! Modo Administrador ativado.")
        notebook.add(frame_admin, text="Administração")  # Adicionar aba administrativa
        janela.update()  # **Força a atualização da interface**
        carregar_sonhos()  # Carregar sonhos ao entrar no modo admin
    else:
        messagebox.showinfo("Login", f"Bem-vindo, {usuario}")

tk.Label(frame_login, text="Usuário:").pack(pady=5)
entrada_usuario = tk.Entry(frame_login)
entrada_usuario.pack()

tk.Label(frame_login, text="Senha:").pack()
entrada_senha = tk.Entry(frame_login, show="*")  # Oculta a senha
entrada_senha.pack()

tk.Button(frame_login, text="Validar Login", command=validar_login).pack(pady=10)

# ---- Aba Administrativa (Somente para Daniel) ----
tk.Label(frame_admin, text="Editor de Sonhos").pack(pady=5)
sonhos_area = tk.Text(frame_admin, height=10, width=60)
sonhos_area.pack()

def carregar_sonhos():
    try:
        with open("sonhos.txt", "r") as arquivo:
            sonhos_area.delete("1.0", tk.END)
            sonhos_area.insert("1.0", arquivo.read())
    except FileNotFoundError:
        sonhos_area.insert("1.0", "Nenhum sonho registrado ainda.")

def salvar_sonhos():
    with open("sonhos.txt", "w") as arquivo:
        arquivo.write(sonhos_area.get("1.0", tk.END))
    messagebox.showinfo("Admin", "Sonhos salvos com sucesso!")

tk.Button(frame_admin, text="Salvar Sonhos", command=salvar_sonhos).pack(pady=5)

# Executar a interface gráfica
janela.mainloop()