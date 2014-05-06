#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod
import urllib.request
import json


class AbstractRequest(metaclass=ABCMeta):

    @abstractmethod
    def ParseData(self):
        data = None
        self.data = data
        pass

    def RetrieveData(self):
        # Retrieve html source from a given url
        source = urllib.request.urlopen(self.url).read().decode('utf-8')
        self.source = source

        # Get JSON
        jsonData = json.loads(self.source)
        self.jsonData = jsonData

        return self.jsonData

    def GetData(self):
        self.RetrieveData()
        self.ParseData()

        return self.data

def main():
    test = AbstractRequest()

if __name__ == '__main__':
    main()

'''
HeroRequest just returns EVERYTHING about the hero
    Hero will use it to fill itself
        Hero_container will contain all the heroes
            ProfileContainer will contain everything about all heroes and profile and manipulate Hero_container


AbstractRequest()
    HeroRequest()
    ItemRequest()
    ProfileRequest()

AbstractElement()
    +SendRequest()
    +ParseData()
    self.raw_data


    Skill():


    Hero()
    +GetItemUrl()
    self.item_url_collection[]
    self.skill_name_list
    self.


    Item()
    self.type
    self.modifier
    self.tooltip

        Gem():
        Weapon():
        Equipment():
            Arm():
            Shield():
             . . .
            Legs()

    Profile()
    +

AbstractContainer
    HeroContainer()

'''
class HeroRequest(AbstractRequest):

    apiProfileBaseUrl = 'http://us.battle.net/api/d3/profile/{}-{}/hero/{}'

    def __init__(self, userName=None, userId=None, hero_id=None):
        if userName is None:
            raise ValueError('ItemRequest init: missing userName')
        if userId is None:
            raise ValueError('ItemRequest init: missing userId')

        if hero_id is None:
            raise ValueError('ItemRequest init: missing query')

        self.userName = userName
        self.userId = str(userId)
        self.query = hero_id

        self.url = apiProfileBaseUrl.format(self.userName, self.userId, self.query)
        print ('Debug: {}'.format(self.url))

    def ParseData(self):
        self.items = {}

        # Get stats
        self.stats = self.jsonData['stats']

        # Get items
        for item in self.jsonData['items']:
            try:
                self.items[item] = {'name': self.jsonData['items'][item]['name'],
                                    'link': self.jsonData['items'][item]['tooltipParams']}
            except KeyError:
                pass

        # Get skills
        self.skills = {}
        for skill in self.jsonData['skills']['active']:
            try:
                self.skills[skill['skill']['name']] = {'rune': skill['rune']['description'],
                                                       'skill': skill['skill']['description']}
            except KeyError:
                pass

        self.data = {'stats':self.stats, 'skills': self.skills, 'items': self.items}

    def GetSkills(self):
        return self.skills

    def GetItems(self):
        return self.items

    def GetStats(self):
        return self.stats
