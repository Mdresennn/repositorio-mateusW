import tkinter as tk
from tkinter import messagebox

class PaginaCadastro:
    def __init__(self, root):
        self.root = root
        self.root.title("Página de Cadastro")
        self.root.geometry("300x400")
        self.root.configure(bg="black")
        
        self.criar_interface()

    def criar_interface(self):
        # Título
        titulo = tk.Label(self.root, text="Cadastro de Usuário", font=("Arial", 16), fg="red", bg="black")
        titulo.pack(pady=10)

        # Campo Nome
        tk.Label(self.root, text="Nome:", fg="red", bg="black").pack(anchor="w", padx=20, pady=5)
        self.entrada_nome = tk.Entry(self.root, bg="white", fg="black")
        self.entrada_nome.pack(fill="x", padx=20)

        # Campo E-mail
        tk.Label(self.root, text="E-mail:", fg="red", bg="black").pack(anchor="w", padx=20, pady=5)
        self.entrada_email = tk.Entry(self.root, bg="white", fg="black")
        self.entrada_email.pack(fill="x", padx=20)

        # Campo Senha
        tk.Label(self.root, text="Senha:", fg="red", bg="black").pack(anchor="w", padx=20, pady=5)
        self.entrada_senha = tk.Entry(self.root, show="*", bg="white", fg="black")
        self.entrada_senha.pack(fill="x", padx=20)

        # Botão de Cadastro
        botao_cadastrar = tk.Button(self.root, text="Cadastrar", command=self.cadastrar_usuario, bg="red", fg="black", activebackground="black", activeforeground="red")
        botao_cadastrar.pack(pady=20)

    def cadastrar_usuario(self):
        nome = self.entrada_nome.get()
        email = self.entrada_email.get()
        senha = self.entrada_senha.get()

        # Validação simples
        if not nome or not email or not senha:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!", parent=self.root)
            return

        # Exemplo de feedback (poderia ser salvo em banco de dados aqui)
        messagebox.showinfo("Sucesso", f"Usuário {nome} cadastrado com sucesso!", parent=self.root)

        # Limpar campos
        self.entrada_nome.delete(0, tk.END)
        self.entrada_email.delete(0, tk.END)
        self.entrada_senha.delete(0, tk.END)

# Inicialização da aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = PaginaCadastro(root)
    root.mainloop()
