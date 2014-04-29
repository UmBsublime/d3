#!/usr/bin/env python3

import genericAPIrequest as apiRequest

apiProfileBaseUrl = 'http://us.battle.net/api/d3/profile/{}-{}/'


class ProfileRequest(apiRequest.AbstractRequest):

    def __init__(self, userName=None, userId=None):
        if userName is None:
            raise ValueError('ItemRequest init: missing userName')
        if userId is None:
            raise ValueError('ItemRequest init: missing userId')

        self.userName = userName
        self.userId = str(userId)

        self.url = apiProfileBaseUrl.format(self.userName,  self.userId)
        print (self.url)

    def ParseData(self):
        '''
        return a dict{NormalHeroes = [h1, h2, ...], HardCoreHeroes = [h1, h2, ...]}
        '''
        normalHeroes = []
        harcoreHeroes = []
        for hero in self.jsonData['heroes']:
            if hero['hardcore'] is True:
                harcoreHeroes.append(hero)
            else:
                normalHeroes.append(hero)

        heroes = {'normal': normalHeroes, 'hardcore': harcoreHeroes}
        self.data = heroes

def main():
    import json
    test = ProfileRequest('sublime', 1487)

    testData = test.RetrieveData()
    #print(json.dumps(testData, indent=4, sort_keys=True))
    test.ParseData()

if __name__ == '__main__':
    main()
