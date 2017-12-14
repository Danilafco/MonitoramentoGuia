# -*- coding: utf-8 -*-
import urllib, json
import csv

class CompletudeOrgaos():

    def getorgaos(self):

        arquivo = open('completudeOrgao.csv', 'wb')

        url = "http://186.249.51.81/api/v1/organs.json"
        response = urllib.urlopen(url)
        organ = json.loads(response.read())
        # Nível de detalhamento das Informações dos Serviços (IS)
        # print(organ[0])


        try:
            writer = csv.writer(arquivo, delimiter='\t')
            writer.writerow(('Nome', 'ID', 'Nome do Órgão*: ', 'NomesPopulares: ', 'Endereço Principal*: ', 'Natureza*: ', 'Telefones: ', 'Horário: ', 'Campos Obrigatórios (4 totais): ', 'Campos Opcionais (2 totais): ', 'COMPLETUDE (6 totais): '))
        finally:
            pass

        for i in organ:
            url2 = 'http://186.249.51.81/api/v1/organs/' + i['id'] + '.json'
            response2 = urllib.urlopen(url2)
            organDentro = json.loads(response2.read())
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


            nomeOrgao = u'%s' % (organDentro['name'])

            try:
                # writer.writerow( [organDentro['id']])
                # writer.writerow( (organDentro['id'], acronimo.encode("utf8") , oneService['id'], nomeServico.encode("utf8"), NomeServico,  NomesPopulares, DescricaoServico, oneService['free'], UnidadesAtendimento, Tempo, OutrasInformacoes, Solicitante, Categoria, PublicoAlvo, TituloEtapa, DescricaoEtapa, Custo, CanaisPrestacao, Documentos, ComentariosTempo, ComentariosCusto, ComentariosCusto, CamposObrigatorios, CamposOpcionais, Completude))
                writer.writerow((nomeOrgao.encode("utf8"), organDentro['id'], NomeOrgao,  NomesPopulares, EnderecoPrincipal, Nature, Telefones, Horarios, CamposObrigatorios, CamposOpcionais, Completude))
            finally:
                pass
