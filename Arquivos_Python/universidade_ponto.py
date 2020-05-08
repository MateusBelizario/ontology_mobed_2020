import pandas as pd
from math import sin, cos, sqrt, atan2, radians

def exportCSV(csvFile):
    csvFile.to_csv(r'C:\Users\Mateus\Desktop\Tratados\universidade_ponto.csv', index=None, header=True)

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
    csvUniversidade = pd.read_csv(filepath_or_buffer="universidades_curitiba.csv", sep=';', engine='python')
    csvPonto = pd.read_csv(filepath_or_buffer="pontos_curitiba.csv", sep=',', engine='python')

    universidade_id = []
    campus_id = []
    dist = []
    ponto_id = []

    # Calcular a distância entre escola e ponto
    for index, row in csvUniversidade.iterrows():
        id_uni = row['ï»¿CD_EQUI']
        universidade = row['COD_IES']
        lat_a = row['LAT_SIRGAS']
        long_a = row['LON_SIRGAS']

        for index_2, row_2 in csvPonto.iterrows():
            ponto = row_2['NUM']
            lat_b = row_2['LAT']
            long_b = row_2['LON']

            distance = calculateDistance(lat_a, lat_b, long_a, long_b)

            if distance == 'PERTO':
                #Append data to arrays
                universidade_id.append(universidade)
                campus_id.append(id_uni)
                dist.append(distance)
                ponto_id.append(ponto)

    # dictionary of lists
    dict = {'campus': campus_id, 'universidade': universidade_id, 'distancia': dist, 'ponto': ponto_id}
    df = pd.DataFrame(dict)
    # saving the dataframe
    # print(df);
    exportCSV(df)

if __name__ == '__main__':
    main()