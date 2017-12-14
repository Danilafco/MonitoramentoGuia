import urllib.request, json

class CompletudeOrgaos():

    def getorgaos(self):

        with urllib.request.urlopen("http://186.249.51.81/api/v1/organs.json") as url:
            organ = json.loads(url.read().decode())
            # Nível de detalhamento das Informações dos Serviços (IS)
            # print(organ[0])
            for i in organ:
                with urllib.request.urlopen('http://186.249.51.81/api/v1/organs/' + i['id'] + '.json') as url:
                    organDentro = json.loads(url.read().decode())
                    #  print (organDentro['name'],'\t',organDentro['acronym'],'\t','http://186.249.51.81/api/v1/organs/' + organDentro['id'] + '.json')

                    # 1 - Verificação do nome do orgão
                    if organDentro['name'] != '':
                        NomeOrgao = 1
                    else:
                        NomeOrgao = 0

                        # 2 - Verificação de nomes populares
                    try:
                        if organDentro['popular_names'][0]['name'] != '':
                            NomesPopulares = 1
                        else:
                            NomesPopulares = 0
                    except:
                        NomesPopulares = 0

                    # 1 - Verificação do nome da Natureza
                    if organDentro['nature'] != '':
                        Nature = 1
                    else:
                        Nature = 0

                    # 1 - Verificação do nome do Endereço principal
                    if organDentro['address'] != '':
                        EnderecoPrincipal = 1
                    else:
                        EnderecoPrincipal = 0

                    # 1 - Verificação do nome do Telefone
                    if organDentro['phones'] != '':
                        Telefones = 1
                    else:
                        Telefones = 0
                    # 2 - Verificação de nomes populares
                    try:
                        if organDentro['schedules'][0]['day'] != '':
                            Horarios = 1
                        else:
                            Horarios = 0
                    except:
                        Horarios = 0

                    CamposObrigatorios = NomeOrgao +  Nature + Horarios + EnderecoPrincipal
                    CamposOpcionais = Telefones + NomesPopulares
                    Completude = CamposObrigatorios + CamposOpcionais

                    print(organDentro['name'])
                    print(organDentro['id'])
                    print('1 - NomeServico: ', NomeOrgao)
                    print('2 - NomesPopulares: ', NomesPopulares)
                    print('3 - Endereço Principal: ', EnderecoPrincipal)
                    print('4 - Unidade Atendim: ', Nature)
                    print('5 - Telefones: ', Telefones)
                    print('------------------------------------- ')
                    print('Campos Obrigatórios: ', CamposObrigatorios)
                    print('Campos Opcionais: ', CamposOpcionais)
                    print('COMPLETUDE: ', Completude)
                    print('------------------------------------- ')
                    print('\n \n')