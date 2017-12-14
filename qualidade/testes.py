# -*- coding: utf-8 -*-
import urllib, json
import csv

class CompletudeServico():

    def getservicos(self):
        arquivo = open('completudeServicos.csv', 'w')


        url = "http://186.249.51.81/api/v1/organs.json"
        response = urllib.urlopen(url)
        organ = json.loads(response.read())

        for i in organ:

            url2 = 'http://186.249.51.81/api/v1/organs/' + i['id'] + '.json'
            response2 = urllib.urlopen(url2)
            organDentro = json.loads(response2.read())
            #print u'Orgão: ' + organDentro['name']

            for j in organDentro['service_ids']:
                urlService = 'http://servicos.al.gov.br/api/v1/services/' + j + '.json'
                response3 = urllib.urlopen(urlService)
                oneService = json.loads(response3.read())

                try:
                    StrCusto = oneService['steps'][0]['cost']['value']
                    if StrCusto[2] != '':
                        # print('Cursto: ' + StrCusto)
                        Custo = 1
                    else:
                        Custo = 0
                        Gratuidade = 'Possui custos, mas não colocou o valor'
                        # print(Gratuidade)
                except:
                    # print('Não possui curso')
                    StrCusto = 0,0

                print StrCusto