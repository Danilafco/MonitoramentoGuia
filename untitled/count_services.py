import urllib.request, json

class CompletudeServico():
    def getservicos(self):
        Count = 0
        CountUnits = 0
        with urllib.request.urlopen("http://186.249.51.81/api/v1/organs.json") as url:
            organ = json.loads(url.read().decode())
            for i in organ:
                with urllib.request.urlopen('http://186.249.51.81/api/v1/organs/' + i['id'] + '.json') as url:
                    organDentro = json.loads(url.read().decode())

                    for idServicos in organDentro['service_ids']:
                        if idServicos != '':
                                Count += 1
                        else:
                            pass
                    for idUnits in organDentro['unit_ids']:
                        urlUnidade = 'http://servicos.al.gov.br/api/v1/units/' + idUnits + '.json'

                        if idUnits != '':
                                CountUnits += 1
                        else:
                            pass

                if organDentro['acronym'] in ['DETRAN', 'SETE' , 'CGE' , 'IMA' , 'SEMARH' , 'SECOM' , 'SEPLAG'
                                              , 'CASAL' , 'SECTI' , 'SEFAZ']:
                    grupo = 1
                elif organDentro['acronym'] in ['CBMAL' , 'ITEC' , 'SEAGRI' , 'SEADES' , 'FAPEAL' ,
                                                  'SEDUC' , 'JUCEAL' , 'Alagoas Previdência' , 'ALGÁS' , 'DITEAL' ,
                                                  'PROCON' , 'SEMUDH' , 'IPASEAL SAÚDE' , 'SEDETUR']:
                    grupo = 2
                elif organDentro['acronym'] in ['ADEAL' , 'ARSAL' , 'CEPAL' , 'Desenvolve' , 'EMATER' ,
                                                  'Gabinete Civil' , 'IDERAL' , 'ITERAL' , 'IZP' , 'POAL' , 'SECULT'
                                              , 'SELAJ' , 'SESAU']:
                    grupo = 3
                elif organDentro['acronym'] in ['Associação Comercial', 'Defensoria', 'PF', 'SEBRAE', 'SMTT']:
                    grupo = 0
                else:
                    grupo = 4
                print(organDentro['acronym'], '\t', 'Servicos: ', '\t', Count, '\t', 'Grupo', '\t', grupo, '\t', 'Unidades: ', '\t', CountUnits)
                Count = 0
                CountUnits = 0