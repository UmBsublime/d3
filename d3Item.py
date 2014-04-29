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
