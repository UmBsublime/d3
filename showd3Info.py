#!/usr/bin/env python3

from abc import ABCMeta

from Request.heroRequest import HeroRequest
from View.ProfileViewer import ProfileViewer
from View.HeroViewer import HeroViewer



def getHero(userName, userId, heroId):
    hero = HeroRequest(userName, userId, heroId)
    return hero.GetData()



def main():

    import os

    os.system('clear')
    userName = 'ltbart'
    userId = 1946

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
