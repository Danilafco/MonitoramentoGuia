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
        ServicoAtivo = 0
        ServicoInativo = 0
        naoInformado = 0

        print 'ID', '\t', 'SIGLA', '\t', 'NOME', '\t', 'Servicos ', '\t', 'Serv. Ativos','\t', 'Serv. Inativos' ,'\t',  'Grupo', '\t' 'Unidades '
        for i in organ:
            urlorganDentro = 'http://servicos.al.gov.br/api/v1/organs/' + i['id'] + '.json'
            responseorganDentro = urllib.urlopen(urlorganDentro)
            organDentro = json.loads(responseorganDentro.read())
            #print organDentro['name']

            for idServicos in organDentro['service_ids']:
                urlService = 'http://servicos.al.gov.br/api/v1/services/' + idServicos + '.json'
                response3 = urllib.urlopen(urlService)
                oneService = json.loads(response3.read())

                try:
                    if oneService['active'] == True:
                        ServicoAtivo += 1

                    if oneService['active'] == False:
                        ServicoInativo += 1
                    if oneService['active'] != True and oneService['active'] != False:
                        ServicoInativo += 1
                except:
                    continue

                if idServicos != '':
                    Count += 1
                else:
                    Count += 0

            for idUnits in organDentro['unit_ids']:
                urlUnidade = 'http://servicos.al.gov.br/api/v1/units/' + idUnits + '.json'
                #print urlUnidade
                if idUnits != '':
                    CountUnits += 1
                else:
                    CountUnits += 1

            if organDentro['id'] in ['56d6ddc18c36c706ac000004', '56df02e98c36c74559000000', '588bae3e8c36c708b4355182',
                                     '57617efd8c36c7464f000000', '576c1f518c36c72a90000000', '588bb11a8c36c708b4355184', '56d723238c36c73983000000'
                , '56d6d7fb8c36c706ac000003', '588baf3e8c36c708b4355183', '5750117e8c36c718eb000005']:

                grupo = 1
            elif organDentro['id'] in ['590b70c68c36c71e8623bb3d', '590a38a68c36c731c7c20e8b', '590b28bf8c36c76305bd6326', '590a3bcd8c36c731c7c20e8c', '590a1de08c36c7298d7ee868',
                                            '5908eaf78c36c7723803da8f', '590a117e8c36c705ff74cad0', '577546098c36c702ca000002', '5908c3188c36c756f6a837b2', '590b30f58c36c76305bd6328',
                                            '56d6e60b8c36c706ac000007', '5908e8138c36c7723803da8e', '590880628c36c708368e836e', '590a256e8c36c731c7c20e88']:
                grupo = 2
            elif organDentro['id'] in ['57501cd88c36c718eb000009', '596e172e8c36c75d14a5a8a7', '596e43e18c36c775620b3b6e', '590b2c0a8c36c76305bd6327', '596ce1af8c36c71b0b29f7a4',
                                            '596cd96b8c36c726a878bbcb', '596e45fb8c36c705d7b97087',  '596e48978c36c7078649c047', '56d6de778c36c706ac000006', '596e4b0f8c36c70a18c2cc90', '596e4b6c8c36c70a18c2cc91',
                                       '596e4d008c36c70a18c2cc92']:
                grupo = 3

            elif organDentro['id'] in ['57b1ecb08c36c75e61000006', '57501ee98c36c718eb00000b', '57c59b5e8c36c76bff000000',
                                       '57754bce8c36c702ca000003', '577e999e8c36c72d65000000', '5a15bfcb547bb36c51ab7864',
                                       '5a15bb6b547bb36c51ab7863','5a16d5be547bb32a341abae9', '5a05d7c9547bb337d23da50c', '5975f13e8c36c75066f55800',
                                       '5975ec948c36c75066f557fc', '5975ee148c36c75066f557fd',  '5975f20f8c36c75066f55801', '596e46de8c36c7078649c046', '5975efc28c36c75066f557ff', '5975e72b8c36c75066f557f5',
                                       '5975e7cc8c36c75066f557f6', '5975ea488c36c75066f557f9', '5975e9298c36c75066f557f8',
                                       '5975ec048c36c75066f557fb', '5975e68f8c36c75066f557f4', '5975e8a18c36c75066f557f7',
                                       '5975ef298c36c75066f557fe', '5975fae08c36c76601b0494f', '58e233698c36c738a1844d9a', '5a16d404547bb32a441abae8', '5a16bae3547bb310b13fd80a',
                                       '5a16bc54547bb310b13fd80b', '5a16d2af547bb32a341abae8', '5a4d152b547bb36ab17faae5', '5a749114547bb357304fa309']:
                 grupo = 4
            else:
                 grupo = 0


            print organDentro['id'], '\t',  organDentro['acronym'], '\t', organDentro['name'], '\t', Count, '\t', ServicoAtivo, '\t', ServicoInativo,  '\t', grupo, '\t', CountUnits

            Count = 0
            CountUnits = 0
            ServicoAtivo = 0
            ServicoInativo = 0
            naoInformado = 0



