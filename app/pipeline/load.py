import os  # biblioteca para manipular arquivos e pastas

import pandas as pd


def load_excel(
    data_frame: pd.DataFrame, output_path: str, file_name: str
) -> str:

    """
    receber um dataframe e salvar como excel

    args:
    data_frame (pd.DataFrame): dataframe a ser salvo como excel
    output_path (str): caminho onde o arquivo será salvo
    file_name (str): nome do arquivo a ser salvo

    return: "Arquivo salvo com sucesso"

    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    data_frame.to_excel(f'{output_path}/{file_name}.xlsx', index=False)
    return 'Arquivo salvo com sucesso'
