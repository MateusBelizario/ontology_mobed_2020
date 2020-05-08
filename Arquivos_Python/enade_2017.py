import pandas as pd
import numpy as np
import math

def exportCSV(csvFile):
    csvFile.to_csv(r'C:\Users\Mateus\Desktop\Tratados\enade_2017.csv', index=None, header=True)

def main():
    global csvEnade
    global csvPonto

    # Abrir arquivo
    csvEnade = pd.read_csv(filepath_or_buffer="enade_2017.CSV", sep=';', engine='python')

    # Valores iniciais da tabela
    ult_curso = 849
    ult_uni = 10

    media_nota = float(0)
    qt_linhas = float(1)

    nu_ano = []
    co_ies = []
    co_curso = []
    nt_geral = []

    for index, row in csvEnade.iterrows():
        ies = row['CO_IES']
        curso = row['CO_CURSO']
        nota = row['NT_GER']

        if ies != ult_uni or curso != ult_curso:
            nu_ano.append(2017)
            co_ies.append(ult_uni)
            co_curso.append(ult_curso)
            nt_geral.append(float(media_nota)/float(qt_linhas))

            ult_curso = curso
            ult_uni = ies

            nota = str(nota).replace(',', '.')
            if nota != 'nan':
                if not math.isnan(float(nota)):
                    media_nota = float(nota)
                    qt_linhas = 1
                else:
                    media_nota = float(0)
                    qt_linhas = 1
        else:
            nota = str(nota).replace(',', '.')
            if nota != 'nan':
                if not math.isnan(float(nota)):
                    media_nota += float(nota)
                    qt_linhas += 1

    # dictionary of lists
    dict = {'ano': nu_ano, 'cod_ies': co_ies, 'co_curso': co_curso, 'nt_geral': nt_geral}
    df = pd.DataFrame(dict)

    # saving the dataframe
    # print(df);
    exportCSV(df)

if __name__ == '__main__':
    main()