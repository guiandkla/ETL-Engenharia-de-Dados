# Github:

https://www.github.com/guiandkla

# O que foi usado:
Python, Pandas e Pypi.

# Criação da Venv:

Venv -> Virtual Enviroment (ambiente virtual).
python -m venv venv (criar ambiente virtual).
venv/Scripts/activate (ativar o ambiente virtual).

### Etapas dos dados:

Data RAW -> São os dados antes de qualquer processamento ou polimento. São os dados em sua forma mais "crua".
Data Ready -> São os dados que foram passados pelos processos de refinamento.

### Pacotes utilizados

pip install pandas | pip install openpyxl | pip install xlsxwriter

### Regras de tratamento de dados:

1º Prezar pela confiabilidade e rastreabilidade dos dados;

### ETL:

EXTRACT - Extrair os dados. São dos dados (Data Raw = Não tratados, dados brutos), que são extraídos de arquivos (Excel, CSV, TXT, JSON etc.), ou APIs, sistemas legados ou bancos de dados.

TRANSFORM - Transformar os dados (processamento e limpeza). Isso pode incluir padronização, tratamento de valores nulos, conversão de tipos, junção de tabelas, normalização ou aplicação de regras de negócio. Normalmente, é feito com scripts ou ferramentas específicas.

LOAD - Carregar os dados. Os dados transformados são armazenados no destino final, que pode ser um banco de dados (SQL, NoSQL), um data warehouse, um data lake ou até mesmo novos arquivos (CSV, Excel, Parquet etc.).