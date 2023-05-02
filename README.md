# Analisador bucket inteligente
Esse código executa a classificação de imagens usando um modelo Keras pré-treinado. O código baixa o conteúdo de um bucket do Amazon S3 especificado como um argumento de linha de comando usando a biblioteca s3scanner. Em seguida, ele carrega um modelo Keras pré-treinado de um arquivo salvo e uma lista de rótulos de classe de um arquivo de texto. O código então processa todas as imagens no diretório baixado e classifica cada imagem usando o modelo pré-treinado. O resultado da classificação, que é a classe prevista e a pontuação de confiança, é exibido em cada imagem usando matplotlib.

# Tutorial de uso:

1) `pip3 uninstall PIL`

2) `pip3 uninstall Pillow`

3) `pip3 install --upgrade Pillow`

4) `pip3 install s3scanner`

5) `python3 analisador-bucket-inteligente.py <nome-bucket>`

# Demonstração:

![image](https://user-images.githubusercontent.com/48680041/235518181-678ddfb2-8573-40c7-8532-1d127c7d4a41.png)

![image](https://user-images.githubusercontent.com/48680041/235518070-ddb2daff-d2d4-4e2e-b7af-a303b7fe0e22.png)

# Créditos pelos dataset's:

* https://github.com/ricardobnjunior/Brazilian-Identity-Document-Dataset
* https://www.kaggle.com/datasets/lprdosmil/unsplash-random-images-collection
* https://www.kaggle.com/datasets/starktony45/image-dataset

