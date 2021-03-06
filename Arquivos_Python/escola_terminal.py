import pandas as pd
from math import sin, cos, sqrt, atan2, radians

def exportCSV(csvFile):
    csvFile.to_csv(r'C:\Users\Mateus\Desktop\Tratados\escola_terminal.csv', index=None, header=True)

def calculateDistance(lat_a, lat_b, lon_a, lon_b):
    lat_a = str(lat_a).replace(',', '.')
    lat_b = str(lat_b).replace(',', '.')
    lon_a = str(lon_a).replace(',', '.')
    lon_b = str(lon_b).replace(',', '.')

    R = 6373.0
    lat1 = radians(float(lat_a))
    lon1 = radians(float(lon_a))
    lat2 = radians(float(lat_b))
    lon2 = radians(float(lon_b))

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    if distance < 0.25:
        return 'PERTO'
    elif distance < 0.50:
        return 'MEDIO'
    else:
        return 'LONGE'

def main():
    global csvEscola
    global csvPonto

    # Abrir arquivo
    csvEscola = pd.read_csv(filepath_or_buffer="escolas_curitiba.csv", sep=';', engine='python')
    csvTerminal = pd.read_csv(filepath_or_buffer="terminal_de_transporte.csv", sep=',', engine='python')

    escola_id = []
    dist = []
    terminal_id = []

    # Calcular a distância entre escola e ponto
    for index, row in csvEscola.iterrows():
        escola = row['ï»¿CD_EQUI']
        lat_a = row['LAT_SIRGAS']
        long_a = row['LON_SIRGAS']

        for index_2, row_2 in csvTerminal.iterrows():
            terminal = row_2['id']
            lat_b = row_2['lat']
            long_b = row_2['lng']

            distance = calculateDistance(lat_a, lat_b, long_a, long_b)

            if distance == 'PERTO':
                #Append data to arrays
                escola_id.append(escola)
                dist.append(distance)
                terminal_id.append(terminal)

    # dictionary of lists
    dict = {'escola': escola_id, 'distancia': dist, 'terminal': terminal_id}
    df = pd.DataFrame(dict)
    # saving the dataframe
    # print(df);
    exportCSV(df)

if __name__ == '__main__':
    main()