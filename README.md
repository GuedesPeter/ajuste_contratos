# Remoção de Sufixo Após Sublinhado em Arquivos XLSX e CSV

Este script processa uma coluna específica de um arquivo `.xlsx` ou `.csv`, removendo o sufixo que aparece após um sublinhado (`_`). O arquivo original é atualizado com as modificações.

## Como funciona

1. Lê um arquivo (XLSX ou CSV).
2. Processa a coluna especificada para remover qualquer conteúdo após o primeiro `_`.
3. Salva o arquivo com os dados ajustados.

## Uso

### Dependências

Certifique-se de ter instalado as bibliotecas necessárias antes de executar o script:

```bash
pip install pandas

