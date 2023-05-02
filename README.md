# Analisador bucket inteligente

Esta ferramenta foi projetada para automatizar o processo de identificação de documentos sensiveis em buckets da AWS S3. Aproveitando o poder da técnica de transfer learning, a ferramenta realiza o download do bucket S3 escolhido, processa as imagens, prevê a classe do documento e fornece uma pontuação de confiança para cada previsão. 

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

