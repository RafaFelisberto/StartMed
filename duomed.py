import tkinter as tk
from tkinter import messagebox
import random

# Lista de perguntas do módulo Hemograma
perguntas = [
    {
        "questao": "Qual componente do hemograma avalia a capacidade do sangue de transportar oxigênio?",
        "opcoes": ["Leucócitos", "Hemoglobina", "Plaquetas", "Glicose"],
        "correta": "Hemoglobina"
    },
    {
        "questao": "Qual célula é responsável pela defesa do organismo?",
        "opcoes": ["Hemácias", "Plaquetas", "Leucócitos", "Fibrinogênio"],
        "correta": "Leucócitos"
    },
    {
        "questao": "Qual parte do hemograma reflete o volume médio de cada hemácia?",
        "opcoes": ["Hematócrito", "VCM (Volume Corpuscular Médio)", "HCM (Hemoglobina Corpuscular Média)", "CHCM"],
        "correta": "VCM (Volume Corpuscular Médio)"
    },
    {
        "questao": "O aumento patológico de plaquetas se chama:",
        "opcoes": ["Leucocitose", "Trombocitose", "Anemia", "Neutropenia"],
        "correta": "Trombocitose"
    }
]

# Embaralha as perguntas
random.shuffle(perguntas)

class MiniGame:
    def __init__(self, master):
        self.master = master
        master.title("Mini Game")
        master.geometry("600x350")
        
        self.score = 0
        self.q_index = 0
        
        # Frame para conteúdo dinâmico
        self.frame = tk.Frame(master)
        self.frame.pack(fill="both", expand=True)
        
        self.mostrar_pergunta()
    
    def mostrar_pergunta(self):
        # Limpa frame
        for widget in self.frame.winfo_children():
            widget.destroy()
        
        if self.q_index < len(perguntas):
            p = perguntas[self.q_index]
            
            # Questão
            label = tk.Label(self.frame, text=p["questao"], font=("Arial", 14), wraplength=550)
            label.pack(pady=20)
            
            # Embaralha as opções pra cada pergunta
            opcs = p["opcoes"].copy()
            random.shuffle(opcs)
            
            # Botões de opção
            for opc in opcs:
                btn = tk.Button(
                    self.frame, text=opc, font=("Arial", 12), width=40,
                    command=lambda escolha=opc: self.verificar(escolha)
                )
                btn.pack(pady=5)
        
        else:
            self.mostrar_resultado()
    
    def verificar(self, escolha):
        correta = perguntas[self.q_index]["correta"]
        if escolha == correta:
            self.score += 1
            messagebox.showinfo("Resultado", "✅ Correto!")
        else:
            messagebox.showerror("Resultado", f"❌ Incorreto!\nResposta certa: {correta}")
        
        self.q_index += 1
        self.mostrar_pergunta()
    
    def mostrar_resultado(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        
        msg = f"Você acertou {self.score} de {len(perguntas)} perguntas!"
        label = tk.Label(self.frame, text=msg, font=("Arial", 16))
        label.pack(pady=30)
        
        btn_reiniciar = tk.Button(
            self.frame, text="Reiniciar", font=("Arial", 12),
            command=self.reiniciar
        )
        btn_reiniciar.pack(pady=10)
        
        btn_sair = tk.Button(
            self.frame, text="Sair", font=("Arial", 12),
            command=self.master.quit
        )
        btn_sair.pack(pady=5)
    
    def reiniciar(self):
        random.shuffle(perguntas)
        self.score = 0
        self.q_index = 0
        self.mostrar_pergunta()


if __name__ == "__main__":
    root = tk.Tk()
    app = MiniGame(root)
    root.mainloop()