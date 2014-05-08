from .abstractViewer import AbstractViewer
from request.profileRequest import ProfileRequest

from element import abstractElement


class ProfileViewer(AbstractViewer):

    def __init__(self, userName, userId):

        self.userName = userName
        self.userId = userId
        profileRequest = ProfileRequest(userName, userId)
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
