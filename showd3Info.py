#!/usr/bin/env python3

from view.ProfileViewer import ProfileViewer
from view.HeroViewer import HeroViewer


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


    myHero = HeroViewer(userName, userId, heroId )

    myHero.print_stats()
    myHero.print_items()
    myHero.print_skills()


if __name__ == '__main__':
    main()
