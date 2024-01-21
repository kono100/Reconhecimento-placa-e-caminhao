# import subprocess

# # Caminho para o script de detecção
# detect_script = "C:\\Users\\User\\Desktop\\FACULDADE\\REGES\\python\\caminhao\\yolov5\\detect.py"

# # Executar a detecção
# subprocess.run([
#     "python", detect_script,
#     "--weights", "C:\\Users\\User\\Desktop\\FACULDADE\\REGES\\python\\caminhao\\yolov5\\yolov5s.pt",
#     "--img", "640",
#     "--conf", "0.25",
#     "--source", " C:\\Users\\User\\Desktop\\FACULDADE\\REGES\\python\\caminhao\\dataset\\foto"
# ])


import subprocess

# Caminho para o script de detecção
detect_script = "C:\\Users\\User\\Desktop\\FACULDADE\\REGES\\python\\caminhao\\yolov5\\detect.py"

# Caminho para o arquivo yolov5s.pt com barras duplas
yolov5s_weights = "C:\\Users\\User\Desktop\\FACULDADE\\REGES\\python\\caminhao\\yolov5\\runs\\train\\exp\\weights\\best.pt"

# Caminho para a pasta contendo as imagens de entrada
source_path = "C:\\Users\\User\\Desktop\\FACULDADE\\REGES\\python\\caminhao\\dataset\\foto"

# Executar a detecção
subprocess.run([
    "python", detect_script,
    "--weights", yolov5s_weights,
    "--img", "640",
    "--conf", "0.25",
    "--source", source_path
])



# ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠

''' 

SÓ RODAR O 3 PARA DETECTAR OS OBJETOS !

'''


# ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠