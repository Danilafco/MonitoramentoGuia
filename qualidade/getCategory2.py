# -*- coding: UTF-8 -*-
import urllib, json
import csv

class CompletudeServico():

    def getservicos(self):
        countServices = 0
        countOrgaos = 0
        url = "http://servicos.al.gov.br/api/v1/organs.json"
        response = urllib.urlopen(url)
        organ = json.loads(response.read())

        try:

            print 'ORGAO', '\t' ,'ServicoId', '\t' , 'ServicoName', '\t' , 'Categoria'

        finally:
            pass

        for i in organ:
            countOrgaos += 1

            url2 = 'http://servicos.al.gov.br/api/v1/organs/' + i['id'] + '.json'
            response2 = urllib.urlopen(url2)
            organDentro = json.loads(response2.read())

            for j in organDentro['service_ids']:
                urlService = 'http://servicos.al.gov.br/api/v1/services/' + j + '.json'
                response3 = urllib.urlopen(urlService)
                oneService = json.loads(response3.read())

                if oneService['active'] == True:
                    countServices += 1

                    try:
                        if organDentro['acronym'] != "":
                            Sigla = u'%s' % (organDentro['acronym'])
                        else:
                            Sigla = 'Sem sigla'
                    except Exception as e:
                        print(e)
                        Sigla = 'Sem sigla'

                    try:
                        if oneService['id'] != "":
                            ServicoId = oneService['id']
                        else:
                            ServicoId = 'Sem id'
                    except  Exception as e:
                        print(e)
                        ServicoId = 'Sem id'

                    try:
                        if oneService['name'] != "":
                            ServicoName = u'%s' % (oneService['name'])
                        else:
                            ServicoName = 'Sem name'
                    except  Exception as e:
                        print(e)
                        ServicoName = 'Sem name'

                    try:
                        for cat in oneService['categories']:
                            if cat['name'] != '':
                                Categoria = 1
                                CategoriaNome = cat['name']
                                print Sigla, '\t', ServicoId, '\t', ServicoName, '\t', CategoriaNome

                            else:
                                Categoria = 0
                                CategoriaNome = 'Não tem categoria'
                                print Sigla, '\t', ServicoId, '\t', ServicoName, '\t', CategoriaNome
                    except:
                        Categoria = 0
                        # print Sigla, '\t', ServicoId, '\t', ServicoName, '\t', CategoriaNome
                else:
                    pass




      #  print 'Orgãos' , countOrgaos
       # print 'Serviços' ,countServices

        # countServices = 0
        # countOrgaos = 0

