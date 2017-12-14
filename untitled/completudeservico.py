import urllib.request, json

class CompletudeServico():

    def getservicos(self,idOrgao):
        with urllib.request.urlopen("http://186.249.51.81/api/v1/organs/"+ idOrgao + ".json") as url:
            Organ = json.loads(url.read().decode())
            for i in Organ['service_ids']:
                urlService = 'http://186.249.51.81/api/v1/services/' + i + '.json'

                with urllib.request.urlopen(urlService) as url:
                    oneService = json.loads(url.read().decode())

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

                    # 5 - Verificação de Tempo
                    try:
                        if oneService['estimated_time'] != '':
                            Tempo = 1
                        else:
                            Tempo = 0
                    except:
                        Tempo = 0

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

                    # 8 - Verificação de Categoria
                    try:
                        if oneService['categories'][0]['id'] != '':
                            Categoria = 1
                        else:
                            Categoria = 0
                    except:
                        Categoria = 0

                        # 9 - Verificação de público Alvo
                    try:
                        if oneService['audiences'][0]['id'] != '':
                            PublicoAlvo = 1
                        else:
                            PublicoAlvo = 0
                    except:
                        PublicoAlvo = 0

                        # 9 - Verificação de nome da Etapa
                    try:
                        if oneService['steps'][0]['title'] != '':
                            TituloEtapa = 1
                        else:
                            TituloEtapa = 0
                    except:
                        TituloEtapa = 0
                        # 10 - Verificação de Descrição da Etapa
                    try:
                        if oneService['steps'][0]['description'] != '':
                            DescricaoEtapa = 1
                        else:
                            DescricaoEtapa = 0
                    except:
                        DescricaoEtapa = 0

                    # 12 - Verificação de Custo
                    if oneService['free'] != 'false':
                        # 12.1 - Verificação de Custo da Etapa
                        try:
                            StrCusto = oneService['steps'][0]['cost']['coin']
                            if StrCusto[2] != '':
                                print('entreou aqui 1')
                                Custo = 1
                            else:
                                print('entreou aqui 2')
                                Custo = 0
                                Gratuidade = 'Possui custos, mas não colocou o valor'
                        except:
                            print('entreou aqui 3')
                            Custo = 1
                    else:
                        Custo = 1

                    # 13 - Verificação de Canais Prestacao
                    try:
                        if oneService['steps'][0]['providing_channels'] != '':
                            CanaisPrestacao = 1
                        else:
                            CanaisPrestacao = 0
                    except:
                        CanaisPrestacao = 0

                    # 14 - Verificação de Documentos
                    try:
                        if oneService['steps'][0]['documents'] != '':
                            Documentos = 1
                        else:
                            Documentos = 0
                    except:
                        Documentos = 0

                    # 15 - Verificação de Comentários sobre o Tempo
                    try:
                        if oneService['estimated_time']['description'] != '':
                            ComentariosTempo = 1
                        else:
                            ComentariosTempo = 0
                    except:
                        ComentariosTempo = 0

                    # 17 - Verificação de Exceções de Documentos
                    try:
                        if oneService['estimated_time']['description'] != '':
                            ComentariosCusto = 1
                        else:
                            ComentariosCusto = 0
                    except:
                        ComentariosCusto = 0

                    CamposObrigatorios = TituloEtapa + DescricaoEtapa + NomeServico + DescricaoServico + UnidadesAtendimento + Solicitante + Categoria + PublicoAlvo
                    CamposOpcionais = ComentariosCusto + ComentariosTempo + NomesPopulares + Tempo + OutrasInformacoes + Custo + CanaisPrestacao + Documentos
                    Completude = CamposObrigatorios + CamposOpcionais

                    print(oneService['name'])
                    print(oneService['id'])
                    print('1 - NomeServico: ', NomeServico)
                    print('2 - NomesPopulares: ', NomesPopulares)
                    print('3 - DescricaoServico: ', DescricaoServico)
                    print('4 - Unidade Atendim: ', UnidadesAtendimento)
                    print('5 - Tempo: ', Tempo)
                    print('6 - Outras Informacoes: ', OutrasInformacoes)
                    print('7 - Solicitante: ', Solicitante)
                    print('8 - Categoria: ', Categoria)
                    print('9 - Público Alvo: ', PublicoAlvo)
                    print('10 - Titulo Etapa: ', TituloEtapa)
                    print('11 - Descricao Etapa: ', DescricaoEtapa)
                    print('12 - Gratuidade Serviço: ', StrCusto)
                    print('12.1 - Custo Etapa: ', Custo)
                    print('13 - Canais de Prestacao: ', CanaisPrestacao)
                    print('14 - Documentos: ', Documentos)
                    print('15 - Comentarios Tempo: ', ComentariosTempo)
                    print('16 - Comentarios Custo: ', ComentariosCusto)
                    print('17 - Exceções de Documentos: ', ComentariosCusto)
                    print('------------------------------------- ')
                    print('Campos Obrigatórios: ', CamposObrigatorios)
                    print('Campos Opcionais: ', CamposOpcionais)
                    print('COMPLETUDE: ', Completude)
                    print('------------------------------------- ')
                    print('\n \n')
