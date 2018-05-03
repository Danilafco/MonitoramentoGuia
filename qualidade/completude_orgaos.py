# -*- coding: utf-8 -*-
import urllib, json
import csv

class CompletudeOrgaos():

    def getorgaos(self):

        arquivo = open('completudeOrgao.csv', 'wb')

        url = "http://servicos.al.gov.br/api/v1/organs.json"
        response = urllib.urlopen(url)
        organ = json.loads(response.read())
        # Nível de detalhamento das Informações dos Serviços (IS)
        # print(organ[0])


        try:
            writer = csv.writer(arquivo, delimiter='\t')
            writer.writerow(('Nome', 'ID', u'Município'.encode('utf8'),

                             'QTDO obrigatorio Inst.', 'QTD opcionais Inst.', 'Percentual Obrigatorio Inst.', 'Percentual Opcionais Inst.',
                             u'Nota da Instituição'.encode('utf8'),

                             u'Nome da Instituição*'.encode('utf8') , 'Natureza*' , 'Dirigente Principal*' , 'Cargo*' , 'Email Oficial*' , 'Site Oficial*', 'Municipio*' , 'Endereco Principal*' ,
                             'Nomes Populares Inst.' , 'Sigla Inst.' , 'Telefones' , 'Horarios',
                             u'Campos Obrigatórios (8 totais):'.encode('utf8'), 'Campos Opcionais (4 totais): ', 'COMPLETUDE (12 totais): '))


        finally:
            pass

        for i in organ:
            url2 = 'http://servicos.al.gov.br/api/v1/organs/' + i['id'] + '.json'
            response2 = urllib.urlopen(url2)
            organDentro = json.loads(response2.read())
            #  print (organDentro['name'],'\t',organDentro['acronym'],'\t','http://186.249.51.81/api/v1/organs/' + organDentro['id'] + '.json')

            # 1 - Verificação do nome do orgão
            if organDentro['name'] != '':
                NomeOrgao = 1.0
            else:
                NomeOrgao = 0.0

                # 2 - Verificação de nomes populares
            try:
                if organDentro['popular_names'][0]['name'] != '':
                    NomesPopulares = 1.0
                else:
                    NomesPopulares = 0.0
            except:
                NomesPopulares = 0.0

            # 1 - Verificação do nome da Natureza
            if organDentro['nature'] != '':
                Nature = 1.0
            else:
                Nature = 0.0

            # 1 - Verificação do nome do Endereço principal
            if organDentro['address'] != '':
                EnderecoPrincipal = 1.0
            else:
                EnderecoPrincipal = 0.0

            # 1 - Verificação do nome do Telefone
            if organDentro['phones'] != '':
                Telefones = 1.0
            else:
                Telefones = 0.0
            # 2 - Verificação de nomes populares
            try:
                if organDentro['schedules'][0]['day'] != '':
                    Horarios = 1.0
                else:
                    Horarios = 0.0
            except:
                Horarios = 0.0

            try:
                if organDentro['office'] != None:
                    Cargo = 1.0
                else:
                    Cargo = 0.0
            except:
                Cargo = 0.0

            try:
                if organDentro['chief_executive_officer'] != None:
                    DirigentePrincipal = 1.0
                else:
                    DirigentePrincipal = 0.0
            except:
                DirigentePrincipal = 0.0

            try:
                if organDentro['official_site'] != None:
                    SiteOficial = 1.0
                else:
                    SiteOficial = 0.0
            except:
                SiteOficial = 0.0

            try:
                if organDentro['official_email'] != None:
                    EmailOficial = 1.0
                else:
                    EmailOficial = 0.0
            except:
                EmailOficial = 0.0

            try:
                if organDentro['active'] != None:
                    status = 'ativo'
                else:
                    status = 'inativo'
            except:
                status = 'não informado'

            try:
                if organDentro['acronym'] != None or organDentro['acronym'] != '':
                    Sigla = 1.0
                else:
                    Sigla = 0.0
            except:
                Cargo = 0.0

            try:
                if organDentro['county'] != None or organDentro['county'] != '':
                    Municipio = 1.0
                else:
                    Municipio = 0.0
            except:
                Municipio = 0.0

            QTDO_brigatorio_orgaos = NomeOrgao +  Nature + DirigentePrincipal + Cargo + EmailOficial + SiteOficial + Municipio + EnderecoPrincipal
            QTD_opcionais_orgaos = NomesPopulares + Sigla + Telefones + Horarios

            Percentual_Obrigatorio_orgaos = QTDO_brigatorio_orgaos / 8.0
            Percentual_Opcionais_orgaos = QTD_opcionais_orgaos / 4.0
            CompletudeTotal_orgao = (QTDO_brigatorio_orgaos + QTD_opcionais_orgaos) / 12.0


            nomeOrgao = u'%s' % (organDentro['name'])
            MunicipioNome = u'%s' % (organDentro['county'])
            #status = u'%s' % organDentro['active']

            try:
                # writer.writerow( [organDentro['id']])
                # writer.writerow( (organDentro['id'], acronimo.encode("utf8") , oneService['id'], nomeServico.encode("utf8"), NomeServico,  NomesPopulares, DescricaoServico, oneService['free'], UnidadesAtendimento, Tempo, OutrasInformacoes, Solicitante, Categoria, PublicoAlvo, TituloEtapa, DescricaoEtapa, Custo, CanaisPrestacao, Documentos, ComentariosTempo, ComentariosCusto, ComentariosCusto, CamposObrigatorios, CamposOpcionais, Completude))
                writer.writerow((nomeOrgao.encode("utf8"), organDentro['id'], MunicipioNome.encode("utf8"),
                                 str(QTDO_brigatorio_orgaos).replace(".", ","),
                                 str(QTD_opcionais_orgaos).replace(".", ","),
                                 str(Percentual_Obrigatorio_orgaos).replace(".", ","),
                                 str(Percentual_Opcionais_orgaos).replace(".", ","),
                                 str(CompletudeTotal_orgao).replace(".", ","),

                                 str(NomeOrgao).replace(".", ",") , str(Nature).replace(".", ",") , str(DirigentePrincipal).replace(".", ",") ,
                                  str(Cargo).replace(".", ",") , str(EmailOficial).replace(".", ",") , str(SiteOficial).replace(".", ","),
                                 str(NomesPopulares).replace(".", ",") , str(Sigla).replace(".", ",") , str(Municipio).replace(".", ",") ,
                                 str(EnderecoPrincipal).replace(".", ",") , str(Telefones).replace(".", ","), str(Horarios).replace(".", ",")



                                 ))

                '''print nomeOrgao.encode("utf8"), '\t',organDentro['id'], '\t',NomeOrgao,'\t', Cargo, '\t',\
                                 DirigentePrincipal, '\t',SiteOficial, '\t',EmailOficial, '\t',organDentro['county'],'\t', NomesPopulares,'\t',\
                                 EnderecoPrincipal, '\t',Nature, '\t',Telefones, '\t',Horarios, '\t',CamposObrigatorios, '\t',CamposOpcionais,'\t',\
                                 Completude'''
            finally:
                pass
