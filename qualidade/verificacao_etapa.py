# -*- coding: UTF-8 -*-
import urllib, json
import csv

class CompletudeServico():

    def getservicos(self):
        numTituloEtapa = 0
        numDescricaoEtapa = 0
        numGratuidadeEtapa = 0
        numCanaisEtapa = 0
        numDocumentosEtapa = 0


        dictTitleFinal = {}
        dictDescriptionFinal = {}
        dictCustoFinal = {}
        dictCanaisFinal = {}
        dictDocumentosFinal = {}
        #input()
        arquivo = open('verificaEtapa.csv', 'wb')

        url = "http://186.249.51.81/api/v1/organs.json"
        response = urllib.urlopen(url)
        organ = json.loads(response.read())

        # Nível de detalhamento das Informações dos Serviços (IS)
        # print(organ[0])
        try:
            writer = csv.writer(arquivo, delimiter='\t')
            #writer.writerow(('ID ORGAO', 'SIGLA', 'id Serv.', 'NomeServico', 'NomeServico*: ', 'NomesPopulares: ', 'DescricaoServico*: ', 'Gratuidade', 'UnidadeAtendim*: ', 'Tempo: ', 'Outras Informacoes: ', 'Solicitante*: ', 'Categoria*: ', 'Publico Alvo*: ', 'Titulo Etapa*: ', 'Descricao Etapa*: ', 'Custo Etapa: ', 'Canais de Prestacao: ', 'Documentos: ', 'Comentarios Tempo: ', 'Comentarios Custo: ', 'Excecoes de Documentos: ', 'Campos Obrigatorios 8 totais:', 'Campos Opcionais 8 totais: ', 'COMPLETUDE 16 totais:'))
        finally:
            pass

        writer.writerow((
            'ID ORGAO', 'SIGLA', 'Gratuidade',
            'Titulo Etapa*: ', 'Descricao Etapa*: ', 'Custo Etapa: ', 'Canais de Prestacao: ',
            'Documentos: '))
        for i in organ:
            url2 = 'http://186.249.51.81/api/v1/organs/' + i['id'] + '.json'
            response2 = urllib.urlopen(url2)
            organDentro = json.loads(response2.read())
            #print u'Orgão: ' + organDentro['name']

            for j in organDentro['service_ids']:
                urlService = 'http://servicos.al.gov.br/api/v1/services/' + j + '.json'
                response3 = urllib.urlopen(urlService)
                oneService = json.loads(response3.read())

            # INICIO verificação da etapa ----------------------------------------------------------------
                # 9 - Verificação de nome da Etapa
                try:
                    for title in oneService['steps']:
                        numTituloEtapa +=1
                        NometituloEtapa = 'Etapa Titulo ' + numTituloEtapa
                        if title != '':
                            TituloEtapa = 1
                        else:
                            TituloEtapa = 0

                        dictTitle = {NometituloEtapa: TituloEtapa}
                        dictTitleFinal.update(dictTitle)
                except:
                    TituloEtapa = 0
                    dictTitle = {u'Nao tem Etapa TITULO': TituloEtapa}
                    dictTitleFinal.update(dictTitle)

                    # 10 - Verificação de Descrição da Etapa
                try:
                    for description in oneService['steps'][0]['description']:
                        numDescricaoEtapa += 1
                        NomeDescricaoEtapa = 'Etapa Descricao ' + numDescricaoEtapa
                        if description != '':
                            DescricaoEtapa = 1
                            dictDescription = {NomeDescricaoEtapa: DescricaoEtapa}
                            dictDescriptionFinal.update(dictDescription)
                        else:
                            DescricaoEtapa = 0
                            dictDescription = {NomeDescricaoEtapa: DescricaoEtapa}
                            dictDescriptionFinal.update(dictDescription)
                except:
                    DescricaoEtapa = 0
                    dictDescription = {u'Nao tem Etapa DESCRICAO': DescricaoEtapa}
                    dictDescriptionFinal.update(dictDescription)

                # 12 - Verificação de Custo
                if oneService['free'] != 'true':
                    # 12.1 - Verificação de Custo da Etapa
                    try:
                        for gratuidade in oneService['steps'][0]['cost']['value']:
                                numGratuidadeEtapa += 1
                                NomeGratuidadeEtapa = 'Etapa Gratuidade ' + numGratuidadeEtapa
                                if gratuidade != '':
                                    #print('Cursto: ' + StrCusto)
                                    Custo = 1
                                    dictCusto = {NomeGratuidadeEtapa: Custo}
                                    dictCustoFinal.update(dictCusto)
                                else:
                                    Custo = 0
                                    dictCusto = {NomeGratuidadeEtapa: Custo}
                                    dictCustoFinal.update(dictCusto)
                                    Gratuidade = u'Possui custos, mas nao colocou o valor'
                                    #print(Gratuidade)
                    except:
                        #print('Não possui curso')
                        Custo = 0
                        dictCusto = {u'Nao tem Etapa CUSTO': Custo}
                        dictCustoFinal.update(dictCusto)
                else:
                    StrCusto = 'deu erro no valor'
                    Custo = 1
                    dictCusto = {'custo etapa': Custo}
                    dictCustoFinal.update(dictCusto)

                # 13 - Verificação de Canais Prestacao
                try:
                    for canais in oneService['steps'][0]['providing_channels']:
                        numCanaisEtapa += 1
                        NomeCanaisEtapa = 'Etapa Canais ' + numCanaisEtapa
                        if canais != '':
                            CanaisPrestacao = 1
                            dictCanais = {NomeCanaisEtapa: CanaisPrestacao}
                            dictCanaisFinal.update(dictCanais)
                        else:
                            CanaisPrestacao = 0
                            dictCanais = {NomeCanaisEtapa: CanaisPrestacao}
                            dictCanaisFinal.update(dictCanais)
                except:
                    CanaisPrestacao = 0
                    dictCanais = {u'Nao tem Etapa CANAIS': CanaisPrestacao}
                    dictCanaisFinal.update(dictCanais)

                # 14 - Verificação de Documentos
                try:
                    for documentos in oneService['steps'][0]['documents']:
                        numDocumentosEtapa += 1
                        NomeDocumentosEtapa = 'Etapa Documentos ' + numDocumentosEtapa
                        if documentos != '':
                            Documentos = 1
                            dictDocumentos = {NomeCanaisEtapa: Documentos}
                            dictDocumentosFinal.update(dictDocumentos)
                        else:
                            Documentos = 0
                except:
                    Documentos = 0
                    dictDocumentos = {u'Nao tem Etapa DOCUMENTOS': Documentos}
                    dictDocumentosFinal.update(dictDocumentos)

                # INICIO verificação da etapa ----------------------------------------------------------------

                acronimo = u'%s' % (organDentro['acronym'])
                #nomeServico = u'%s' % (oneService['name'])
                try:

                   writer.writerow( (organDentro['id'], acronimo.encode("utf8"), oneService['free'],
                                     dictTitleFinal, dictDescriptionFinal, dictCustoFinal, dictCanaisFinal, dictDocumentosFinal))
                finally:
                    pass