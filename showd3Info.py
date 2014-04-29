#!/usr/bin/env python3

import interfaceD3info as d3Info
import os


# "Weight in tons {0.weight}"      # 'weight' attribute of first positional arg
# "Units destroyed: {players[0]}"  # First element of keyword argument 'players'.

#print (getD3info.DoAll('sublime', 1487))

def GetHeroes(userName, battleTag):
    heros = d3Info.ChampRequest(uid={'username': userName, 'battletag': battleTag})
    return heros.GetInfo()


def ChooseHeroType(heroes):
    print('   CHOOSE HERO TYPE')
    print('1. Normal')
    print('2. Hardcore')
    choice = input('What type do you want to see ?: ')
    if int(choice) is 1:
        showHeroes(heroes, 'normal', short=True)
    elif int(choice) is 2:
        showHeroes(heroes, 'hardcore', short=True)
    else:
        print ('you suck')


def showHeroes(heroes, heroType, short=False):
    os.system('clear')

    i = 0
    if short:
        print ('Heros are shown like this "name / level / class"')
    print ('*' * 80)
    for hero in heroes[heroType]:
        if short:
            i += 1
            print ('{:>2}.  |  {:<12} /  {:<4} /   {:<4}'.format(i,
                                                                 hero['name'],
                                                                 hero['level'],
                                                                 hero['class']
                                                                 ))
        else:
            print('{}: {}'.format('Name', hero['name']))
            print('{}: {}'.format('Class', hero['class']))
            print('{}: {}'.format('Level', hero['level']))
            if heroType is 'hardcore':
                print('{}: {}'.format('Dead', hero['dead']))

    print ('*' * 80)


def ShowHero(hero):
    #for key, value in hero.items() :
        #print ('{}: {}'.format(key, value))
    pass


def main():
    heroes = GetHeroes('sublime', 1487)
    ChooseHeroType(heroes)
    pass


if __name__ == '__main__':
    main()
