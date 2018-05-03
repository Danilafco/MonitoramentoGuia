# -*- coding: UTF-8 -*-
import urllib, json
import csv

class CompletudeServico():

    def getservicos(self):

        url = "http://186.249.51.81/api/v1/organs.json"
        response = urllib.urlopen(url)
        organ = json.loads(response.read())

        countEtapa = 0
        somaTitle = 0
        somaDescriprion = 0
        somaDocumentos = 0
        somaTypeChannel = 0
        descriptionCusto = 0
        somaCost = 0

        etapas = []
        print 'Orgao', '\t', 'ID', '\t', 'SERVICO', '\t', 'Quantidade etapas: ', '\t', 'Soma Titulo', '\t', \
            'Soma Descricao', '\t', 'Soma Documentos', '\t', \
            'Soma Channels', '\t', 'Gratuidade' , '\t', 'Soma Cost', '\t','Description Cost', '\t', 'BUFFER ETAPAS'
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
                    for i in oneService["steps"]:
                        countEtapa += 1
                        # VERIFICAÇÃO TITULO ETAPAS
                        if i['title'] != '':
                            title = 1
                            etapas.append('Etapa: ')
                            etapas.append(countEtapa)
                            etapas.append('Title')
                            etapas.append(title)
                            somaTitle += title

                        else:
                            title = 0
                            etapas.append('Etapa: ')
                            etapas.append(countEtapa)
                            etapas.append('Title')
                            etapas.append(title)
                            somaTitle += title

                        # VERIFICAÇÃO DESCRIÇÃO ETAPAS
                        if i['description'] != '':
                            description = 1
                            etapas.append('Etapa: ')
                            etapas.append(countEtapa)
                            etapas.append('Description')
                            etapas.append(description)
                            somaDescriprion += description
                        else:
                            description = 0
                            etapas.append('Etapa: ')
                            etapas.append(countEtapa)
                            etapas.append('Description')
                            etapas.append(description)
                            somaDescriprion += description
                        #try:
                         #   print '-----------------------------  try 1'
                            # VERIFICAÇÃO DOCUMENTOS ETAPAS
                        for n in i["documents"]:
                         #   print '-----------------------------  try 2', j
                            if n['name'] != '':
                             #   print '-----------------------------  try 3', j
                                documents = 1
                                etapas.append('Etapa: ')
                                etapas.append(countEtapa)
                                etapas.append('Documents')
                                etapas.append(documents)
                                somaDocumentos += documents
                            else:
                              #  print '-----------------------------  try 4'
                                documents = 0
                                etapas.append('Etapa: ')
                                etapas.append(countEtapa)
                                etapas.append('Documents')
                                etapas.append(documents)
                                somaDocumentos += documents
                       # except Exception as e:
                           #print e
                         #   pass
                             #   print '-----------------------------  try 5'
                             #    etapas.append('Etapa: ')
                             #    etapas.append(countEtapa)
                             #    etapas.append('Documents')
                             #    etapas.append(documents)
                        #try:
                        for p in i["providing_channels"]:
                         #   print '-----------------------------  try 2', j
                            if p['type'] != '':
                             #   print '-----------------------------  try 3', j
                                typeChannel = 1
                                etapas.append('Etapa: ')
                                etapas.append(countEtapa)
                                etapas.append('Type Channel')
                                etapas.append(typeChannel)
                                somaTypeChannel += typeChannel
                            else:
                              #  print '-----------------------------  try 4'
                              typeChannel = 0
                              etapas.append('Etapa: ')
                              etapas.append(countEtapa)
                              etapas.append('Type Channel')
                              etapas.append(typeChannel)
                              somaTypeChannel += typeChannel
                   # except Exception as e:
                        # print e
                     #   pass

                        #try:
                        if oneService['free'] == True:
                            if i["cost"]["value"] != '':
                                cost = 1
                                etapas.append('Etapa: ')
                                etapas.append(countEtapa)
                                etapas.append('Cost')
                                etapas.append(typeChannel)
                                somaCost = cost
                            else:
                              #  print '-----------------------------  try 4'
                              cost = 0
                              etapas.append('Etapa: ')
                              etapas.append(countEtapa)
                              etapas.append('Cost')
                              etapas.append(typeChannel)
                              somaCost = cost
                            # Descrição do custo
                            if i["cost"]["description"] != '':
                                descriptionCusto = 1
                                etapas.append('Etapa: ')
                                etapas.append(countEtapa)
                                etapas.append('Cost description')
                                etapas.append(descriptionCusto)
                               # somaCost = description
                            else:
                              #  print '-----------------------------  try 4'
                              descriptionCusto = 0
                              etapas.append('Etapa: ')
                              etapas.append(countEtapa)
                              etapas.append('Cost description')
                              etapas.append(descriptionCusto)
                              #somaCost = description
                        else:
                            cost = 1
                            etapas.append('Etapa: ')
                            etapas.append(countEtapa)
                            etapas.append('Cost')
                            etapas.append(typeChannel)
                            somaCost = cost
                        # except Exception as e:
                        #     # print e
                        #     pass

                except Exception as e:
                   # print e
                    continue

                print organDentro['acronym'], '\t', oneService['id'], '\t', oneService['name'], '\t', \
                    countEtapa, '\t', somaTitle, '\t', \
                    somaDescriprion, '\t', somaDocumentos, '\t', \
                    somaTypeChannel, '\t', oneService['free'] , '\t',somaCost, '\t', descriptionCusto , '\t',  etapas

                #print 'QTD Etapas' + countEtapa +

                #print etapas

                countEtapa = 0
                somaDescriprion = 0
                somaTitle = 0
                somaDocumentos = 0
                somaTypeChannel = 0
                somaCost = 0
                etapas = []
                etapas = []
