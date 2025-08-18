import pandas as pd
import os
import glob

# Caminho para leitura dos arquivos
folder_path = 'src\\data\\raw'

# Lista todos os arquivos de Excel
excel_files = glob.glob(os.path.join(folder_path, '*.xlsx'))

if not excel_files:
    print("Nenhum arquivo Excel (.xlsx) encontrado.")
else:
    
    # dataframe = tabela na memória para guardar os conteúdos dos arquivos:
    dfs = []

    for excel_file in excel_files:
        
        try: #Lê todo o conteúdo dos arquivos Excel:
            df_temp = pd.read_excel(excel_file)

            # Lê apenas o nome do arquivo Excel:
            file_name = os.path.basename(excel_file)

            df_temp['filename'] = file_name
            
            # Cria a coluna (Location) de sigla do país do qual os dados se referem (BR: Brasil, FR: França, IT: Itália):
            if 'brasil' in file_name.lower():
                df_temp['Location'] = 'BR'
            elif 'france' in file_name.lower():
                df_temp['Location'] = 'FR'
            elif 'italian' in file_name.lower():
                df_temp['Location'] = 'IT'
            

            # Cria a coluna (Campaign) que extrai o nome da campanha que está sendo mencionada como "link" nos arquivos:
            df_temp['Campaign'] = df_temp['utm_link'].str.extract(r'utm_campaign=(.*)')

            # Guarda dados tratados dentro de uma dataframe comum:
            dfs.append(df_temp)


            # Informa erro na leitura:
        except Exception as e:
            print(f"Erro ao ler o arquivo {excel_file} : {e}")

if dfs:
    # Concatena todas as tabelas salvas no DFS como uma tabela única:
    result = pd.concat(dfs, ignore_index=True)

    # Caminho de saída:    
    output_file = os.path.join('src', 'data', 'ready', 'clean.xlsx')

    # Configuração do motor de escrita:
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')

    # Leva os dados do resultado a serem escritos no motor de Excel configurado:
    result.to_excel(writer, index=False)

    writer._save()
else:
    print("Nenhum dado para ser salvo!")