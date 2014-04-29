#!/usr/bin/env python3

import d3Profile, d3Item, d3Hero
import os


def GetProfile(userName, userId):
    profile = d3Profile.ProfileRequest(userName, userId)
    #heroes.GetData()
    return profile.GetData()

def GetHero(userName, userId, heroId):
    hero = d3Hero.HeroRequest(userName, userId, heroId)
    return hero.GetData()


def showProfile(profile):
    os.system('clear')

    i = 0

    print ('Heros are shown like this "name / level / class / Hardcore"')
    print ('*' * 80)
    choiceMapping = {}
    for heroId in profile:
        i += 1
        choiceMapping[str(i)] = heroId
        print ('{:>2}.  |  {:<12} /  {:<4} /   {:<15}/  {:<4}'.format(i,
                                                                      profile[heroId]['name'],
                                                                      profile[heroId]['level'],
                                                                      profile[heroId]['class'],
                                                                      str(profile[heroId]['hardcore'])
                                                                      ))

    print ('*' * 80)

    moreInfo = input('What hero do you want info on ? <num>: ')

    try:
        heroId = choiceMapping[str(moreInfo)]
        #print (test)
        return heroId
    except KeyError:
        print ('invalid choice')


def ShowHero(hero):

    for name, stat in hero['stats'].items():
        print ('{:<20}: {:<10}'.format(name, stat))

    for skillName, value in hero['skills'].items():
        print ('*' * 80)
        print ('Skill Name: {}\n{}\nRune Effect: {}'.format(skillName,
                                                                          value['skill'],
                                                                          value['rune']))
    print ('*' * 80)
    #print (hero)


def main():
    userName = 'sublime'
    userId = 1487

    profile = GetProfile(userName, userId)
    #print (heroes)
    heroId = showProfile(profile)
    hero = GetHero(userName, userId, heroId)
    ShowHero(hero)


if __name__ == '__main__':
    main()
