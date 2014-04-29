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
        self.userId = str(userId)  #lol
        self.query = query

        self.url = apiProfileBaseUrl.format(self.userName, self.userId, self.query)
        print (self.url)

    def ParseData(self):

        # Get stats
        self.stats = self.jsonData['stats']

        # Get items
        self.items = {}
        for item in self.jsonData['items']:
            self.items[item] = {'name': self.jsonData['items'][item]['name'],
                                'link': self.jsonData['items'][item]['tooltipParams']}

        # Get skills
        self.skills = {}
        for skill in self.jsonData['skills']['active']:
            self.skills[skill['skill']['name']] = {'rune': skill['rune']['description'],
                                                   'skill': skill['skill']['description']}
        self.data = {'stats':self.stats, 'skills': self.skills, 'items': self.items}

    def GetSkills(self):
        return self.skills

    def GetItems(self):
        return self.items

    def GetStats(self):
        return self.stats

def main():
    import json
    test = HeroRequest('sublime', 1487, '44528223')

    testData = test.GetData()
    print(json.dumps(testData, indent=4, sort_keys=True))
    test.ParseData()
    print (test.url)

    for item in testData['items']:
        print (item)
        print(testData['items'][item]['link'])


if __name__ == '__main__':
    main()
