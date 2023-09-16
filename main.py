import os
from tkinter.filedialog import askdirectory

#Seleciona uma pasta para ser realizado a organização
local = askdirectory(title="Escolha uma pasta")

#Lista os arquivos no local
listaArquivos = os.listdir(local)

#Organiza os arquivos em pasta de acordo com seus tipos
pastas = {
    "Imagens": [".png", ".jpg",".jpeg",".gif",".PNG"],
    "Planilhas": [".xlsx"],
    "PDF" : [".pdf"],
    "Músicas e Vídeos" : [".csv",".mpeg",".mp3",".mp4",".mkv"],
    "Textos": [".txt",".log",".doc",".docx"],
    "Torrents": [".torrent"],
    "Compactados": [".zip",".rar"],
    "Executáveis": [".exe"]
}

#Encontra as extensões e encaminha os arquivos para as pastas corretas
for listaArquivo in listaArquivos:
    nomeArquivo, extensaoArquivo = os.path.splitext(f"{local}/{listaArquivo}")
    for pasta in pastas:
        if extensaoArquivo in pastas[pasta]:
            if not os.path.exists(f"{local}/{pasta}"):
                os.mkdir(f"{local}/{pasta}")
            os.rename(f"{local}/{listaArquivo}" , f"{local}/{pasta}/{listaArquivo}")