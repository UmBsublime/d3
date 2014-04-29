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
            raise ValueError('D3ApiRequest: You need to init api request with username')
        if uid['battletag'] is None:
            raise ValueError('D3ApiRequest: You need to init api request with battletag')
            
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

def main():
    user = {'username': 'sublime', 'battletag': 1487}
    os.system('clear')

    request = D3ApiRequest(uid=user)
    request.DoIt()

if __name__ == '__main__':
    main()
