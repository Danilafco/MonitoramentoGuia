# -*- coding: utf-8 -*-
import urllib, json
import csv

from decimal import Decimal


class CompletudeServico():

    def getservicos(self):

        arquivo = open('completudeServicos.csv', 'wb')

        url = "http://servicos.al.gov.br/api/v1/organs.json"
        response = urllib.urlopen(url)
        organ = json.loads(response.read())

        try:
            writer = csv.writer(arquivo, delimiter='\t')
            writer.writerow(('Orgao', 'ID serv.', u'Nome Serviço'.encode('utf8'), 'QTDO_brigatorio',  'QTD_opcionais',  'Percentual_Obrigatorio',  'Percentual_Opcionais' ,   u'Nota do serviço'.encode('utf8'),
                             'Status', 'Atualizador', u'Data Modificação'.encode('utf8'), u'Data Criação'.encode('utf8'),

                             u'Nota - Nome do Serviço*'.encode('utf8'), u'Nota - Descrição do Serviço*'.encode('utf8'), 'Nota - Unidades de Atendimento*',
                             'Nota - Solicitante*', 'Nota - Categoria*', 'Nota - Publico Alvo*', 'Nota - Maturidade*' , u'Nota - Título da Etapa*'.encode('utf8'),
                             u'Nota - Descrição da Etapa*'.encode('utf8'),

                             'Nota - Nomes Populares', 'Nota - Tempo Estimado', 'Nota - Comentarios do Tempo', 'Nota - Gratuidade',
                             u'Nota - Outras Informaçoes'.encode('utf8'), 'Nota - Documentos', u'Nota - Exceções de Documentos'.encode('utf8'), 'Nota - Canais',
                             'Nota - Valor Custo', u'Nota - Descrição do Custo'.encode('utf8')

                             ))

            print 'Orgao', '\t', 'ID serv.', '\t', u'Nome Serviço'.encode('utf8'), '\t', 'QTDO_brigatorio', '\t','QTD_opcionais','\t', 'Percentual_Obrigatorio', '\t','Percentual_Opcionais','\t', u'Nota do serviço'.encode('utf8'),'\t','Status', '\t','Atualizador', '\t',u'Data Modificação'.encode('utf8'),'\t',u'Data Criação'.encode('utf8'), '\t', u'Nota - Nome do Serviço*'.encode('utf8'),'\t', u'Nota - Descrição do Serviço*'.encode('utf8'),'\t','Nota - Unidades de Atendimento*','\t','Nota - Solicitante*', '\t','Nota - Categoria*', '\t','Nota - Publico Alvo*','\t', 'Nota - Maturidade*','\t',u'Nota - Título da Etapa*'.encode('utf8'),'\t',u'Nota - Descrição da Etapa*'.encode('utf8'),'\t','Nota - Nomes Populares', '\t','Nota - Tempo Estimado', '\t','Nota - Comentarios do Tempo','\t','Nota - Gratuidade','\t',u'Nota - Outras Informaçoes'.encode('utf8'), '\t','Nota - Documentos','\t',u'Nota - Exceções de Documentos'.encode('utf8'), '\t','Nota - Canais','\t','Nota - Valor Custo', '\t',u'Nota - Descrição do Custo'.encode('utf8')



        finally:
            pass

        countservices = 0.0



        for i in organ:
            url2 = 'http://servicos.al.gov.br/api/v1/organs/' + i['id'] + '.json'
            response2 = urllib.urlopen(url2)
            organDentro = json.loads(response2.read())

            for j in organDentro['service_ids']:
                urlService = 'http://servicos.al.gov.br/api/v1/services/' + j + '.json'
                response3 = urllib.urlopen(urlService)
                oneService = json.loads(response3.read())


                countEtapa = 0.0
                somaTitle = 0.0
                somaDescriprion = 0.0
                somaDocumentos = 0.0
                somaCanais = 0.0
                somaCusto = 0.0
                somaDescriptionCusto = 0.0
                somaDocumentosExcecoes = 0.0

                countEtapa1 = 0.0
                somaTitle1 = 0.0
                somaDescriprion1 = 0.0
                somaDocumentos1 = 0.0
                somaCanais1 = 0.0
                somaCusto1 = 0.0
                somaDocumentosExcecoes1 = 0.0

                QTDO_brigatorio = 0.0
                QTD_opcionais = 0.0
                Percentual_Obrigatorio = 0.0
                Percentual_Opcionais = 0.0
                CompletudeTotal = 0.0


                etapas = []
                countservices = countservices+1.0
                #print oneService['id'] , '\t', oneService['name']
                ComentariosTempo = 0.0
                Tempo = 0.0
                typeTempo = 0.0

                try:
                    if oneService['maturity_level'] != "" or  oneService['maturity_level'] != None:
                        maturidade = 1.0
                    else:
                        maturidade = 0.0
                except:
                    maturidade = 0.0

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
                        NomeServico = 1.0
                    else:
                        NomeServico = 0.0
                except:
                    NomeServico = 0.0
                    pass

                # Verificação de nomes populares

                try:
                    if oneService['popular_names'][0]['name'] != None or oneService['popular_names'] != None or oneService['popular_names'][0]['name'] != "":
                        NomesPopulares = 1.0
                    else:
                        NomesPopulares = 0.0
                except:
                    NomesPopulares = 0.0
                    pass

                # 3 -  Verificação de descrição de serviços
                try:
                    if oneService['description'] != "" or oneService['description'] != None:
                        DescricaoServico = 1.0
                    else:
                        DescricaoServico = 0.0
                except:
                    DescricaoServico = 0.0
                    pass


                # 4 - Verificação de Unidades de Atendimento
                try:
                    if oneService['unit_ids'] != [] or oneService['unit_ids'] != None:
                        UnidadesAtendimento = 1.0
                    else:
                        UnidadesAtendimento = 0.0
                except:
                    UnidadesAtendimento = 0.0
                    pass

                # 5 - Verificação de Tempo
                try:
                    if oneService['estimated_time'] != "" or oneService['estimated_time'] != [] or oneService['estimated_time'] != None:
                        Tempo = 1.0
                    else:
                        Tempo = 0.0
                except:
                    Tempo = 0.0
                    pass

                try:
                    if oneService['estimated_time']['description'] != "":
                        ComentariosTempo = 1.0
                    else:
                        ComentariosTempo = 0.0

                except:
                    ComentariosTempo = 0.0
                    pass

                try:
                    if oneService['estimated_time']['type'] != "":
                        typeTempo = 1.0
                    else:
                        typeTempo = 0.0
                except:
                    typeTempo = 0.0
                    pass

                # 6 - Verificação de Outras informações
                try:
                    if oneService['other_informations'] != '':
                        OutrasInformacoes = 1.0
                    else:
                        OutrasInformacoes = 0.0
                except:
                    OutrasInformacoes = 0.0
                    pass

                # 7 - Verificação de Solicitante
                try:
                    if oneService['applicants'] != [] or oneService['applicants'] != None:
                        Solicitante = 1.0
                        if oneService['applicants'][0]['type'] != '':
                            SolicitanteTipo = 1.0
                        else:
                            SolicitanteTipo = 0.0

                        if oneService['applicants'][0]['requirements'] != '':
                            SolicitanteRequisitos = 1.0
                        else:
                            SolicitanteRequisitos = 0.0
                    else:
                        Solicitante = 0.0
                        SolicitanteTipo = 0.0
                except:
                    Solicitante = 0.0
                    SolicitanteTipo = 0.0
                    SolicitanteRequisitos = 0.0
                    pass

                # 8 - Verificação de Categoria
                try:
                    if oneService['categories'][0]['id'] != "" or  oneService['categories'] != [] or oneService['categories'] != None:
                        Categoria = 1.0
                    else:
                        Categoria = 0.0
                except:
                    Categoria = 0.0
                    pass



                # 9 - Verificação de público Alvo
                try:
                    if oneService['audiences'][0]['id'] != '' or oneService['audiences'] != None or oneService['audiences'] != [] or oneService['audiences'] != "":
                        PublicoAlvo = 1.0
                    else:
                        PublicoAlvo = 0.0
                except:

                    PublicoAlvo = 0.0
                    pass

                ##### VERIFICAÇÃO DAS ETAPAS

                if oneService['steps'] != None:
                    for i in oneService['steps']:

                        # try:
                        #     print  oneService['id'], '\t', oneService['name'], '\t', \
                        #     i['documents'][0]['cases'][0]['description'], '\t', 1
                        # except:
                        #     print  oneService['id'], '\t', oneService['name'], '\t', \
                        #         "--------", '\t', 0

                        countEtapa += 1.0
                        # print oneService['name'], '\t', i['title']

                        # VERIFICAÇÃO TITULO ETAPAS
                        if i['title'] != '':
                            etapas.append('** Et: ')
                            etapas.append(countEtapa)
                            etapas.append('Title')
                            etapas.append(1.0)
                            somaTitle += 1.0
                        else:
                            etapas.append('** Et: ')
                            etapas.append(countEtapa)
                            etapas.append('Title')
                            etapas.append(0.0)
                            somaTitle += 0.0

                        # VERIFICAÇÃO DESCRIÇÃO ETAPAS
                        if i['description'] != '':
                            etapas.append('** Et: ')
                            etapas.append(countEtapa)
                            etapas.append('Description')
                            etapas.append(1.0)
                            somaDescriprion += 1.0
                        else:
                            etapas.append('** Et: ')
                            etapas.append(countEtapa)
                            etapas.append('Description')
                            etapas.append(0.0)
                            somaDescriprion += 0.0

                        # VERIFICAÇÃO DOCUMENTOS ETAPAS
                        try:
                            if i['documents'] != None:
                                etapas.append('** Et: ')
                                etapas.append(countEtapa)
                                etapas.append('Documentos')
                                etapas.append(1.0)
                                somaDocumentos += 1.0

                                if i['documents'][0]['cases'][0]['description'] != None:
                                    etapas.append('** Et: ')
                                    etapas.append(countEtapa)
                                    etapas.append('ExcecoesDocumentos')
                                    etapas.append(1.0)
                                    somaDocumentosExcecoes += 1.0
                                else:
                                    etapas.append('** Et: ')
                                    etapas.append(countEtapa)
                                    etapas.append('ExcecoesDocumentos')
                                    etapas.append(0.0)
                                    somaDocumentosExcecoes += 0.0
                            else:
                                etapas.append('** Et: ')
                                etapas.append(countEtapa)
                                etapas.append('Documentos')
                                etapas.append(0.0)
                                somaDocumentos += 0.0

                                etapas.append('** Et: ')
                                etapas.append(countEtapa)
                                etapas.append('ExcecoesDocumentos')
                                etapas.append(0.0)
                                somaDocumentosExcecoes += 0.0
                        except:

                            etapas.append('** Et: ')
                            etapas.append(countEtapa)
                            etapas.append('Documentos')
                            etapas.append(0.0)
                            somaDocumentos += 0.0

                        # VERIFICAÇÃO CANAIS DE PRESTAÇÃO ETAPAS
                        try:
                            etapas.append('** Et: ')
                            etapas.append(countEtapa)
                            etapas.append('Canais')
                            etapas.append(1.0)
                            somaCanais += 1.0
                        except:

                            etapas.append('** Et: ')
                            etapas.append(countEtapa)
                            etapas.append('Canais')
                            etapas.append(0.0)
                            somaCanais += 0.0

                        # 12 - Verificação de Custo
                        if oneService['free'] == True :
                            # 12.1 - Verificação de Custo da Etapa
                            try:
                                StrCusto = str(i['cost']['value'])
                                if StrCusto != '':
                                    # print('Cursto: ' + StrCusto)
                                    etapas.append('** Et: ')
                                    etapas.append(countEtapa)
                                    etapas.append('Custo')
                                    etapas.append(1.0)
                                    somaCusto += 1.0


                                else:
                                    etapas.append('** Et: ')
                                    etapas.append(countEtapa)
                                    etapas.append('Custo')
                                    etapas.append(0.0)
                                    somaCusto += 0.0

                            except:

                                # print('Não possui curso')
                                etapas.append('** Et: ')
                                etapas.append(countEtapa)
                                etapas.append('Custo')
                                etapas.append(1.0)
                                somaCusto += 1.0
                                gratuidade = 1.0
                                continue

                            try:
                                if i['cost']['description'] != "":
                                    etapas.append('** Et: ')
                                    etapas.append(countEtapa)
                                    etapas.append('Description')
                                    etapas.append(1.0)
                                    somaDescriptionCusto = 1.0
                                    gratuidade = 1.0

                                else:
                                    etapas.append('** Et: ')
                                    etapas.append(countEtapa)
                                    etapas.append('Description')
                                    etapas.append(0.0)
                                    somaDescriptionCusto = 0.0
                                    gratuidade = 0.0

                            except:
                                etapas.append('** Et: ')
                                etapas.append(countEtapa)
                                etapas.append('Description')
                                etapas.append(0.0)
                                somaDescriptionCusto = 0.0
                                gratuidade = 0.0
                                continue

                        if oneService['free'] == False:
                            etapas.append('** Et: ')
                            etapas.append(countEtapa)
                            etapas.append('Custo')
                            etapas.append(1.0)
                            somaCusto += 1.0
                            gratuidade = 1.0
                            somaDescriptionCusto = 1.0
                            #print 'entrou aqui false 88.0'
                        '''else:
                            etapas.append('** Et: ')
                            etapas.append(countEtapa)
                            etapas.append('Custo')
                            etapas.append(0.0)
                            somaCusto += 0.0
                            somaDescriptionCusto = 0.0
                            #print 'entrou aqui false 99.0'''

                    #FIM DA VERIFICAÇÃO DAS ETAPAS

                    if countEtapa != 0.0:
                        if somaTitle != 0.0:
                            somaTitle1 = 1.0
                        else:
                            somaTitle1 = 0.0

                        if somaDescriprion != 0.0:
                            somaDescriprion1 = 1.0
                        else:
                            somaDescriprion1 = 0.0

                        if somaDocumentos != 0.0:
                            somaDocumentos1 = 1.0
                        else:
                            somaDocumentos1 = 0.0

                        if somaDocumentosExcecoes != 0.0:
                            somaDocumentosExcecoes1 = 1.0
                        else:
                            somaDocumentosExcecoes1 = 0.0

                        if somaCanais != 0.0:
                            somaCanais1 = 1.0
                        else:
                            somaCanais1 = 0.0

                        if somaCusto != 0.0:
                            somaCusto1 = 1.0
                        else:
                            somaCusto1 = 0.0



                        countEtapa1 = 1.0

                    else:
                        countEtapa1 = 0.0



#countEtapa1, '\t', somaTitle1, '\t', somaDescriprion1, '\t', somaDocumentos1, '\t', somaDocumentosExcecoes1, '\t', somaCanais1, '\t', somaCusto1, '\t', somaDescriptionCusto1, '\t'
                    #mediaEtapa =  (countEtapa + somaTitle + somaDescriprion + somaDocumentos + somaCanais + somaCusto + somaDescriptionCusto)/7

                    #QTDO_brigatorio = round ((NomeServico + DescricaoServico + UnidadesAtendimento + Solicitante + Categoria + countEtapa1 +  somaTitle1 + somaDescriprion1),2)
                    #QTD_opcionais = round ((NomesPopulares + Tempo + typeTempo + ComentariosTempo + OutrasInformacoes + SolicitanteTipo + SolicitanteRequisitos + PublicoAlvo + somaDocumentos1 + somaDocumentosExcecoes1 + somaCanais1 + somaCusto1 + somaDescriptionCusto1),2)

                    #Percentual_Obrigatorio = round (round(QTDO_brigatorio,2)/round(8.0,2),2)
                    #Percentual_Opcionais =  round((round(QTD_opcionais,2)/round(13.0, 2)),2)
                    #CompletudeTotal = round (((QTDO_brigatorio + QTD_opcionais)/21.0),2)



                else:
                    somaTitle1 = 0.0
                    somaDescriprion1 = 0.0
                    somaDocumentos1 = 0.0
                    somaDocumentosExcecoes1  = 0.0
                    somaCanais1  = 0.0
                    somaCusto1  = 0.0
                    somaDescriptionCusto =  0.0

                QTDO_brigatorio = NomeServico + DescricaoServico + UnidadesAtendimento + \
                                  Solicitante + Categoria + PublicoAlvo + somaTitle1 + \
                                  somaDescriprion1 + maturidade

                QTD_opcionais = NomesPopulares + Tempo + ComentariosTempo + OutrasInformacoes + somaDocumentos1 + \
                                somaDocumentosExcecoes1 + somaCanais1 + somaCusto1 + somaDescriptionCusto

                Percentual_Obrigatorio = QTDO_brigatorio / 9.0
                Percentual_Opcionais = QTD_opcionais / 9.0
                CompletudeTotal = (QTDO_brigatorio + QTD_opcionais) / 18.0

                ServicoName2 = u'%s' % (oneService['name'])
                Sigla = u'%s' % (Sigla)

                ultimaAtualizacao = u'%s' % oneService['latest_updater']

                oneService['active']

                try:

                    writer.writerow((Sigla.encode('utf8'), ServicoId, ServicoName2.encode('utf8'),
                                     str(QTDO_brigatorio).replace(".", ","),
                                     str(QTD_opcionais).replace(".", ","),
                                     str(Percentual_Obrigatorio).replace(".", ","),
                                     str(Percentual_Opcionais).replace(".", ","),
                                     str(CompletudeTotal).replace(".", ","),
                                     oneService['active'], ultimaAtualizacao.encode('utf8'),
                                     oneService['date_modified'], oneService['date'],

                                     str(NomeServico).replace(".", ","), str(DescricaoServico).replace(".", ","),
                                     str(UnidadesAtendimento).replace(".", ","),
                                     str(Solicitante).replace(".", ","), str(Categoria).replace(".", ","),
                                     str(PublicoAlvo).replace(".", ","), str(maturidade).replace(".", ","),
                                     str(somaTitle1).replace(".", ","),
                                     str(somaDescriprion1).replace(".", ","),

                                     str(NomesPopulares).replace(".", ","), str(Tempo).replace(".", ","),
                                     str(ComentariosTempo).replace(".", ","), oneService['free'],
                                     str(OutrasInformacoes).replace(".", ","),
                                     str(somaDocumentos1).replace(".", ","),
                                     str(somaDocumentosExcecoes1).replace(".", ","),
                                     str(somaCanais1).replace(".", ","),
                                     str(somaCusto1).replace(".", ","), str(somaDescriptionCusto).replace(".", ",")

                                     ))

                    print Sigla.encode('utf8'), '\t', ServicoId, '\t', ServicoName2.encode('utf8'), '\t', str(
                        QTDO_brigatorio).replace(".", ","), '\t', str(QTD_opcionais).replace(".", ","), '\t', str(
                        Percentual_Obrigatorio).replace(".", ","), '\t', str(Percentual_Opcionais).replace(".",
                                                                                                           ","), '\t', str(
                        CompletudeTotal).replace(".", ","), '\t', oneService[
                        'active'], '\t', ultimaAtualizacao.encode('utf8'), '\t', oneService['date_modified'], '\t', \
                    oneService['date'], '\t', str(NomeServico).replace(".", ","), '\t', str(
                        DescricaoServico).replace(".", ","), '\t', str(UnidadesAtendimento).replace(".",
                                                                                                    ","), '\t', str(
                        Solicitante).replace(".", ","), '\t', str(Categoria).replace(".", ","), '\t', str(
                        PublicoAlvo).replace(".", ","), '\t', str(maturidade).replace(".", ","), '\t', str(
                        somaTitle1).replace(".", ","), '\t', str(somaDescriprion1).replace(".", ","), '\t', str(
                        NomesPopulares).replace(".", ","), '\t', str(Tempo).replace(".", ","), '\t', str(
                        ComentariosTempo).replace(".", ","), '\t', oneService['free'], '\t', str(
                        OutrasInformacoes).replace(".", ","), '\t', str(somaDocumentos1).replace(".",
                                                                                                 ","), '\t', str(
                        somaDocumentosExcecoes1).replace(".", ","), '\t', str(somaCanais1).replace(".",
                                                                                                   ","), '\t', str(
                        somaCusto1).replace(".", ","), '\t', str(somaDescriptionCusto).replace(".", ",")



                finally:
                    pass



                        #writer.writerow((Sigla.encode('utf8'), ServicoId,  ServicoName2.encode('utf8'), QTDO_brigatorio,  QTD_opcionais,  Percentual_Obrigatorio, Percentual_Opcionais,CompletudeTotal,
                         #                oneService['active'],  ultimaAtualizacao.encode('utf8'), oneService['date_modified'], oneService['date'],

                          #               NomeServico, NomesPopulares,  DescricaoServico, UnidadesAtendimento,Tempo,  typeTempo,  ComentariosTempo, OutrasInformacoes,  Solicitante, SolicitanteTipo,  SolicitanteRequisitos, Categoria,  PublicoAlvo,
                           #              0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                            #             0.0,  0.0,  0.0,  0.0,  0.0,0.0, 0.0, 0.0, []))


        print countservices
