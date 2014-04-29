class ChampRequest():

    def __init__(self, uid={'username': None, 'battletag': None}):

        self.uid = uid
        self._Prepare()

    def _Prepare(self):
        self.RetrieveJSON()
        self.ParseHeroes()

    def RetrieveJSON(self):
        #request = getD3info.D3ApiRequest(self.uid)
        request.Retrieve()
        self.json = request.jsonData

    def ParseHeroes(self):
        '''
        return a dict{NormalHeroes = [h1, h2, ...], HardCoreHeroes = [h1, h2, ...]}
        '''
        normalHeroes = []
        harcoreHeroes = []
        for hero in self.json['heroes']:
            if hero['hardcore'] is True:
                harcoreHeroes.append(hero)
            else:
                normalHeroes.append(hero)

        heroes = {'normal': normalHeroes, 'hardcore': harcoreHeroes}
        self.heroes = heroes

    def GetInfo(self):
        return self.heroes

