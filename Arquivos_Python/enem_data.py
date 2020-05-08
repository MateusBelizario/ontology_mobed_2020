import pandas as pd

def treatValueINSE(stringValue):
    return stringValue[6]

def main():
    global csvFile

    #Abrir arquivo
    csvFile = pd.read_csv(filepath_or_buffer="enem_2005_2015.csv", sep=';', engine='python')

    #Tirar linhas com INSE null
    csvFile = csvFile[pd.notnull(csvFile['INSE'])]

    #Filtrar por ano
    csvFile = csvFile[csvFile['NU_ANO'] == 2015]

    #Tratar valor do INSE
    csvFile['INSE'] = csvFile['INSE'].apply(treatValueINSE)

    #EXPORT
    csvFile.to_csv(r'C:\Users\Mateus\Desktop\Tratados\enem_2005_2015.csv', index=None, header=True)

if __name__ == '__main__':
    main()