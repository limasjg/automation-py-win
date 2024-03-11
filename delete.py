import os

# Obtenha o diretório do perfil do usuário
user_profile = os.environ['USERPROFILE']

# Defina o diretório de exclusão
origin = os.path.join(user_profile, "Documents", "pasta1")

# Listando origem
files = os.listdir(origin)

# Para excluir os arquivos
for file in files:
    path_diretory = os.path.join(origin, file)
    os.remove(path_diretory)

print('Arquivos Removidos!')