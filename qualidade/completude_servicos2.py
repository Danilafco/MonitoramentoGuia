# -*- coding: UTF-8 -*-
import urllib, json
import csv

class CompletudeServico():

    def getservicos(self):
        #input()

        countEtapa = 0
        somaTitle = 0
        somaDescriprion = 0
        somaDocumentos = 0
        somaTypeChannel = 0
        descriptionCusto = 0
        somaCost = 0
        documentsCases = 0
        somaDocumentosCasos = 0
        countservices = 0


        etapas = []

        arquivo = open('completudeServicos2.csv', 'wb')

        url = "http://186.249.51.81/api/v1/organs.json"
        response = urllib.urlopen(url)
        organ = json.loads(response.read())

        # Nível de detalhamento das Informações dos Serviços (IS)
        # print(organ[0])
        try:
            writer = csv.writer(arquivo, delimiter='\t')
            # writer.writerow(('ID ORGAO', 'SIGLA', 'id Serv.', 'NomeServico', 'NomeServico*: ',
            #                  'NomesPopulares: ', 'DescricaoServico*: ', 'Gratuidade', 'UnidadeAtendim*: ',
            #                  'Tempo: ', 'Outras Informacoes: ', 'Solicitante*: ', 'Categoria*: ', 'Publico Alvo*: ',
            #                  'Titulo Etapa*: ', 'Descricao Etapa*: ', 'Custo Etapa: ', 'Canais de Prestacao: ',
            #                  'Documentos: ', 'Comentarios Tempo: ', 'Comentarios Custo: ', 'Excecoes de Documentos: ',
            #                  'Campos Obrigatorios 8 totais:', 'Campos Opcionais 8 totais: ', 'COMPLETUDE 16 totais:'))
            writer.writerow(('ID ORGAO', 'SIGLA', 'id Serv.', 'NomeServico*', 'NomeServico*: ',
                             'NomesPopulares: ', 'DescricaoServico*: ', 'Gratuidade', 'Custo', 'ComentariosCusto', 'UnidadeAtendim*: ',
                             'Tempo: ', 'Outras Informacoes: ', 'Solicitante*: ', 'Categoria*: ', 'Publico Alvo*: ',
                             'Comentarios Tempo: ',

                             'Quantidade etapas: ', 'Soma Titulo', 'Soma Descricao','Soma Documentos', 'Soma casos Documentos',
                             'Soma Channels', 'Soma Cost',

                             'Campos Obrigatorios 8 totais:', 'Campos Opcionais 8 totais: ', 'COMPLETUDE 16 totais:', 'BUFFER ETAPAS'))


        finally:
            pass

        for i in organ:

            url2 = 'http://186.249.51.81/api/v1/organs/' + i['id'] + '.json'
            response2 = urllib.urlopen(url2)
            organDentro = json.loads(response2.read())
            #print u'Orgão: ' + organDentro['name']

            for j in organDentro['service_ids']:
                countEtapa = 0
                countservices = countservices +1

                urlService = 'http://servicos.al.gov.br/api/v1/services/' + j + '.json'
                response3 = urllib.urlopen(urlService)
                oneService = json.loads(response3.read())

                # 1 - Verificação do nome do serviço
                if oneService['name'] != '':
                    NomeServico = 1
                else:
                    NomeServico = 0

                    # 2 - Verificação de nomes populares
                try:
                    if oneService['popular_names'][0]['name'] != '':
                        NomesPopulares = 1
                    else:
                        NomesPopulares = 0
                except:
                    NomesPopulares = 0
                    continue

                # 3 -  Verificação de descrição de serviços
                if oneService['description'] != '':
                    DescricaoServico = 1
                else:
                    DescricaoServico = 0

                # 4 - Verificação de Unidades de Atendimento
                try:
                    if oneService['unit_ids'] != '':
                        UnidadesAtendimento = 1
                    else:
                        UnidadesAtendimento = 0
                except:
                    UnidadesAtendimento = 0
                    continue

                # 5 - Verificação de Tempo
                try:
                    if oneService['estimated_time'] != '':
                        Tempo = 1
                    else:
                        Tempo = 0
                except:
                    Tempo = 0
                    continue

                # 6 - Verificação de Outras informações
                if oneService['other_informations'] != '':
                    OutrasInformacoes = 1
                else:
                    OutrasInformacoes = 0

                    # 7 - Verificação de Solicitante
                try:
                    if oneService['applicants'][0]['type'] != '':
                        Solicitante = 1
                    else:
                        Solicitante = 0
                except:
                    Solicitante = 0
                    continue

                # 8 - Verificação de Categoria
                try:
                    if oneService['categories'][0]['id'] != '':
                        Categoria = 1
                    else:
                        Categoria = 0
                except:
                    Categoria = 0
                    continue

                    # 9 - Verificação de público Alvo
                try:
                    if oneService['audiences'][0]['id'] != '':
                        PublicoAlvo = 1
                    else:
                        PublicoAlvo = 0
                except:
                    PublicoAlvo = 0
                    continue

                # INICIO verificação da etapa ----------------------------------------------------------------
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

                        #TituloEtapa = somaTitle / countEtapa


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

                        #DescricaoEtapa = somaDescriprion / countEtapa
                        try:
                         #   print '-----------------------------  try 1'
                            # VERIFICAÇÃO DOCUMENTOS ETAPAS
                            for n in i["documents"]:
                             #   print '-----------------------------  try 2', j
                                if n['name'] != '':
                                 #   print '-----------------------------  try 3', j
                                    documents = 1
                                    Documentos = 1
                                    etapas.append('Etapa: ')
                                    etapas.append(countEtapa)
                                    etapas.append('Documents')
                                    etapas.append(documents)
                                    somaDocumentos += documents

                                    try:
                                        if n['cases'] != '':
                                            documentsCases = 1
                                            etapas.append('Etapa: ')
                                            etapas.append(countEtapa)
                                            etapas.append('Documents Cases')
                                            etapas.append(documentsCases)
                                            somaDocumentosCasos += documentsCases
                                        else:
                                            documentsCases = 0
                                            etapas.append('Etapa: ')
                                            etapas.append(countEtapa)
                                            etapas.append('Documents Cases')
                                            etapas.append(documentsCases)

                                    except Exception as e:
                                    # print e
                                        continue

                                else:
                                  #  print '-----------------------------  try 4'
                                    documents = 0
                                    Documentos = 0
                                    etapas.append('Etapa: ')
                                    etapas.append(countEtapa)
                                    etapas.append('Documents')
                                    etapas.append(documents)
                                    somaDocumentos += documents


                        except Exception as e:
                           #print e
                            continue
                             #   print '-----------------------------  try 5'
                             #    etapas.append('Etapa: ')
                             #    etapas.append(countEtapa)
                             #    etapas.append('Documents')
                             #    etapas.append(documents)

                        try:
                            for p in i["providing_channels"]:
                             #   print '-----------------------------  try 2', j
                                if p['type'] != '':
                                 #   print '-----------------------------  try 3', j
                                    typeChannel = 1
                                    CanaisPrestacao = 0
                                    etapas.append('Etapa: ')
                                    etapas.append(countEtapa)
                                    etapas.append('Type Channel')
                                    etapas.append(typeChannel)
                                    somaTypeChannel += typeChannel
                                else:
                                  #  print '-----------------------------  try 4'
                                  typeChannel = 0
                                  CanaisPrestacao = 0
                                  etapas.append('Etapa: ')
                                  etapas.append(countEtapa)
                                  etapas.append('Type Channel')
                                  etapas.append(typeChannel)
                                  somaTypeChannel += typeChannel
                        except Exception as e:
                            # print e
                            continue

                        # Verificação do custo
                        #try:
                        if oneService['free'] == True:
                            if i["cost"]["value"] != '':
                                Custo = 1
                                cost = 1
                                etapas.append('Etapa: ')
                                etapas.append(countEtapa)
                                etapas.append('Cost')
                                etapas.append(cost)
                                somaCost = cost
                            else:
                              #  print '-----------------------------  try 4'
                              Custo = 0
                              cost = 0
                              etapas.append('Etapa: ')
                              etapas.append(countEtapa)
                              etapas.append('Cost')
                              etapas.append(cost)
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
                            Custo = 1
                            etapas.append('Etapa: ')
                            etapas.append(countEtapa)
                            etapas.append('Cost')
                            etapas.append(cost)
                            somaCost = cost
                        # except Exception as e:
                        #     # print e
                        #     pass
                except Exception as e:
                    # print e
                    continue
                # FIM verificação da etapa ----------------------------------------------------------------
                # 15 - Verificação de Comentários sobre o Tempo
                try:
                    if oneService['estimated_time']['description'] != '':
                        ComentariosTempo = 1
                    else:
                        ComentariosTempo = 0
                except:
                    ComentariosTempo = 0
                    continue

                if somaTitle != 0:
                    TituloEtapa = somaTitle / countEtapa
                else:
                    TituloEtapa = 0
                if somaDescriprion != 0:
                    DescricaoEtapa = somaDescriprion / countEtapa
                else:
                    DescricaoEtapa = 0

                CamposObrigatorios = TituloEtapa + DescricaoEtapa + NomeServico + DescricaoServico + UnidadesAtendimento + Solicitante + Categoria + PublicoAlvo
                CamposOpcionais = descriptionCusto + ComentariosTempo + NomesPopulares + Tempo + OutrasInformacoes + Custo + CanaisPrestacao + Documentos
                Completude = CamposObrigatorios + CamposOpcionais
                acronimo = u'%s' % (organDentro['acronym'])
                nomeServico = u'%s' % (oneService['name'])

                try:
                    writer.writerow((organDentro['id'], acronimo.encode("utf8"), oneService['id'],
                                     nomeServico.encode("utf8"), NomeServico, NomesPopulares, DescricaoServico,
                                     oneService['free'], Custo, descriptionCusto, UnidadesAtendimento, Tempo, OutrasInformacoes, Solicitante,
                                     Categoria, PublicoAlvo, ComentariosTempo,

                                     countEtapa, somaTitle, somaDescriprion, somaDocumentos, somaDocumentosCasos,
                                     somaTypeChannel, somaCost,

                                     CamposObrigatorios, CamposOpcionais, Completude, etapas))
                except Exception as e:
                    # print e
                    pass



                countEtapa = 0
                somaDescriprion = 0
                somaTitle = 0
                somaDocumentos = 0
                somaTypeChannel = 0
                documentsCases = 0
                somaDocumentosCasos = 0
                somaCost = 0
                etapas = []
                       # writer.writerow( (organDentro['id'], acronimo.encode("utf8") , oneService['id'],
                       #                   nomeServico.encode("utf8"), NomeServico,  NomesPopulares, DescricaoServico,
                       #                   oneService['free'], UnidadesAtendimento, Tempo, OutrasInformacoes, Solicitante,
                       #                   Categoria, PublicoAlvo, TituloEtapa, DescricaoEtapa, Custo, CanaisPrestacao,
                       #                   Documentos, ComentariosTempo, ComentariosCusto, ComentariosCusto, CamposObrigatorios,
                       #                   CamposOpcionais, Completude))



        print countservices
        countservices = 0

        # writer.writerow((
        #     'ID ORGAO', 'SIGLA', 'id Serv.', 'NomeServico', 'NomeServico*: ', 'NomesPopulares: ',
        #     'DescricaoServico*: ', 'Gratuidade', 'UnidadeAtendim*: ', 'Tempo: ',
        #     'Outras Informacoes: ', 'Solicitante*: ', 'Categoria*: ', 'Publico Alvo*: ',
        #     'Titulo Etapa*: ', 'Descricao Etapa*: ', 'Custo Etapa: ', 'Canais de Prestacao: ',
        #     'Documentos: ', 'Comentarios Tempo: ', 'Comentarios Custo: ',
        #     'Excecoes de Documentos: ', 'Campos Obrigatorios 8 totais:',
        #     'Campos Opcionais 8 totais: ', 'COMPLETUDE 16 totais:'))
        # writer.writerow((organDentro['id'], acronimo.encode("utf8"), oneService['id'], nomeServico.encode("utf8"),
        #                  NomeServico, NomesPopulares, DescricaoServico, oneService['free'], UnidadesAtendimento, Tempo,
        #                  OutrasInformacoes, Solicitante, Categoria, PublicoAlvo, TituloEtapa, DescricaoEtapa, Custo,
        #                  CanaisPrestacao, Documentos, ComentariosTempo, ComentariosCusto, ComentariosCusto,
        #                  CamposObrigatorios, CamposOpcionais, Completude))
        # arquivo.close()

