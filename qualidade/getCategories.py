# -*- coding: UTF-8 -*-
import urllib, json
import csv

class CompletudeServico():

    def getservicos(self):
        countServices = 0
        #input()
        arquivo = open('getCategoria.csv', 'wb')

        url = "http://186.249.51.81/api/v1/organs.json"
        response = urllib.urlopen(url)
        organ = json.loads(response.read())

        # Nível de detalhamento das Informações dos Serviços (IS)
        # print(organ[0])
        try:
            writer = csv.writer(arquivo, delimiter='\t')
            # writer.writerow(('ID ORGAO', 'SIGLA', 'id Serv.', 'NomeServico', 'Categoria', 'NomeServico*: ', 'NomesPopulares: ', 'DescricaoServico*: ', 'Gratuidade', 'UnidadeAtendim*: ', 'Tempo: ', 'Outras Informacoes: ', 'Solicitante*: ', 'Categoria*: ', 'Publico Alvo*: ', 'Titulo Etapa*: ', 'Descricao Etapa*: ', 'Custo Etapa: ', 'Canais de Prestacao: ', 'Documentos: ', 'Comentarios Tempo: ', 'Comentarios Custo: ', 'Excecoes de Documentos: ', 'Campos Obrigatorios 8 totais:', 'Campos Opcionais 8 totais: ', 'COMPLETUDE 16 totais:'))
            #writer.writerow(('ID ORGAO', 'SIGLA', 'id Serv.', 'NomeServico', 'Categorias'))
            print 'ID ORGAO', '\t' ,'SIGLA', '\t', 'id Serv.', '\t', 'NomeServico', '\t', 'Categorias'

        finally:
            pass

        for i in organ:

            url2 = 'http://186.249.51.81/api/v1/organs/' + i['id'] + '.json'
            response2 = urllib.urlopen(url2)
            organDentro = json.loads(response2.read())
            #print u'Orgão: ' + organDentro['name']
            servico = []
            etapas = []
            for j in organDentro['service_ids']:
                urlService = 'http://servicos.al.gov.br/api/v1/services/' + j + '.json'
                response3 = urllib.urlopen(urlService)
                oneService = json.loads(response3.read())

                countServices +=1

                # 8 - Verificação de Categoria
                #acronimo = u'%s' % (organDentro['acronym'])
                #nomeServico = u'%s' % (oneService['name'])
                try:
                    for cat in oneService['categories']:
                        if cat['name'] != '':
                            Categoria = 1
                            CategoriaNome = cat['name']

                        else:
                            Categoria = 0
                            CategoriaNome = 'Não tem categoria'
                except:
                    Categoria = 0

                try:
                    if oneService['name'] != "":
                        ServicoName = u'%s' % (oneService['name'])
                    else:
                        ServicoName = 'Sem name'
                except:
                    ServicoName = 'Sem name'

                try:
                    if organDentro['acronym'] != "":
                        Sigla = u'%s' % (organDentro['acronym'])
                    else:
                        Sigla = 'Sem sigla'
                except:
                    Sigla = 'Sem sigla'

                try:
                    # writer.writerow((organDentro['id'], acronimo.encode("utf8"), oneService['id'],
                    #                 nomeServico.encode("utf8"), CategoriaNome.encode("utf8")))
                    print organDentro['id'], '\t', Sigla, '\t', oneService['id'], '\t',ServicoName, '\t', CategoriaNome
                except:
                    print organDentro['id'], '\t', Sigla, '\t', oneService['id'], '\t', ServicoName, '\t', 'não tem categoria'
                    pass







                    # 9 - Verificação de público Alvo
                # try:
                #     if oneService['audiences'][0]['id'] != '':
                #         PublicoAlvo = 1
                #     else:
                #         PublicoAlvo = 0
                # except:
                #     PublicoAlvo = 0
                #     # INICIO verificação da etapa ----------------------------------------------------------------
                #     # 9 - Verificação de nome da Etapa
                # try:
                #     if oneService['steps'][0]['title'] != '':
                #         TituloEtapa = 1
                #     else:
                #         TituloEtapa = 0
                # except:
                #     TituloEtapa = 0
                #     # 10 - Verificação de Descrição da Etapa
                # try:
                #     if oneService['steps'][0]['description'] != '':
                #         DescricaoEtapa = 1
                #     else:
                #         DescricaoEtapa = 0
                # except:
                #     DescricaoEtapa = 0
                #
                # # 12 - Verificação de Custo
                # if oneService['free'] != 'true':
                #     # 12.1 - Verificação de Custo da Etapa
                #     try:
                #         StrCusto = str(oneService['steps'][0]['cost']['value'])
                #         if StrCusto != '':
                #             #print('Cursto: ' + StrCusto)
                #             Custo = 1
                #         else:
                #             Custo = 0
                #             Gratuidade = 'Possui custos, mas não colocou o valor'
                #             #print(Gratuidade)
                #     except:
                #         #print('Não possui curso')
                #         Custo = 1
                # else:
                #     StrCusto = 'deu erro no valor'
                #     Custo = 1
                #
                # # 13 - Verificação de Canais Prestacao
                # try:
                #     if oneService['steps'][0]['providing_channels'] != '':
                #         CanaisPrestacao = 1
                #     else:
                #         CanaisPrestacao = 0
                # except:
                #     CanaisPrestacao = 0
                #
                # # 14 - Verificação de Documentos
                # try:
                #     if oneService['steps'][0]['documents'] != '':
                #         Documentos = 1
                #     else:
                #         Documentos = 0
                # except:
                #     Documentos = 0
                # # INICIO verificação da etapa ----------------------------------------------------------------
                # # 15 - Verificação de Comentários sobre o Tempo
                # try:
                #     if oneService['estimated_time']['description'] != '':
                #         ComentariosTempo = 1
                #     else:
                #         ComentariosTempo = 0
                # except:
                #     ComentariosTempo = 0
                #
                # # 17 - Verificação de Exceções de Documentos
                # try:
                #     if oneService['estimated_time']['description'] != '':
                #         ComentariosCusto = 1
                #     else:
                #         ComentariosCusto = 0
                # except:
                #     ComentariosCusto = 0
                #
                # CamposObrigatorios = TituloEtapa + DescricaoEtapa + NomeServico + DescricaoServico + UnidadesAtendimento + Solicitante + Categoria + PublicoAlvo
                # CamposOpcionais = ComentariosCusto + ComentariosTempo + NomesPopulares + Tempo + OutrasInformacoes + Custo + CanaisPrestacao + Documentos
                # Completude = CamposObrigatorios + CamposOpcionais
                # acronimo = u'%s' % (organDentro['acronym'])
                # nomeServico = u'%s' % (oneService['name'])
                # #Categoria = u'%s' % (oneService['categories'][0]['name'])
                #
                # try:
                #    # writer.writerow( [organDentro['id']])
                #    # writer.writerow((
                #    #                 'ID ORGAO', 'SIGLA', 'id Serv.', 'NomeServico', 'NomeServico*: ', 'NomesPopulares: ',
                #    #                 'DescricaoServico*: ', 'Gratuidade', 'UnidadeAtendim*: ', 'Tempo: ',
                #    #                 'Outras Informacoes: ', 'Solicitante*: ', 'Categoria*: ', 'Publico Alvo*: ',
                #    #                 'Titulo Etapa*: ', 'Descricao Etapa*: ', 'Custo Etapa: ', 'Canais de Prestacao: ',
                #    #                 'Documentos: ', 'Comentarios Tempo: ', 'Comentarios Custo: ',
                #    #                 'Excecoes de Documentos: ', 'Campos Obrigatorios 8 totais:',
                #    #                 'Campos Opcionais 8 totais: ', 'COMPLETUDE 16 totais:'))
                #    #writer.writerow( (organDentro['id'], acronimo.encode("utf8") , oneService['id'], nomeServico.encode("utf8"), CategoriaNome.encode("utf8"), NomeServico,  NomesPopulares, DescricaoServico, oneService['free'], UnidadesAtendimento, Tempo, OutrasInformacoes, Solicitante, Categoria, PublicoAlvo, TituloEtapa, DescricaoEtapa, Custo, CanaisPrestacao, Documentos, ComentariosTempo, ComentariosCusto, ComentariosCusto, CamposObrigatorios, CamposOpcionais, Completude))
                #   # writer.writerow( ([organDentro['id']], [organDentro['acronym']], [oneService['id']], [oneService['name']], [NomeServico],  [NomesPopulares], [DescricaoServico], [oneService['free']], [UnidadesAtendimento], [Tempo], [OutrasInformacoes], [Solicitante], [Categoria], [PublicoAlvo], [TituloEtapa], [DescricaoEtapa], [Custo], [CanaisPrestacao], [Documentos], [ComentariosTempo], [ComentariosCusto], [ComentariosCusto], [CamposObrigatorios], [CamposOpcionais], [Completude]))
                # finally:
                #     pass
                #
                # countServices = 0


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

