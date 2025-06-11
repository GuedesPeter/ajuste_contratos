import pandas as pd
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
