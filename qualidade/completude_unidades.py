# -*- coding: utf-8 -*-
import urllib, json
import csv

class CompletudeUnidades():

    def getunidades(self):

        arquivo = open('completudeUnidades.csv', 'wb')

        url = "http://186.249.51.81/api/v1/organs.json"
        response = urllib.urlopen(url)
        organ = json.loads(response.read())

        # Nível de detalhamento das Informações dos Serviços (IS)
        # print(organ[0])
        try:
            writer = csv.writer(arquivo, delimiter='\t')
            writer.writerow(('ID ORGAO', 'SIGLA ORGAO','Nome Unidade*', 'ID', 'Nome Unidade*: ', 'Endereço Principal*: ', 'Telefones: ', 'E-mail: ', 'Horarios*: ', 'Campos Obrigatórios (3 totais): ', 'Campos Opcionais (2 totais): ', 'COMPLETUDE (5 total): '))
        finally:
            pass

        for i in organ:
            url2 = 'http://186.249.51.81/api/v1/organs/' + i['id'] + '.json'
            response = urllib.urlopen(url2)
            organDentro = json.loads(response.read())
            #print u'Orgão: ' + organDentro['name']

            for j in organDentro['unit_ids']:
                urlUnidade = 'http://servicos.al.gov.br/api/v1/units/' + j + '.json'
                response2 = urllib.urlopen(urlUnidade)
                unidadeDentro = json.loads(response2.read())

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

                acronimo = u'%s' % (organDentro['acronym'])
                nomeUnidade = u'%s' % (unidadeDentro['name'])

                try:
                   # writer.writerow( [organDentro['id']])
                   #writer.writerow( (organDentro['id'], acronimo.encode("utf8") , oneService['id'], nomeServico.encode("utf8"), NomeServico,  NomesPopulares, DescricaoServico, oneService['free'], UnidadesAtendimento, Tempo, OutrasInformacoes, Solicitante, Categoria, PublicoAlvo, TituloEtapa, DescricaoEtapa, Custo, CanaisPrestacao, Documentos, ComentariosTempo, ComentariosCusto, ComentariosCusto, CamposObrigatorios, CamposOpcionais, Completude))
                   writer.writerow((organDentro['id'], acronimo.encode("utf8") ,nomeUnidade.encode("utf8"), unidadeDentro['id'], NomeUnidade, EnderecoPrincipal, Telefones, Email, Horarios, CamposObrigatorios, CamposOpcionais, Completude))
                finally:
                    pass




        #  print (organDentro['name'],'\t',organDentro['acronym'],'\t','http://186.249.51.81/api/v1/organs/' + organDentro['id'] + '.json')