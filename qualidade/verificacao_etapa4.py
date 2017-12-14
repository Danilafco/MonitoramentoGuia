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
        countservices = 0
        etapas = []
        #print  'ID SERVICO', '\t', 'name SERVICO', '\t', 'NOME CASO', '\t', 'VALOR'
        print 'orgao', '\t', 'id serv.', '\t', 'Nome Servico', '\t', '.....', '\t', 'Nota Nome*', '\t', ' Nota  NomesPopulares', '\t', ' Nota DescricaoServico*', '\t', 'Nota UnidadesAtendimento*' '\t', 'Nota Tempo' , '\t', 'typeTempo','\t',  'ComentariosTempo', '\t',  'Nota OutrasInformacoes' , '\t', 'Solicitante', '\t', 'SolicitanteTipo', '\t', 'SolicitanteRequisitos', '\t', 'Nota Categoria', '\t', 'Nota PublicoAlvo', '\t', '.....', '\t', 'QTD Etapa', '\t', 'QTD title', '\t', 'QTD Descrição', '\t', 'QTD Documentos', '\t', 'Documentos Excecoes', '\t', 'QTD Canais', '\t', 'QTD Custo', '\t', 'QTD Description custo', '\t', 'Buffer Etapa'
        # print 'Orgao', '\t', 'ID', '\t', 'SERVICO', '\t', 'Quantidade etapas: ', '\t', 'Soma Titulo', '\t', \
        #     'Soma Descricao', '\t', 'Soma Documentos', '\t', \
        #     'Soma Channels', '\t', 'Gratuidade' , '\t', 'Soma Cost', '\t','Description Cost', '\t', 'BUFFER ETAPAS'
        for i in organ:
            url2 = 'http://servicos.al.gov.br/api/v1/organs/' + i['id'] + '.json'
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
                countservices = countservices+1
                #print oneService['id'] , '\t', oneService['name']
                ComentariosTempo = 0
                Tempo = 0
                typeTempo = 0

                try:
                    if organDentro['acronym'] != "":
                        Sigla = u'%s' % (organDentro['acronym'])
                    else:
                        Sigla = 'Sem sigla'
                except:
                    Sigla = 'Sem sigla'

                try:
                    if oneService['id'] != "":
                        ServicoId = oneService['id']
                    else:
                        ServicoId = 'Sem id'
                except:
                    ServicoId = 'Sem id'

                try:
                    if oneService['name'] != "":
                        ServicoName = u'%s' % (oneService['name'])
                    else:
                        ServicoName = 'Sem name'
                except:
                    ServicoName = 'Sem name'

                # 1 - Verificação do nome do serviço
                try:
                    if oneService['name'] != "":
                        NomeServico = 1
                    else:
                        NomeServico = 0
                except:
                    NomeServico = 0
                    pass

                # Verificação de nomes populares

                try:
                    if oneService['popular_names'][0]['name'] != None or oneService['popular_names'] != None or oneService['popular_names'][0]['name'] != "":
                        NomesPopulares = 1
                    else:
                        NomesPopulares = 0
                except:
                    NomesPopulares = 0
                    pass

                # 3 -  Verificação de descrição de serviços
                try:
                    if oneService['description'] != "" or oneService['description'] != None:
                        DescricaoServico = 1
                    else:
                        DescricaoServico = 0
                except:
                    DescricaoServico = 0
                    pass


                # 4 - Verificação de Unidades de Atendimento
                try:
                    if oneService['unit_ids'] != [] or oneService['unit_ids'] != None:
                        UnidadesAtendimento = 1
                    else:
                        UnidadesAtendimento = 0
                except:
                    UnidadesAtendimento = 0
                    pass

                # 5 - Verificação de Tempo
                try:
                    if oneService['estimated_time'] != "" or oneService['estimated_time'] != [] or oneService['estimated_time'] != None:
                        Tempo = 1
                    else:
                        Tempo = 0
                except:
                    Tempo = 0
                    pass

                try:
                    if oneService['estimated_time']['description'] != "":
                        ComentariosTempo = 1
                    else:
                        ComentariosTempo = 0

                except:
                    ComentariosTempo = 0
                    pass

                try:
                    if oneService['estimated_time']['type'] != "":
                        typeTempo = 1
                    else:
                        typeTempo = 0
                except:
                    typeTempo = 0
                    pass

                # 6 - Verificação de Outras informações
                try:
                    if oneService['other_informations'] != '':
                        OutrasInformacoes = 1
                    else:
                        OutrasInformacoes = 0
                except:
                    OutrasInformacoes = 0
                    pass

                # 7 - Verificação de Solicitante
                try:
                    if oneService['applicants'] != [] or oneService['applicants'] != None:
                        Solicitante = 1
                        if oneService['applicants'][0]['type'] != '':
                            SolicitanteTipo = 1
                        else:
                            SolicitanteTipo = 0

                        if oneService['applicants'][0]['requirements'] != '':
                            SolicitanteRequisitos = 1
                        else:
                            SolicitanteRequisitos = 0
                    else:
                        Solicitante = 0
                except:
                    Solicitante = 0
                    pass

                # 8 - Verificação de Categoria
                try:
                    if oneService['categories'][0]['id'] != "" or  oneService['categories'] != [] or oneService['categories'] != None:
                        Categoria = 1
                    else:
                        Categoria = 0
                except:
                    Categoria = 0
                    pass



                # 9 - Verificação de público Alvo
                try:
                    if oneService['audiences'][0]['id'] != '' or oneService['audiences'] != None or oneService['audiences'] != [] or oneService['audiences'] != "":
                        PublicoAlvo = 1
                    else:
                        PublicoAlvo = 0
                except:

                    PublicoAlvo = 0
                    pass

                ##### VERIFICAÇÃO DAS ETAPAS
                try:
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
                except:
                    pass
                    #FIM DA VERIFICAÇÃO DAS ETAPAS

                    mediaEtapa =  (countEtapa + somaTitle + somaDescriprion + somaDocumentos + somaCanais + somaCusto + somaDescriptionCusto)/7

                    print Sigla,'\t', ServicoId, '\t', ServicoName,'\t', '.....', '\t', NomeServico,'\t', NomesPopulares, '\t', DescricaoServico, '\t', UnidadesAtendimento, '\t', Tempo, '\t', typeTempo, '\t', ComentariosTempo, '\t', OutrasInformacoes, '\t', Solicitante, '\t', SolicitanteTipo, '\t', SolicitanteRequisitos, '\t', Categoria, '\t', PublicoAlvo, '\t',  '.....', '\t', countEtapa, '\t', somaTitle, '\t', somaDescriprion, '\t', somaDocumentos, '\t', somaDocumentosExcecoes, '\t', somaCanais, '\t', somaCusto, '\t', somaDescriptionCusto, '\t', etapas
                else:
                    #continue
                    print Sigla,'\t', ServicoId, '\t', ServicoName, '\t', '.....','\t', NomeServico,'\t', NomesPopulares, '\t', DescricaoServico, '\t', UnidadesAtendimento, '\t', Tempo, '\t', typeTempo, '\t', ComentariosTempo, '\t', OutrasInformacoes, '\t', Solicitante, '\t', SolicitanteTipo, '\t', SolicitanteRequisitos, '\t', Categoria, '\t', PublicoAlvo, '\t', '.....', '\t', 0, '\t', 0, '\t', 0, '\t', 0, '\t', 0, '\t' ,0, '\t', 0, '\t', 0, '\t', []

        print countservices
