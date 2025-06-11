
# MODELO VSCODE -----------------------------------------------------------------

import pandas as pd
import os
import platform
import subprocess


arquivo_entrada = 'Pt25.xlsx'
arquivo_saida = 'pt25_sem_duplicatas.xlsx'


df = pd.read_excel(arquivo_entrada)


if 'external_id' not in df.columns:
    raise ValueError("A coluna 'external_id' não foi encontrada no arquivo.")


df_sem_duplicatas = df.drop_duplicates(subset='external_id')


df_sem_duplicatas.to_excel(arquivo_saida, index=False)

print(f"Arquivo salvo com sucesso como: {arquivo_saida}")


caminho_absoluto = os.path.abspath(arquivo_saida)
diretorio = os.path.dirname(caminho_absoluto)


sistema = platform.system()

try:
    if sistema == 'Windows':
        os.startfile(diretorio)
    elif sistema == 'Darwin':  # macOS
        subprocess.run(['open', diretorio])
    else:  # Linux
        subprocess.run(['xdg-open', diretorio])
except Exception as e:
    print(f"Não foi possível abrir o diretório automaticamente: {e}")



# MODELO COLLAB NOTEBOOK ----------------------------------------------------------

'''import pandas as pd
from google.colab import files

arquivo_entrada = '/content/Pt26.xlsx'
arquivo_saida = 'pt26_sem_duplicatas.xlsx'


df = pd.read_excel(arquivo_entrada)

if 'external_id' not in df.columns:
    raise ValueError("A coluna 'external_id' não foi encontrada no arquivo.")


df_sem_duplicatas = df.drop_duplicates(subset='external_id')


df_sem_duplicatas.to_excel(arquivo_saida, index=False)

# Faz o download do arquivo para o usuário
files.download(arquivo_saida)

print(f"Arquivo salvo com sucesso e pronto para download: {arquivo_saida}")
'''
