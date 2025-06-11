import pandas as pd

arquivo_entrada = '/content/Pt5.xlsx'
arquivo_saida = 'pt_sem_duplicatas.xlsx'

df = pd.read_excel(arquivo_entrada)

if 'external_id' not in df.columns:
    raise ValueError("A coluna 'external_id' não foi encontrada no arquivo.")


df_sem_duplicatas = df.drop_duplicates(subset='external_id')
df_sem_duplicatas.to_excel(arquivo_saida, index=False)

print(f"Arquivo salvo com sucesso como: {arquivo_saida}")
