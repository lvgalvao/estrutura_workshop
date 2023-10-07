"""esse é o módulo de extração de dados."""

import glob  # biblioteca para listar arquivos
import os  # biblioteca para manipular arquivos e pastas
from typing import List

import pandas as pd


def extract_from_excel(path: str) -> List[pd.DataFrame]:
    """
    função para ler os arquivos de
    uma pasta data/input e retornar uma lista de dataframes

    args: input_path (str): caminho da pasta com os arquivos

    return: lista de dataframes
    """
    all_files = glob.glob(os.path.join(path, '*.xlsx'))

    data_frame_list = []
    for file in all_files:
        data = pd.read_excel(file)
        data_frame_list.append(data)

    return data_frame_list


if __name__ == '__main__':
    data_frame_list = extract_from_excel('data/input')
    print(data_frame_list)
