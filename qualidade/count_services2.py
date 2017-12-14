# -*- coding: utf-8 -*-
import urllib, json

class CompletudeServico():
    def getservicos(self):
        url = "http://186.249.51.81/api/v1/organs.json"
        response = urllib.urlopen(url)
        organ = json.loads(response.read())
        #print organ
        Count = 0
        CountUnits = 0

        #orgaos = 'Órgão','\t','Servicos: ', '\t', 'Grupo', '\t', 'Unidades: '

        #print organDentro['acronym'], '\t', Count, '\t', grupo, '\t', CountUnits


        for i in organ:
            urlorganDentro = 'http://186.249.51.81/api/v1/organs/' + i['id'] + '.json'
            responseorganDentro = urllib.urlopen(urlorganDentro)
            organDentro = json.loads(responseorganDentro.read())
            #print organDentro['name']
            for idServicos in organDentro['service_ids']:
                if idServicos != '':
                    Count += 1
                else:
                    pass
            for idUnits in organDentro['unit_ids']:
                urlUnidade = 'http://servicos.al.gov.br/api/v1/units/' + idUnits + '.json'
                #print urlUnidade
                if idUnits != '':
                    CountUnits += 1
                else:
                    pass

            if organDentro['acronym'] in ['DETRAN', 'SETE', 'CGE', 'IMA', 'SEMARH', 'SECOM', 'SEPLAG'
                , 'CASAL', 'SECTI', 'SEFAZ'] and organDentro['active'] == 'true':
                grupo = 1
            elif organDentro['acronym'] in ['CBMAL', 'ITEC', 'SEAGRI', 'SEADES', 'FAPEAL',
                                            'SEDUC', 'JUCEAL', u'Alagoas Previdência', u'ALGÁS', 'DITEAL',
                                            'PROCON', 'SEMUDH', u'IPASEAL SAÚDE', 'SEDETUR'] and organDentro['active'] == 'true':
                grupo = 2
            elif organDentro['acronym'] in ['ADEAL', 'ARSAL', 'CEPAL', 'Desenvolve', 'EMATER',
                                            'Gabinete Civil', 'IDERAL', 'ITERAL', 'IZP', 'POAL', 'SECULT'
                , 'SELAJ', 'SESAU'] and organDentro['active'] == 'true':
                grupo = 3
            elif organDentro['acronym'] in [u'Associação Comercial', 'Defensoria', 'PF', 'SEBRAE', 'SMTT'] and organDentro['active'] == 'true':
                grupo = 4
            else:
                grupo = 0
            print organDentro['id'], '\t', organDentro['acronym'], '\t', 'Servicos: ', '\t', Count, '\t', 'Grupo', '\t', grupo, '\t', 'Unidades: ', '\t', CountUnits
            Count = 0
            CountUnits = 0



