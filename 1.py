import subprocess
import sys

# Clonar o repositório YOLOv5
subprocess.run(["git", "clone", "https://github.com/ultralytics/yolov5"])

# Mover para o diretório clonado
sys.path.append("yolov5")
import os
os.chdir("yolov5")

# Instalar as dependências do projeto
subprocess.run(["pip", "install", "-qr", "requirements.txt", "comet_ml"])

# Inicializar as configurações do notebook
import torch
from utils import notebook_init
display = notebook_init()



# ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠

''' 

SÓ RODAR O 1 SE NÃO TIVER O CLONE

'''


# ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠