import pandas as pd
import requests
import json

def exportCSV(csvFile):
    csvFile.to_csv(r'C:\Users\Mateus\Desktop\Tratados\escola_ponto.csv', index=None, header=True)

def main():
    global csvLinhas

    # Abrir arquivo
    csvLinhas = pd.read_csv(filepath_or_buffer="linha_onibus.csv", sep=',', engine='python')
    jsonFile = '';

    for index, row in csvLinhas.iterrows():
        cod = row['cod_linha']
        response = requests.get("http://transporteservico.urbs.curitiba.pr.gov.br/getPontosLinha.php?linha="+cod+"&c=e6244")

        responseJson = response.json()
        if (len(responseJson) > 0 ):

            for x in range(len(responseJson)):
                responseJson[x]['COD_LINHA'] = cod

            if (index == 0):
                jsonFile = json.dumps(responseJson)
            else:
                res_dict = jsonFile + json.dumps(responseJson)
                jsonFile = res_dict

    f = open("pontos_linhas.json", "a")
    f.write(jsonFile)
    f.close()

if __name__ == '__main__':
    main()