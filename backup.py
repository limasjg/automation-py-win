import shutil
import os

# Obtenha o diretório do perfil do usuário
user_profile = os.environ['USERPROFILE']

# Defina a origin e o destiny do backup
origin = os.path.join(user_profile, "Documents", "pasta1")
destiny = os.path.join(user_profile, "Documents", "pasta2")

# Verifica se o diretório de destiny existe, senão o cria
if not os.path.exists(destiny):
    os.makedirs(destiny)

# Listando origem
files = os.listdir(origin)

# Itera sobre os arquivos dentro da pasta1 e copia-os para a pasta2
for file in files:
    file_origin = os.path.join(origin, file)
    file_destiny = os.path.join(destiny, file)
    shutil.copy2(file_origin, file_destiny)

# Imprima uma mensagem de sucesso
print("Backup criado com sucesso!")

# Para excluir os arquivos
for file in files:
    path_diretory = os.path.join(origin, file)
    os.remove(path_diretory)

print('Arquivos Removidos!')