import tkinter as tk
from tkinter import messagebox

def salvar_mensagem_em_arquivo():
    mensagem = mensagem_texto.get('1.0', tk.END)
    nome_arquivo = "mensagem_salva.txt"
    
    # Obter o caminho absoluto da pasta em que o código está localizado
    import os
    caminho_pasta_atual = os.path.dirname(os.path.abspath(__file__))

    # Combinar o caminho absoluto com o nome do arquivo de texto para criar o caminho completo do arquivo
    caminho_completo_arquivo = os.path.join(caminho_pasta_atual, nome_arquivo)

    # Salvar a mensagem em um arquivo de texto
    with open(caminho_completo_arquivo, 'w') as arquivo:
        arquivo.write(mensagem)
    
    # Mostrar mensagem de sucesso
    messagebox.showinfo("Mensagem Salva", "Mensagem salva com sucesso!")
    
    # Fechar a janela
    janela.quit()

# Criar a janela principal
janela = tk.Tk()
janela.title("Salvar Mensagem")

# Criar um campo de texto para digitar a mensagem
mensagem_texto = tk.Text(janela, wrap="word", height=10, width=50)
mensagem_texto.pack(pady=10)

# Criar um botão para salvar a mensagem
botao_salvar = tk.Button(janela, text="Salvar Mensagem", command=salvar_mensagem_em_arquivo)
botao_salvar.pack()

# Iniciar a execução da interface gráfica
janela.mainloop()