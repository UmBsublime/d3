from .abstractViewer import AbstractViewer
from request.heroRequest import HeroRequest


class HeroViewer(AbstractViewer):

    def __init__(self, userName, userId, heroId, border1='*', border2='-'):

        self.userName = userName
        self.userId = userId
        self.heroId = heroId

        self.border1 = border1
        self.border2 = border2

        heroRequest = HeroRequest(self.userName, self.userId, self.heroId)
        self.hero = heroRequest.GetData()
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

