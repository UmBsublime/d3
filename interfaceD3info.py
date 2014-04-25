#!/usr/bin/env python3

import getD3info
from abc import ABCMeta, abstractmethod


class AbstractInterface(metaclass=ABCMeta):

    @abstractmethod
    def GetInfo(self):
        pass


class GetChamps(AbstractInterface):

    def __init__(self, uid={'username': None, 'battletag': None}):

        self.uid = uid

        champsRAW = getD3info.ChampRequest(uid)
        
        self.champs = champsRAW.GetHeroes()
        #print (self.champs)
        pass

    def GetInfo(self):
        return self.champs
        pass


def main():
    user = {'username': 'sublime', 'battletag': 1487}
    test = GetChamps(user)

if __name__ == '__main__':

    main()