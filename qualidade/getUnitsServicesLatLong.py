# -*- coding: UTF-8 -*-
import urllib, json
import csv

class CompletudeServico():

    def getservicos(self):
        countServices = 0

        arquivo = open('getLatLongUnitsServices.csv', 'wb')

        url = "http://servicos.al.gov.br/api/v1/units.json"
        response = urllib.urlopen(url)
        units = json.loads(response.read())

        try:
            writer = csv.writer(arquivo, delimiter='\t')

            print 'num ordem','\t', 'ID Servico','\t', 'nome Servico','\t', 'ID Units','\t', 'NomeUnidade: ','\t',  'Latitude','\t', 'Longitude'
            # writer.writerow(
            #     ('num ordem', 'ID Servico', 'nome Servico', 'ID Units', 'NomeUnidade: ', 'Latitude', 'Longitude',))


        except Exception as e:
            pass

        for i in units:
            countServices = 0

            url2 = 'http://servicos.al.gov.br/api/v1/units/' + i['id'] + '.json'
            response2 = urllib.urlopen(url2)
            unitDentro = json.loads(response2.read())

            try:

                if unitDentro['name'] != '':
                    nomeUnidade = u'%s' % (unitDentro['name'])
                else:
                    nomeUnidade = ''

                if unitDentro['coordinates']['latitude'] != '':
                    UnitNamelatitude = unitDentro['coordinates']['latitude']
                else:
                    UnitNamelatitude = ''

                if unitDentro['coordinates']['longitude'] != '':
                    UnitNamelongitude = unitDentro['coordinates']['longitude']
                else:
                    UnitNamelongitude = ''
            except Exception as e:
                continue

            if unitDentro['service_ids'] != []:

                for services in unitDentro['service_ids']:

                    urlService = 'http://servicos.al.gov.br/api/v1/services/' + services + '.json'
                    response3 = urllib.urlopen(urlService)
                    oneService = json.loads(response3.read())

                    nomeServico = u'%s' % (oneService['name'])


                    countServices += 1
                    # writer.writerow(countServices, oneService['id'], nomeServico , unitDentro['id'], nomeUnidade, UnitNamelatitude,
                    #                       UnitNamelongitude)
                    print countServices,'\t', oneService['id'],'\t', nomeServico,'\t', unitDentro['id'],'\t', nomeUnidade,'\t', UnitNamelatitude,'\t', UnitNamelongitude
            else:
                # writer.writerow((0, '', '', unitDentro['id'], nomeUnidade, UnitNamelatitude, UnitNamelongitude))
                print 0, '\t', '','\t', '','\t', unitDentro['id'],'\t', nomeUnidade,'\t', UnitNamelatitude,'\t', UnitNamelongitude




            #print UnitNamelatitude
            #print UnitNamelongitude

           # try:




                        # try:
                        #
                        #     if unitDentro['name'] != '':
                        #
                        #         writer.writerow((unitDentro['id'], nomeUnidade.encode("utf8"), UnitNamelatitude,
                        #                      UnitNamelongitude, countServices, oneService['id'], nomeServico))
                        #     else:
                        #         nomeUnidade = ''
                        #         nomeServico = ''
                        #
                        #         writer.writerow((unitDentro['id'], nomeUnidade.encode("utf8"), UnitNamelatitude,
                        #                      UnitNamelongitude, countServices, oneService['id'], nomeServico))
                        #
                        #     # print nomeUnidade.encode("utf8"),UnitNamelatitude,UnitNamelongitude, countServices
                        # except Exception as e:
                        #     pass
                    #print unitDentro['service_ids']
              #  else:
                    #countServices = 0

            # except Exception as e:
            #     continue

            # try:
            #
            #     if unitDentro['name'] != '':
            #         nomeUnidade = u'%s' % (unitDentro['name'])
            #     else:
            #         nomeUnidade = ''
            #
            #     #writer.writerow((unitDentro['id'], nomeUnidade.encode("utf8"),UnitNamelatitude,UnitNamelongitude, countServices ))
            #     writer.writerow((unitDentro['id'], nomeUnidade.encode("utf8"), UnitNamelatitude,
            #                          UnitNamelongitude, countServices, oneService['id'], oneService['name']))
            #
            #     #print nomeUnidade.encode("utf8"),UnitNamelatitude,UnitNamelongitude, countServices
            # except Exception as e:
            #     pass





