#!/usr/bin/env python3


from view.ProfileViewer import ProfileViewer
from view.HeroViewer import HeroViewer

from helper.general import getHero


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
