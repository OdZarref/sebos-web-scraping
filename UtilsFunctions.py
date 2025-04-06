class UtilsFunctions:
    def getStrTime() -> str:
        from datetime import datetime
        return datetime.now().isoformat()[0:-13]

    def randintID() -> str:
        from random import randint
        return str(randint(10 ** 8, 10 ** 9))