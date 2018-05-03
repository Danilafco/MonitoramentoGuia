# -*- coding: utf-8 -*-
import urllib, json

class CompletudeServico():
    def getservicos(self):
        url = "http://servicos.al.gov.br/api/v1/organs.json"
        response = urllib.urlopen(url)
        organ = json.loads(response.read())
        #print organ
        Count = 0
        CountUnits = 0
        print 'ID', '\t', 'Status Orgao', '\t', 'SIGLA', '\t', 'NOME', '\t' 'Nome Unidades', '\t' 'Status Unidades', '\t' 'Latitude', '\t' 'Longitude',
        for i in organ:
            urlorganDentro = 'http://servicos.al.gov.br/api/v1/organs/' + i['id'] + '.json'
            responseorganDentro = urllib.urlopen(urlorganDentro)
            organDentro = json.loads(responseorganDentro.read())
            #print organDentro['name']

            # if organDentro['unit_ids'] != [] or organDentro['unit_ids'] != '' or organDentro['unit_ids'] != None:
            try:
                for idUnits in organDentro['unit_ids']:
                    urlUnidade = 'http://servicos.al.gov.br/api/v1/units/' + idUnits + '.json'
                    try:

                        if urlUnidade['name'] != '' or None:
                            nomeUnidade = u'%s' % (urlUnidade['name'])
                        else:
                            nomeUnidade = ''

                        if urlUnidade['coordinates']['latitude'] != '':
                            UnitNamelatitude = urlUnidade['coordinates']['latitude']
                        else:
                            UnitNamelatitude = ''

                        if urlUnidade['coordinates']['longitude'] != '':
                            UnitNamelongitude = urlUnidade['coordinates']['longitude']
                        else:
                            UnitNamelongitude = ''
                    except Exception as e:
                        continue

                    print organDentro['id'], '\t', organDentro['active'], '\t', organDentro['acronym'], '\t', \
                        organDentro['name'], '\t', nomeUnidade, urlUnidade['active'], UnitNamelatitude, UnitNamelongitude
            except:

                print organDentro['id'], '\t', organDentro['active'], '\t', organDentro['acronym'], '\t', organDentro['name'], '\t', '', '', '', ''





