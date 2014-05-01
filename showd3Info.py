#!/usr/bin/env python3

from abc import ABCMeta
import d3Profile, d3Item, d3Hero


def getHero(userName, userId, heroId):
    hero = d3Hero.HeroRequest(userName, userId, heroId)
    return hero.GetData()


class AbstractViewer(metaclass=ABCMeta):

    def _set_header(self, title, border='*'):

        border80 = border * 80
        title = '{border}{title:^78}{border}'.format(border=border, title=title)

        self.header = '{border80}\n{title}\n{border80}'.format(border80=border80, title=title)


class ProfileViewer(AbstractViewer):

    def __init__(self, userName, userId):

        self.userName = userName
        self.userId = userId
        profileRequest = d3Profile.ProfileRequest(userName, userId)
        self.profile = profileRequest.GetData()

        self.border1='*'
        self.border2='-'
        self._set_header('PROFILE')

        i = 0
        choiceMapping = {}
        for heroId in self.profile:
            i += 1
            choiceMapping[str(i)] = heroId

        self.choiceMapping = choiceMapping

    def set_hero(self, heroId):

        heroRequest = d3Hero.HeroRequest(self.userName, self.userId, heroId)
        self.hero = heroRequest.GetData()

    def get_hero(self, heroId):
        heroRequest = d3Hero.HeroRequest(self.userName, self.userId, heroId)
        return heroRequest.GetData()

    def get_heroId_mapping(self):
        return self.choiceMapping

    def print_profile(self):
        print(self.header)
        print(' #      {:<12} |  {:<4} |   {:<15}|  {:<4}'.format('NAME', 'LVL', 'CLASS', 'HARDCORE'))
        print(self.border2 * 80)
        i = 0
        for heroId in self.profile:
            i += 1
            print('{:>2}.  |  {:<12} |  {:<4} |   {:<15}|  {:<4}'.format(i,
                                                                         self.profile[heroId]['name'],
                                                                         self.profile[heroId]['level'],
                                                                         self.profile[heroId]['class'],
                                                                         str(self.profile[heroId]['hardcore'])
                                                                         ))
        print(self.border2 * 80)


class HeroViewer(AbstractViewer):

    def __init__(self, hero, border1='*', border2='-'):

        self.hero = hero
        self.border1 = border1
        self.border2 = border2
        self.header = None
        self._set_header('NO INIT')

    def print_items(self):
        self._set_header('ITEMS')
        print(self.header)

        for itemType, item in self.hero['items'].items():
            print('{:<15}: {}'.format(itemType,
                                      item['name']))

    def print_skills(self):
        self._set_header('SKILLS')
        print(self.header)

        for skillName, description in self.hero['skills'].items():
            print('SKILL\n{}\n{}\n\nRUNE\n{}'.format(skillName,
                                                     description['skill'],
                                                     description['rune']
                                                     ))
            print(self.border2 * 80)

    def print_stats(self):
        self._set_header('STATS')
        print(self.header)
        for name, stat in self.hero['stats'].items():
            print('{:<20}: {:<25}'.format(name, stat))


def main():

    import os

    os.system('clear')
    userName = 'sublime'
    userId = 1487

    myProfile = ProfileViewer(userName, userId)
    heroIdMapping = myProfile.get_heroId_mapping()

    myProfile.print_profile()
    choice = input("choose a hero <num>: ")
    heroId = heroIdMapping[str(choice)]

    hero = getHero(userName, userId, heroId)
    myHero = HeroViewer(hero)

    myHero.print_stats()
    myHero.print_items()
    myHero.print_skills()


if __name__ == '__main__':
    main()
