# Gerador de QR Code

Este projeto é um gerador de QR Code simples com **interface gráfica** em Python usando a API do [goQR.me](https://goqr.me/api/).

Foram usadas as seguintes bibliotecas: tkinter, requests, pillow e io

## Como usar

1. Instale as dependências listadas em `requirements.txt`.
2. Execute o arquivo `gerador_qrcode.py` para abrir um programa que gera QR Code.

### Ou, opcionalmente

1. Baixe a versão para **Windows** ou **Linux** em **Releases**.

## Requisitos

- Python 3.8 ou maior
- As bibliotecas listadas em `requirements.txt`


## Funções do programa
Caixa de texto para inserir o link. Se o link estiver na área de transferência, o programa identificará automaticamente no momento que o usuário clicar na caixa de texto.  
Há um botão que gera o QR Code a partir do link na caixa de texto.  
É possível clicar com o botão direito na imagem do QR Code gerada para salvá-la no dispositivo.
## Como instalar os requisitos

Isso só vale se você for usar o script (gerador_qrcode.py)

### Windows

#### Caso você tenha o pip na variável PATH

`pip install -r requirements.txt`

#### Caso você não tenha o pip na variável PATH

`python -m pip install -r requirements.txt`

### Linux

`sudo apt install python3-tk`

#### Dentro do ambiente do virtual
`pip install -r requirements.ext`




Sinta-se à vontade para contribuir ou abrir issues!
