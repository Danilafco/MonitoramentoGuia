import urllib.request, json

class CompletudeUnidades():

    def getunidades(self):

        with urllib.request.urlopen("http://186.249.51.81/api/v1/organs.json") as url:
            organ = json.loads(url.read().decode())
            # Nível de detalhamento das Informações dos Serviços (IS)
            # print(organ[0])
            for i in organ:
                with urllib.request.urlopen('http://186.249.51.81/api/v1/organs/' + i['id'] + '.json') as url:
                    organDentro = json.loads(url.read().decode())

                    for j in organDentro['unit_ids']:
                        urlUnidade = 'http://servicos.al.gov.br/api/v1/units/' + j + '.json'
                       # print(urlUnidade)
                        with urllib.request.urlopen(urlUnidade) as url:
                            unidadeDentro = json.loads(url.read().decode())

                            # 1 - Verificação do nome do orgão
                            if unidadeDentro['name'] != '':
                                NomeUnidade = 1
                            else:
                                NomeUnidade = 0

                            # 1 - Verificação do nome do Endereço principal
                            if unidadeDentro['address'] != '':
                                EnderecoPrincipal = 1
                            else:
                                EnderecoPrincipal = 0

                            # 1 - Verificação do nome do Telefone
                            if unidadeDentro['phones'] != '':
                                Telefones = 1
                            else:
                                Telefones = 0
                            # 2 - Verificação de nomes populares
                            try:
                                if unidadeDentro['schedules'][0]['day'] != None:
                                    Horarios = 1
                                else:
                                    Horarios = 0
                            except:
                                Horarios = 0

                            # 1 - Verificação do nome do orgão
                            if unidadeDentro['email'] != None:
                                Email = 1
                            else:
                                Email = 0

                            CamposObrigatorios = NomeUnidade + Horarios + EnderecoPrincipal
                            CamposOpcionais = Telefones + Email
                            Completude = CamposObrigatorios + CamposOpcionais

                            print(unidadeDentro['name'])
                            print(unidadeDentro['id'])
                            print('1 - NomeServico: ', NomeUnidade)
                            print('2 - Endereço Principal: ', EnderecoPrincipal)
                            print('3 - Telefones: ', Telefones)
                            print('3 - E-mail: ', Email)
                            print('4 - Horarios: ', Horarios)
                            print('------------------------------------- ')
                            print('Campos Obrigatórios: ', CamposObrigatorios)
                            print('Campos Opcionais: ', CamposOpcionais)
                            print('COMPLETUDE: ', Completude)
                            print('------------------------------------- ')
                            print('\n \n')

                    #  print (organDentro['name'],'\t',organDentro['acronym'],'\t','http://186.249.51.81/api/v1/organs/' + organDentro['id'] + '.json')