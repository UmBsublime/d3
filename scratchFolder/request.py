#!/usr/bin/env python3

import urllib.request
import json


class Request():

    def __init__(self, url):

        self.url = url


    def Fetch(self):
        # Retrieve html source from a given url
        source = urllib.request.urlopen(self.url).read().decode('utf-8')
        self.source = source
        # Get JSON
        jsonData = json.loads(self.source)

        self.data = jsonData



class Profile():

    baseUrl = 'http://us.battle.net/api/d3/profile/{}-{}/'

    def __init__(self, userName=None, userId=None):
        if userName is None:
            raise ValueError('Profile init: missing userName')
        if userId is None:
            raise ValueError('Profile init: missing userId')

        self.userName = userName
        self.userId = str(userId)

        self.url = Profile.baseUrl.format(self.userName,  self.userId)
        print ('Debug: {}'.format(self.url))

        r = Request(self.url)
        r.Fetch()
        self.raw_profile = r.data

class Hero():

    baseUrl = 'http://us.battle.net/api/d3/profile/{}-{}/hero/{}'

    def __init__(self, userName=None, userId=None, heroId=None):
        if userName is None:
            raise ValueError('Hero init: missing userName')
        if userId is None:
            raise ValueError('Hero init: missing userId')
        if heroId is None:
            raise ValueError('Hero init: missing heroId')

        self.userName = userName
        self.userId = str(userId)
        self.heroId = heroId

        self.url = Hero.baseUrl.format(self.userName, self.userId, self.heroId)
        print ('Debug: {}'.format(self.url))

        r = Request(self.url)
        r.Fetch()
        self.raw_hero = r.data

class Item():

    baseUrl = 'http://us.battle.net/api/d3/data/'

    def __init__(self, itemId = None):

        if itemId is None:
            raise ValueError('ItemRequest init: missing itemId')

        self.itemId = itemId

        self.url = Item.baseUrl + self.itemId
        print ('Debug: {}'.format(self.url))

        r = Request(self.url)
        r.Fetch()
        self.raw_item = r.data



def main():
    import json
    test = Profile('sublime', 1487)

    print(json.dumps(test.raw_profile, indent=4, sort_keys=True))

if __name__ == '__main__':
    main()


