#!/usr/bin/env python3

#import getD3info
from abc import ABCMeta, abstractmethod

import urllib.request
import json

'''
    $this->item_url      = 'http://'.$server.$this->host.'/api/d3/data/';
    $this->follower_url  = 'http://'.$server.$this->host.'/api/d3/data/follower/';
    $this->artisan_url   = 'http://'.$server.$this->host.'/api/d3/data/artisan/';
    $this->item_img_url  = 'http://'.$server.$this->media_host.'/d3/icons/items/';
    $this->skill_img_url = 'http://'.$server.$this->media_host.'/d3/icons/skills/';
    $this->skill_url     = 'http://'.$server.$this->host.'/d3/'.substr($locale, 0, -3).'/tooltip/';
    $this->paperdoll_url = 'http://'.$server.$this->host.'/d3/static/images/profile/hero/paperdoll/';
'''






apiProfileBaseUrl = 'http://us.battle.net/api/d3/profile/'
apiItemBaseUrl = 'http://us.battle.net/api/d3/data/item/'


class AbstractRequest(metaclass=ABCMeta):


    @abstractmethod
    def RetrieveData(self):
        pass

    @abstractmethod
    def ParseData(self):
        pass

    @abstractmethod
    def GetData(self):
        ''' return the requested data'''
        pass



class ItemRequest(AbstractRequest):

    def __init__(self, itemId = None, query=None):
        if itemId is None:
            raise ValueError('ItemRequest init: missing itemId')

        if query is None:
            raise ValueError('ItemRequest init: missing query')

        self.itemId = itemId
        self.query = query

        self.url = apiItemBaseUrl + self.query
        print (self.url)


    def RetrieveData(self):
        # Retrieve html source from a given url
        source = urllib.request.urlopen(self.url).read().decode('utf-8')
        self.source = source

        # Get JSON
        jsonData = json.loads(self.source)
        self.jsonData = jsonData


        return self.jsonData

    def ParseData(self):
        self.type = None
        self.typeName = None
        self.gems = None



        self.type = self.jsonData['type']['id']
        print (self.type)
        self.typeName = self.jsonData['typeName']
        print (self.typeName)

        if self.jsonData['gems']:
            self.gems = self.jsonData['gems']
            print (self.gems)


    def GetData(self):
        pass









def main():
    user = {'username': 'sublime', 'battletag': 1487}
    item = ItemRequest(itemId=12, query='CroBCNm4uisSBwgEFZ-S1aUdIJ3kBB1oa9k0HQKZ58sdILQFlR3DDZzlHXCLd_AiCwgBFWdCAwAYDCAYMI8CONcEQABIAlAQWARgiwVqKwoMCAAQ6t-qlYCAgIAPEhsIuMi_2QkSBwgEFYEnlLEwiwI4AEABWASQAQBqKwoMCAAQ8d-qlYCAgIAPEhsIxpzCnAoSBwgEFYEnlLEwiwI4AEABWASQAQClASC0BZWtAY-QylC4AdyZkYEKwAEBGMG106ILUAJYAA')
    itemData = item.RetrieveData()
    print(json.dumps(itemData, indent=4, sort_keys=True))
    item.ParseData()
if __name__ == '__main__':

    main()


class ChampRequest():

    def __init__(self, uid={'username': None, 'battletag': None}):

        self.uid = uid
        self._Prepare()

    def _Prepare(self):
        self.RetrieveJSON()
        self.ParseHeroes()

    def RetrieveJSON(self):
        #request = getD3info.D3ApiRequest(self.uid)
        request.Retrieve()
        self.json = request.jsonData

    def ParseHeroes(self):
        '''
        return a dict{NormalHeroes = [h1, h2, ...], HardCoreHeroes = [h1, h2, ...]}
        '''
        normalHeroes = []
        harcoreHeroes = []
        for hero in self.json['heroes']:
            if hero['hardcore'] is True:
                harcoreHeroes.append(hero)
            else:
                normalHeroes.append(hero)

        heroes = {'normal': normalHeroes, 'hardcore': harcoreHeroes}
        self.heroes = heroes

    def GetInfo(self):
        return self.heroes

