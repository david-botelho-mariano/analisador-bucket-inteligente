from keras.models import load_model  # Importa a função para carregar o modelo treinado
from PIL import Image, ImageOps  # Importa a biblioteca para manipular imagens
import numpy as np  # Importa a biblioteca NumPy para trabalhar com arrays
import matplotlib.pyplot as plt  # Importa a biblioteca para visualização de dados
import os  # Importa a biblioteca para trabalhar com sistema de arquivos


def baixar_bucket_s3(nome_bucket, diretorio_dump):
    try:        
        subprocess.run(["s3scanner", "dump", "--bucket", nome_bucket, "--dump-dir", diretorio_dump], check=True) # Executa o comando s3scanner para baixar o conteúdo do bucket S3        
        print(f"Bucket S3 '{nome_bucket}' baixado para '{diretorio_dump}'.")        
    except subprocess.CalledProcessError as e:        
        print(f"Erro ao baixar o bucket S3 '{nome_bucket}': {e}")
        return False
    return True

# Define a função para carregar o modelo treinado e os rótulos das classes
def carregar_modelo_treinado(caminho_modelo, caminho_rotulos):
    modelo = load_model(caminho_modelo, compile=False)  # Carrega o modelo treinado
    nomes_classes = open(caminho_rotulos, "r").readlines()  # Carrega os rótulos das classes
    return modelo, nomes_classes


# Define a função para preprocessar a imagem antes da classificação
def preprocessar_imagem(caminho_imagem):
    dados = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)  # Cria um array para armazenar a imagem processada
    imagem = Image.open(caminho_imagem).convert("RGB")  # Abre a imagem e converte para o formato RGB
    tamanho = (224, 224)  # Define o tamanho para o qual a imagem será redimensionada
    imagem = ImageOps.fit(imagem, tamanho, Image.Resampling.LANCZOS)  # Redimensiona a imagem com o método LANCZOS
    array_imagem = np.asarray(imagem)  # Converte a imagem em um array NumPy
    array_imagem_normalizada = (array_imagem.astype(np.float32) / 127.5) - 1  # Normaliza os valores dos pixels
    dados[0] = array_imagem_normalizada  # Armazena a imagem normalizada no array de dados
    return dados, imagem


# Define a função para fazer a previsão da classe da imagem
def prever_imagem(modelo, dados, nomes_classes):
    previsao = modelo.predict(dados)  # Faz a previsão da classe usando o modelo treinado
    indice = np.argmax(previsao)  # Obtém o índice da classe com maior probabilidade
    nome_classe = nomes_classes[indice]  # Obtém o nome da classe correspondente
    pontuacao_confianca = previsao[0][indice]  # Obtém a pontuação de confiança da previsão
    return nome_classe, pontuacao_confianca


# Define a função para processar todas as imagens em um diretório
def processar_imagens_no_diretorio(caminho_diretorio, modelo, nomes_classes):
    for nome_arquivo in os.listdir(caminho_diretorio):  # Itera sobre os arquivos no diretório
        # Verifica se o arquivo é uma imagem com extensão .jpg, .jpeg ou .png
        if nome_arquivo.endswith(".jpg") or nome_arquivo.endswith(".jpeg") or nome_arquivo.endswith(".png"):
            caminho_imagem = os.path.join(caminho_diretorio, nome_arquivo)
            dados, imagem = preprocessar_imagem(caminho_imagem)  # Preprocessa a imagem e obtém os dados normalizados
            nome_classe, pontuacao_confianca = prever_imagem(modelo, dados, nomes_classes)  # Preve a classe e a pontuação de confiança
            #print(f"Arquivo: {nome_arquivo}")  # Exibe o nome do arquivo da imagem
            #print("Classe:", nome_classe[2:], end="")  # Exibe a classe prevista
            #print("Pontuação de Confiança:", pontuacao_confianca)  # Exibe a pontuação de confiança da previsão
            plt.imshow(imagem)  # Mostra a imagem original
            plt.title(nome_classe[2:])  # Adiciona o título com a classe prevista à imagem
            plt.axis("off")  # Remove os eixos da imagem
            plt.show()  # Exibe a imagem com a classe prevista


if __name__ == "__main__":
    caminho_modelo = "modelo_keras.h5"
    caminho_rotulos = "categorias.txt"
    caminho_diretorio = "dataset misturado/"

    modelo, nomes_classes = carregar_modelo_treinado(caminho_modelo, caminho_rotulos)  # Carrega o modelo treinado e os rótulos das classes
    processar_imagens_no_diretorio(caminho_diretorio, modelo, nomes_classes)  # Processa e classifica as imagens no diretório
