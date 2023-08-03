import os
import sounddevice as sd
import wavio

def gravar_audio(nome_arquivo, duracao_segundos):
    taxa_amostragem = 44100
    canais = 2

    print("Gravando áudio...")
    gravacao = sd.rec(int(taxa_amostragem * duracao_segundos), samplerate=taxa_amostragem, channels=canais)
    sd.wait()
    print("Gravação concluída.")

    # Obter o caminho absoluto da pasta em que o código está localizado
    caminho_pasta_atual = os.path.dirname(os.path.abspath(__file__))

    # Combinar o caminho absoluto com o nome do arquivo de áudio para criar o caminho completo do arquivo
    caminho_completo_arquivo = os.path.join(caminho_pasta_atual, nome_arquivo)

    # Salva o áudio em um arquivo WAV
    wavio.write(caminho_completo_arquivo, gravacao, taxa_amostragem, sampwidth=2)

if __name__ == "__main__":
    nome_arquivo = "audio_gravado.wav"
    duracao_segundos = 5

    gravar_audio(nome_arquivo, duracao_segundos)