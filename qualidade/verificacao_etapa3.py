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
        #print  'ID SERVICO', '\t', 'name SERVICO', '\t', 'NOME CASO', '\t', 'VALOR'
        print 'id serv.', '\t', 'Nome Servico', '\t',  'QTD Etapa', '\t','QTD title' , '\t', 'QTD Descrição' , '\t',\
            'QTD Documentos', '\t', 'Documentos Excecoes', '\t', 'QTD Canais', '\t', 'QTD Custo' , '\t', 'QTD Description' , '\t', 'Buffer Etapa'
        # print 'Orgao', '\t', 'ID', '\t', 'SERVICO', '\t', 'Quantidade etapas: ', '\t', 'Soma Titulo', '\t', \
        #     'Soma Descricao', '\t', 'Soma Documentos', '\t', \
        #     'Soma Channels', '\t', 'Gratuidade' , '\t', 'Soma Cost', '\t','Description Cost', '\t', 'BUFFER ETAPAS'
        for i in organ:
            url2 = 'http://186.249.51.81/api/v1/organs/' + i['id'] + '.json'
            response2 = urllib.urlopen(url2)
            organDentro = json.loads(response2.read())
            #print u'Orgão: ' + organDentro['name']

            for j in organDentro['service_ids']:
                urlService = 'http://servicos.al.gov.br/api/v1/services/' + j + '.json'
                response3 = urllib.urlopen(urlService)
                oneService = json.loads(response3.read())

                # print oneService['id'], '\t', oneService['name'], '\t', '-', '\t', '-', '\t', '-', '\t', \
                #     '-', '\t', '-', '\t', '-'

                #print oneService['name']
                countEtapa = 0
                somaTitle = 0
                somaDescriprion = 0
                somaDocumentos = 0
                somaCanais = 0
                somaCusto = 0
                somaDescriptionCusto = 0
                somaDocumentosExcecoes = 0
                etapas = []

                # 1 - Verificação do nome do serviço
                if oneService['name'] != '':
                    NomeServico = 1
                else:
                    NomeServico = 0
                acronimo = u'%s' % (organDentro['acronym'])
                if oneService['steps'] != None:
                    for i in oneService['steps']:

                        # try:
                        #     print  oneService['id'], '\t', oneService['name'], '\t', \
                        #     i['documents'][0]['cases'][0]['description'], '\t', 1
                        # except:
                        #     print  oneService['id'], '\t', oneService['name'], '\t', \
                        #         "--------", '\t', 0

                        countEtapa += 1
                        # print oneService['name'], '\t', i['title']
                        # VERIFICAÇÃO TITULO ETAPAS
                        if i['title'] != '':
                            etapas.append('** Et: ')
                            etapas.append(countEtapa)
                            etapas.append('Title')
                            etapas.append(1)
                            somaTitle += 1
                        else:
                            etapas.append('** Et: ')
                            etapas.append(countEtapa)
                            etapas.append('Title')
                            etapas.append(0)
                            somaTitle += 0

                        # VERIFICAÇÃO DESCRIÇÃO ETAPAS
                        if i['description'] != '':
                            etapas.append('** Et: ')
                            etapas.append(countEtapa)
                            etapas.append('Description')
                            etapas.append(1)
                            somaDescriprion += 1
                        else:
                            etapas.append('** Et: ')
                            etapas.append(countEtapa)
                            etapas.append('Description')
                            etapas.append(0)
                            somaDescriprion += 0

                        # VERIFICAÇÃO DOCUMENTOS ETAPAS
                        try:
                            if i['documents'] != None:
                                etapas.append('** Et: ')
                                etapas.append(countEtapa)
                                etapas.append('Documentos')
                                etapas.append(1)
                                somaDocumentos += 1

                                if i['documents'][0]['cases'][0]['description'] != None:
                                    etapas.append('** Et: ')
                                    etapas.append(countEtapa)
                                    etapas.append('ExcecoesDocumentos')
                                    etapas.append(1)
                                    somaDocumentosExcecoes += 1
                                else:
                                    etapas.append('** Et: ')
                                    etapas.append(countEtapa)
                                    etapas.append('ExcecoesDocumentos')
                                    etapas.append(0)
                                    somaDocumentosExcecoes += 0
                            else:
                                etapas.append('** Et: ')
                                etapas.append(countEtapa)
                                etapas.append('Documentos')
                                etapas.append(0)
                                somaDocumentos += 0

                                etapas.append('** Et: ')
                                etapas.append(countEtapa)
                                etapas.append('ExcecoesDocumentos')
                                etapas.append(0)
                                somaDocumentosExcecoes += 0
                        except:
                            etapas.append('** Et: ')
                            etapas.append(countEtapa)
                            etapas.append('Documentos')
                            etapas.append(0)
                            somaDocumentos += 0

                        # VERIFICAÇÃO CANAIS DE PRESTAÇÃO ETAPAS
                        try:
                            etapas.append('** Et: ')
                            etapas.append(countEtapa)
                            etapas.append('Canais')
                            etapas.append(1)
                            somaCanais += 1
                        except:
                            etapas.append('** Et: ')
                            etapas.append(countEtapa)
                            etapas.append('Canais')
                            etapas.append(0)
                            somaCanais += 0

                        # 12 - Verificação de Custo
                        if oneService['free'] != 'true':
                            # 12.1 - Verificação de Custo da Etapa
                            try:
                                StrCusto = str(i['cost']['value'])
                                if StrCusto != '':
                                    # print('Cursto: ' + StrCusto)
                                    etapas.append('** Et: ')
                                    etapas.append(countEtapa)
                                    etapas.append('Custo')
                                    etapas.append(1)
                                    somaCusto += 1

                                else:
                                    etapas.append('** Et: ')
                                    etapas.append(countEtapa)
                                    etapas.append('Custo')
                                    etapas.append(0)
                                    somaCusto += 0

                            except:
                                # print('Não possui curso')
                                etapas.append('** Et: ')
                                etapas.append(countEtapa)
                                etapas.append('Custo')
                                etapas.append(1)
                                somaCusto += 1

                            try:
                                if i['cost']['value'] != '' and i['cost']['description'] != '':
                                    etapas.append('** Et: ')
                                    etapas.append(countEtapa)
                                    etapas.append('Description')
                                    etapas.append(1)
                                    somaDescriptionCusto += 1
                                else:
                                    etapas.append('** Et: ')
                                    etapas.append(countEtapa)
                                    etapas.append('Description')
                                    etapas.append(0)
                                    somaDescriptionCusto += 0
                            except:
                                etapas.append('** Et: ')
                                etapas.append(countEtapa)
                                etapas.append('Description')
                                etapas.append(0)
                                somaDescriptionCusto += 0

                        else:
                            StrCusto = 'deu erro no valor'
                            etapas.append('** Et: ')
                            etapas.append(countEtapa)
                            etapas.append('Custo')
                            etapas.append(1)
                            somaCusto += 1


                    mediaEtapa =  (countEtapa + somaTitle + somaDescriprion + somaDocumentos + somaCanais + somaCusto + somaDescriptionCusto)/7

                    print oneService['id'], '\t', oneService[
                        'name'], '\t', countEtapa, '\t', somaTitle, '\t', somaDescriprion, '\t', somaDocumentos, '\t', somaDocumentosExcecoes, '\t', somaCanais, '\t', somaCusto, '\t', somaDescriptionCusto, '\t', etapas
                else:
                    #continue
                    print oneService['id'], '\t', oneService[
                        'name'], '\t', 0, '\t', 0, '\t', 0, '\t', 0, '\t', 0, '\t' ,0, '\t', 0, '\t', []

#este código está correto

