# -*- coding: utf-8 -*-
import urllib, json
import csv

class NotaProveniencia():

    def getProveniencia(self):

        arquivo = open('proveniencia.csv', 'wb')

        url = "http://servicos.al.gov.br/api/v1/organs.json"
        response = urllib.urlopen(url)
        organ = json.loads(response.read())
        # Nível de detalhamento das Informações dos Serviços (IS)
        # print(organ[0])


        try:
            writer = csv.writer(arquivo, delimiter='\t')
            writer.writerow((u'Instituição Publicadora'.encode('utf8'), 'ID', 'Nota Proveniencia',
                             u'Nota nome Instituição'.encode('utf8'), u'Email Instituição'.encode('utf8') , u'Endereco Instituição'.encode('utf8') ,
                             u'Telefones Instituição'.encode('utf8')))

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


            try:
                if organDentro['official_email'] != None:
                    EmailOficial = 1.0
                else:
                    EmailOficial = 0.0
            except:
                EmailOficial = 0.0

            CompletudeProveniencia = NomeOrgao + Telefones + EmailOficial + EnderecoPrincipal

            NotaProveniencia = (CompletudeProveniencia) / 4.0


            nomeOrgao = u'%s' % (organDentro['name'])
            MunicipioNome = u'%s' % (organDentro['county'])
            #status = u'%s' % organDentro['active']

            try:
                # writer.writerow( [organDentro['id']])
                # writer.writerow( (organDentro['id'], acronimo.encode("utf8") , oneService['id'], nomeServico.encode("utf8"), NomeServico,  NomesPopulares, DescricaoServico, oneService['free'], UnidadesAtendimento, Tempo, OutrasInformacoes, Solicitante, Categoria, PublicoAlvo, TituloEtapa, DescricaoEtapa, Custo, CanaisPrestacao, Documentos, ComentariosTempo, ComentariosCusto, ComentariosCusto, CamposObrigatorios, CamposOpcionais, Completude))
                writer.writerow((nomeOrgao.encode("utf8"), organDentro['id'], NotaProveniencia,

                                 str(NomeOrgao).replace(".", ",") , str(EmailOficial).replace(".", ",") , str(EnderecoPrincipal).replace(".", ",") ,
                                 str(Telefones).replace(".", ",")
))

                '''print nomeOrgao.encode("utf8"), '\t',organDentro['id'], '\t',NomeOrgao,'\t', Cargo, '\t',\
                                 DirigentePrincipal, '\t',SiteOficial, '\t',EmailOficial, '\t',organDentro['county'],'\t', NomesPopulares,'\t',\
                                 EnderecoPrincipal, '\t',Nature, '\t',Telefones, '\t',Horarios, '\t',CamposObrigatorios, '\t',CamposOpcionais,'\t',\
                                 Completude'''
            finally:
                pass
