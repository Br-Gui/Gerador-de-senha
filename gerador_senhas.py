import customtkinter as ctk
from tkinter import messagebox, filedialog
import random
import string
import re
from datetime import datetime

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class GeradorSenhaApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gerador de Senhas Seguras")
        self.geometry("520x570")
        self.resizable(False, False)

        self.contador_senhas = 0
        self.tema_claro = True
        self.incluir_maiusculas = ctk.BooleanVar(value=True)
        self.incluir_minusculas = ctk.BooleanVar(value=True)
        self.incluir_numeros = ctk.BooleanVar(value=True)
        self.incluir_simbolos = ctk.BooleanVar(value=True)
        self.senha_var = ctk.StringVar()
        self.senha_completa = ""

        self.criar_interface()

    def criar_interface(self):
        frame = ctk.CTkFrame(self, corner_radius=12)
        frame.pack(expand=True, fill="both", padx=20, pady=20)

        top_frame = ctk.CTkFrame(frame, fg_color="transparent")
        top_frame.pack(fill="x")
        self.switch_tema = ctk.CTkSwitch(
            top_frame, text="Modo Claro", command=self.alternar_tema
        )
        self.switch_tema.pack(side="right", padx=8, pady=8)

        ctk.CTkLabel(frame, text="Gerador de Senhas Seguras",
                     font=("Segoe UI", 20, "bold")).pack(pady=(10, 10))

        frame_input = ctk.CTkFrame(frame, fg_color="transparent")
        frame_input.pack(pady=5)
        ctk.CTkLabel(frame_input, text="Comprimento da senha:",
                     font=("Segoe UI", 12)).grid(row=0, column=0, padx=5)
        self.entry_tamanho = ctk.CTkEntry(
            frame_input, width=60, font=("Segoe UI", 12), justify="center")
        self.entry_tamanho.grid(row=0, column=1, padx=5)
        self.entry_tamanho.insert(0, "12")

        frame_opcoes = ctk.CTkFrame(frame, fg_color="transparent")
        frame_opcoes.pack(pady=12)
        ctk.CTkCheckBox(frame_opcoes, text="Maiúsculas", variable=self.incluir_maiusculas).grid(
            row=0, column=0, padx=8, pady=5)
        ctk.CTkCheckBox(frame_opcoes, text="Minúsculas", variable=self.incluir_minusculas).grid(
            row=0, column=1, padx=8, pady=5)
        ctk.CTkCheckBox(frame_opcoes, text="Números", variable=self.incluir_numeros).grid(
            row=1, column=0, padx=8, pady=5)
        ctk.CTkCheckBox(frame_opcoes, text="Símbolos", variable=self.incluir_simbolos).grid(
            row=1, column=1, padx=8, pady=5)

        self.btn_gerar = ctk.CTkButton(
            frame, text="Gerar Senha", command=self.gerar, font=("Segoe UI", 12, "bold"), height=36
        )
        self.btn_gerar.pack(pady=(8, 8), fill="x", padx=30)

        self.label_senha = ctk.CTkEntry(frame, textvariable=self.senha_var, font=(
            "Consolas", 14, "bold"), width=340, justify="center")
        self.label_senha.pack(pady=12)

        self.label_forca = ctk.CTkLabel(frame, text="", font=("Segoe UI", 12))
        self.label_forca.pack(pady=2)
        self.barra_forca = ctk.CTkProgressBar(frame, width=320, height=18)
        self.barra_forca.pack(pady=6)
        self.barra_forca.set(0)

        frame_botoes = ctk.CTkFrame(frame, fg_color="transparent")
        frame_botoes.pack(pady=10)
        ctk.CTkButton(frame_botoes, text="Copiar", command=self.copiar, width=120).grid(row=0, column=0, padx=10)
        ctk.CTkButton(frame_botoes, text="Salvar", command=self.salvar, width=120).grid(row=0, column=1, padx=10)

        self.label_contador = ctk.CTkLabel(frame, text="Senhas geradas: 0", font=("Segoe UI", 10))
        self.label_contador.pack(pady=(16, 2))
        self.label_data = ctk.CTkLabel(frame, text="", font=("Segoe UI", 10))
        self.label_data.pack(pady=(2, 8))

    def alternar_tema(self):
        self.tema_claro = not self.tema_claro
        ctk.set_appearance_mode("light" if self.tema_claro else "dark")
        self.switch_tema.configure(
            text="Modo Claro" if self.tema_claro else "Modo Escuro")

    def gerar(self):
        try:
            tamanho = int(self.entry_tamanho.get())
            if tamanho < 4 or tamanho > 9999:
                raise ValueError("Digite um número entre 4 e 9999.")
            senha = self.gerar_senha(tamanho)
            self.senha_completa = senha
            self.senha_var.set(self.limitar_texto(senha, 32))
            forca, cor, valor = self.validar_forca(senha)
            self.label_forca.configure(
                text=f"Força da senha: {forca}", text_color=self.cor_forca(cor))
            self.barra_forca.set(valor / 100)
            self.contador_senhas += 1
            self.label_contador.configure(
                text=f"Senhas geradas: {self.contador_senhas}")
            self.label_data.configure(
                text=f"Gerada em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def copiar(self):
        senha = getattr(self, 'senha_completa', None)
        if senha:
            self.clipboard_clear()
            self.clipboard_append(senha)
            messagebox.showinfo("Copiado", "Senha copiada para a área de transferência!")

    def salvar(self):
        senha = getattr(self, 'senha_completa', None)
        if senha:
            caminho = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[
                ("Arquivo de Texto", "*.txt")])
            if caminho:
                with open(caminho, "w") as f:
                    f.write(f"Senha gerada: {senha}\n")
                    f.write(f"Data e hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
                messagebox.showinfo("Salvo", "Senha salva com sucesso!")

    def gerar_senha(self, tamanho):
        caracteres = ''
        if self.incluir_maiusculas.get():
            caracteres += string.ascii_uppercase
        if self.incluir_minusculas.get():
            caracteres += string.ascii_lowercase
        if self.incluir_numeros.get():
            caracteres += string.digits
        if self.incluir_simbolos.get():
            caracteres += string.punctuation
        if not caracteres:
            raise ValueError("Selecione pelo menos um tipo de caractere.")
        return ''.join(random.choices(caracteres, k=tamanho))

    def validar_forca(self, senha):
        comprimento = len(senha)
        tem_maiuscula = bool(re.search(r'[A-Z]', senha))
        tem_minuscula = bool(re.search(r'[a-z]', senha))
        tem_numero = bool(re.search(r'\d', senha))
        tem_simbolo = bool(re.search(r'\W', senha))
        pontuacao = sum([
            tem_maiuscula, tem_minuscula, tem_numero, tem_simbolo])
        if comprimento >= 12 and pontuacao == 4:
            return "Forte", "green", 100
        elif comprimento >= 8 and pontuacao >= 3:
            return "Média", "orange", 60
        else:
            return "Fraca", "red", 30

    def limitar_texto(self, texto, limite):
        return texto if len(texto) <= limite else texto[:limite-3] + "..."

    def cor_forca(self, cor):
        return {"green": "#22c55e", "orange": "#facc15", "red": "#ef4444"}.get(cor, "#000000")

if __name__ == "__main__":
    app = GeradorSenhaApp()
    app.mainloop()
