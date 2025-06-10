import pandas as pd
import os

def remover_sufixo_apos_sublinhado(texto):
    if isinstance(texto, str) and '_' in texto:
        indice_sublinhado = texto.find('_')
        return texto[:indice_sublinhado]
    else:
        return texto

def processar_e_salvar_no_mesmo_arquivo(caminho_arquivo, nome_coluna_para_processar):
    if not os.path.exists(caminho_arquivo):
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return

    try:
        if caminho_arquivo.lower().endswith('.xlsx'):
            df = pd.read_excel(caminho_arquivo)
            tipo_arquivo = 'xlsx'
        elif caminho_arquivo.lower().endswith('.csv'):
            df = pd.read_csv(caminho_arquivo)
            tipo_arquivo = 'csv'
        else:
            print(f"Erro: Tipo de arquivo não suportado.")
            return

        if nome_coluna_para_processar not in df.columns:
            print(f"Erro: Coluna '{nome_coluna_para_processar}' não encontrada.")
            return

        df[nome_coluna_para_processar] = df[nome_coluna_para_processar].apply(remover_sufixo_apos_sublinhado)

        if tipo_arquivo == 'xlsx':
            df.to_excel(caminho_arquivo, index=False)
        elif tipo_arquivo == 'csv':
            df.to_csv(caminho_arquivo, index=False, encoding='utf-8')

        print(f"Processamento concluído! O arquivo '{caminho_arquivo}' foi atualizado.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    caminho_do_seu_arquivo = '/content/Pt28.xlsx'
    nome_da_coluna = 'external_id'

    processar_e_salvar_no_mesmo_arquivo(caminho_do_seu_arquivo, nome_da_coluna)

    try:
        if caminho_do_seu_arquivo.lower().endswith('.xlsx'):
            df_verificacao = pd.read_excel(caminho_do_seu_arquivo)
        elif caminho_do_seu_arquivo.lower().endswith('.csv'):
            df_verificacao = pd.read_csv(caminho_do_seu_arquivo)
        else:
            df_verificacao = None

        if df_verificacao is not None:
            print(df_verificacao.head())
    except Exception as e:
        print(f"Não foi possível ler o arquivo: {e}")
