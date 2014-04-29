#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod
import urllib.request
import json


class AbstractRequest(metaclass=ABCMeta):

    @abstractmethod
    def ParseData(self):
        pass

    def RetrieveData(self):
        # Retrieve html source from a given url
        source = urllib.request.urlopen(self.url).read().decode('utf-8')
        self.source = source

        # Get JSON
        jsonData = json.loads(self.source)
        self.jsonData = jsonData

        return self.jsonData

    def GetData(self):
        self.RetrieveData()
        self.ParseData()

        return self.data
