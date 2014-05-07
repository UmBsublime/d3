#!/usr/bin/env python3

import abstractRequest as apiRequest

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
        print ('Debug: {}'.format(self.url))

    def ParseData(self):
        '''
        return a dict
        '''
        heroIdList = {}
        for hero in self.jsonData['heroes']:
            heroIdList[hero['id']] = hero

        self.data = heroIdList

def main():
    import json
    test = ProfileRequest('sublime', 1487)

    testData = test.RetrieveData()
    #print(json.dumps(testData, indent=4, sort_keys=True))
    test.ParseData()
    print(json.dumps(test.GetData(), indent=4, sort_keys=True))

if __name__ == '__main__':
    main()
