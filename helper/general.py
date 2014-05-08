from request.heroRequest import HeroRequest

def getHero(userName, userId, heroId):
    hero = HeroRequest(userName, userId, heroId)
    return hero.GetData()

