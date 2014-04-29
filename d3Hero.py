#!/usr/bin/env python3

import genericAPIrequest as apiRequest

apiProfileBaseUrl = 'http://us.battle.net/api/d3/profile/{}-{}/hero/{}'


class HeroRequest(apiRequest.AbstractRequest):

    def __init__(self, userName=None, userId=None, query=None):
        if userName is None:
            raise ValueError('ItemRequest init: missing userName')
        if userId is None:
            raise ValueError('ItemRequest init: missing userId')

        if query is None:
            raise ValueError('ItemRequest init: missing query')

        self.userName = userName
        self.userId = str(userId)
        self.query = query

        self.url = apiProfileBaseUrl.format(self.userName, self.userId, self.query)
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
    test = HeroRequest('sublime', 1487, '44528223')

    testData = test.RetrieveData()
    #print(json.dumps(testData, indent=4, sort_keys=True))
    test.ParseData()
    pritn (test.url)


if __name__ == '__main__':
    main()
