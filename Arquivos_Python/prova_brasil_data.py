import pandas as pd

def treatValueINSE(stringValue):
    if stringValue == 'Muito-baixo':
        return 1
    elif stringValue == 'Baixo':
        return 2
    elif stringValue == 'Médio-baixo':
        return 3
    elif stringValue == 'Médio':
        return 4
    elif stringValue == 'Médio-alto':
        return 5
    elif stringValue == 'Alto':
        return 6
    elif stringValue == 'Muito-alto':
        return 7

def main():
    global csvFile

    #PB_5_MAT
    csvFile = pd.read_csv(filepath_or_buffer="prova_brasil_5_mat_2017.csv")

    #Limpar dados inconsistentes
    csvFile = csvFile[csvFile['NSE* (Classe)'] != 'Sem dados*']
    csvFile = csvFile[csvFile['Percentual Proficiente (%)'] != 'Sem dados*']

    #Tratar valor do INSE
    csvFile['NSE* (Classe)'] = csvFile['NSE* (Classe)'].apply(treatValueINSE)

    #EXPORT
    csvFile.to_csv(r'C:\Users\Mateus\Desktop\Tratados\prova_brasil_5_mat_2017.csv', index=None, header=True)

    #-------------------------------------------------------------------------------------------------------

    #PB_5_PT
    csvFile = pd.read_csv(filepath_or_buffer="prova_brasil_5_port_2017.csv")

    #Limpar dados inconsistentes
    csvFile = csvFile[csvFile['NSE* (Classe)'] != 'Sem dados*']
    csvFile = csvFile[csvFile['Percentual Proficiente (%)'] != 'Sem dados*']

    #Tratar valor do INSE
    csvFile['NSE* (Classe)'] = csvFile['NSE* (Classe)'].apply(treatValueINSE)

    #EXPORT
    csvFile.to_csv(r'C:\Users\Mateus\Desktop\Tratados\prova_brasil_5_port_2017.csv', index=None, header=True)

    #-------------------------------------------------------------------------------------------------------

    #PB_9_MAT
    csvFile = pd.read_csv(filepath_or_buffer="prova_brasil_9_mat_2017.csv")

    #Limpar dados inconsistentes
    csvFile = csvFile[csvFile['NSE* (Classe)'] != 'Sem dados*']
    csvFile = csvFile[csvFile['Percentual Proficiente (%)'] != 'Sem dados*']

    #Tratar valor do INSE
    csvFile['NSE* (Classe)'] = csvFile['NSE* (Classe)'].apply(treatValueINSE)

    #EXPORT
    csvFile.to_csv(r'C:\Users\Mateus\Desktop\Tratados\prova_brasil_9_mat_2017.csv', index=None, header=True)

    #-------------------------------------------------------------------------------------------------------

    #PB_9_PT
    csvFile = pd.read_csv(filepath_or_buffer="prova_brasil_9_port_2017.csv")

    #Limpar dados inconsistentes
    csvFile = csvFile[csvFile['NSE* (Classe)'] != 'Sem dados*']
    csvFile = csvFile[csvFile['Percentual Proficiente (%)'] != 'Sem dados*']

    #Tratar valor do INSE
    csvFile['NSE* (Classe)'] = csvFile['NSE* (Classe)'].apply(treatValueINSE)

    #EXPORT
    csvFile.to_csv(r'C:\Users\Mateus\Desktop\Tratados\prova_brasil_9_port_2017.csv', index=None, header=True)

if __name__ == '__main__':
    main()