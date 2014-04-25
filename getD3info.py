#!/usr/bin/env python3


import urllib.request
import json

import sys
import os


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


class D3ApiRequest():

    def __init__(self, uid={'username': None, 'battletag': None}, query='', queryType='profile', ):

        self.query = query
        self.queryType = queryType
        self.uid = uid
        test = False
        if uid['username'] is None:
            print ('D3ApiRequest: You need to init api request with username')
            test = True
        if uid['battletag'] is None:
            print ('D3ApiRequest: You need to init api request with battletag')
            test = True

        if test:
            print('D3ApiRequest: api request init error')
            sys.exit()

        self.profileUrl = '{}{}-{}/'.format(apiProfileBaseUrl,
                                            self.uid['username'],
                                            self.uid['battletag']
                                            )

    def ForgeUrl(self):

        url = ''
        if self.queryType is 'profile':
            url = self.profileUrl
        elif self.queryType is 'item':
            url = apiItemBaseUrl + self.query
        elif self.queryType is 'champion':
            url = self.profileUrl + 'hero/' + self.query

        self.url = url

    def GetSource(self):
        ''' Retrieve html source from a given url '''
        source = urllib.request.urlopen(self.url).read().decode('utf-8')
        self.source = source
        return self.source

    def GetJSON(self):
        jsonData = json.loads(self.source)
        self.jsonData = jsonData
        return self.jsonData

    def Retrieve(self):
        self.ForgeUrl()
        self.GetSource()
        self.GetJSON()

    def DoIt(self):
        print('[-]Forging url')
        self.ForgeUrl()
        print ('Forged url: {}'.format(self.url))

        print('[-]Getting Source')
        self.GetSource()
        print ('Source: {}'.format(self.source))

        print('[-]Getting JSON')
        self.GetJSON()
        print ('JSON: {}'.format(self.jsonData))


class ChampRequest(object):

    def __init__(self, uid={'username': None, 'battletag': None}):

        self.uid = uid
        self._Prepare()

    def _Prepare(self):
        self.RetrieveJSON()
        self.ParseHeroes()

    def RetrieveJSON(self):
        request = D3ApiRequest(self.uid)
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

    def GetHeroes(self):
        return self.heroes



def main():
    user = {'username': 'sublime', 'battletag': 1487}
    os.system('clear')

    request = D3ApiRequest(uid=user)
    request.DoIt()

    testUser = ChampRequest(uid=user)
    testUser.json

    #champs = Champions('sublime', 1487)
    #print (champs.GetHeroes())


if __name__ == '__main__':
    main()

###############################
# OLD


class Champions():

    def __init__(self, userName, battleTag):

        self.userName = userName
        self.battleTag = battleTag
        self.url = self.ForgeUrl()
        self.source = self.GetSource()
        self.jsonData = self.GetJSON()

    def ForgeUrl(self):
        urlBase = 'http://us.battle.net/api/d3/profile/'
        url = urlBase + self.userName + '-' + str(self.battleTag) + '/'
        return url

    def GetSource(self):
        ''' Retrieve html source from a given url '''
        source = urllib.request.urlopen(self.url).read().decode('utf-8')
        return source

    def GetJSON(self):
        jsonData = json.loads(self.source)
        return jsonData

    def GetHeroes(self):
        '''
        return a dict{NormalHeroes = [h1, h2, ...], HardCoreHeroes = [h1, h2, ...]}
        '''
        normalHeroes = []
        harcoreHeroes = []
        for hero in self.jsonData['heroes']:
            if hero['hardcore'] is True:
                harcoreHeroes.append(hero)
            else:
                normalHeroes.append(hero)

        heroes = {'normal': normalHeroes, 'hardcore': harcoreHeroes}
        return heroes
