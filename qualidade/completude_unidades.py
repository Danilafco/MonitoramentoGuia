# -*- coding: utf-8 -*-
import urllib, json
import csv

class CompletudeUnidades():

    def getunidades(self):

        arquivo = open('completudeUnidades.csv', 'wb')

        url = "http://servicos.al.gov.br/api/v1/organs.json"
        response = urllib.urlopen(url)
        organ = json.loads(response.read())

        # Nível de detalhamento das Informações dos Serviços (IS)
        # print(organ[0])
        try:
            writer = csv.writer(arquivo, delimiter='\t')
            writer.writerow(('ID Unidade', 'Orgao', 'Nome da U. A.', u'Município Unit.'.encode('utf8'),

                             'QTDO obrigatorio Uni.', 'QTD opcionais Uni.', 'Percentual Obrigatorio Uni.', 'Percentual Opcionais Uni.',
                             u'Nota da U. A.'.encode('utf8'),

                             'Nome da U.A.*:', 'Municipio Unit.*', 'Endereço Principal da U. A.*:', 'Telefones da U. A.:', 'Email da U. A:', 'Horarios U. A.:',

                             ))
        finally:
            pass

        for i in organ:
            url2 = 'http://servicos.al.gov.br/api/v1/organs/' + i['id'] + '.json'
            response = urllib.urlopen(url2)
            organDentro = json.loads(response.read())
            #print u'Orgão: ' + organDentro['name']

            for j in organDentro['unit_ids']:
                urlUnidade = 'http://servicos.al.gov.br/api/v1/units/' + j + '.json'
                response2 = urllib.urlopen(urlUnidade)
                unidadeDentro = json.loads(response2.read())

                # 1 - Verificação do nome do orgão
                if unidadeDentro['name'] != '':
                    NomeUnidade = 1.0
                else:
                    NomeUnidade = 0.0

                # 1 - Verificação do nome do Endereço principal
                if unidadeDentro['address'] != '':
                    EnderecoPrincipal = 1.0
                else:
                    EnderecoPrincipal = 0.0

                # 1 - Verificação do nome do Telefone
                if unidadeDentro['phones'] != '':
                    Telefones = 1.0
                else:
                    Telefones = 0.0
                # 2 - Verificação de nomes populares
                try:
                    if unidadeDentro['schedules'][0]['day'] != None:
                        Horarios = 1.0
                    else:
                        Horarios = 0.0
                except:
                    Horarios = 0.0

                # 1 - Verificação do nome do orgão
                if unidadeDentro['email'] != None:
                    Email = 1.0
                else:
                    Email = 0.0

                try:
                    if unidadeDentro['county'] != None or unidadeDentro['county'] != '':
                        Municipio = 1.0
                    else:
                        Municipio = 0.0
                except:
                    Municipio = 0.0

                CamposObrigatorios = NomeUnidade + Municipio + EnderecoPrincipal
                CamposOpcionais = Telefones + Email + Horarios
                Completude = CamposObrigatorios + CamposOpcionais

                Percentual_Obrigatorio_unit = CamposObrigatorios / 3.0
                Percentual_Opcionais_unit = CamposOpcionais / 3.0
                CompletudeTotal_unit = (CamposObrigatorios + CamposOpcionais) / 6.0


                acronimo = u'%s' % (organDentro['acronym'])
                nomeUnidade = u'%s' % (unidadeDentro['name'])
                MunicipioNomeUnit = u'%s' % (organDentro['county'])

                try:
                   # writer.writerow( [organDentro['id']])
                   #writer.writerow( (organDentro['id'], acronimo.encode("utf8") , oneService['id'], nomeServico.encode("utf8"), NomeServico,  NomesPopulares, DescricaoServico, oneService['free'], UnidadesAtendimento, Tempo, OutrasInformacoes, Solicitante, Categoria, PublicoAlvo, TituloEtapa, DescricaoEtapa, Custo, CanaisPrestacao, Documentos, ComentariosTempo, ComentariosCusto, ComentariosCusto, CamposObrigatorios, CamposOpcionais, Completude))
                   writer.writerow((unidadeDentro['id'], acronimo.encode("utf8") ,nomeUnidade.encode("utf8"), MunicipioNomeUnit.encode("utf8"),

                                    str(CamposObrigatorios).replace(".", ","),
                                    str(CamposOpcionais).replace(".", ","),
                                    str(Percentual_Obrigatorio_unit).replace(".", ","),
                                    str(Percentual_Opcionais_unit).replace(".", ","),
                                    str(CompletudeTotal_unit).replace(".", ","),

                                    str(NomeUnidade).replace(".", ","), str(Municipio).replace(".", ",") , str(EnderecoPrincipal).replace(".", ","),
                                    str(Telefones).replace(".", ","), str(Email).replace(".", ","), str(Horarios).replace(".", ",")

                                    ))
                finally:
                    pass




        #  print (organDentro['name'],'\t',organDentro['acronym'],'\t','http://186.249.51.81/api/v1/organs/' + organDentro['id'] + '.json')