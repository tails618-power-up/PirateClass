import random
class PirateNameGenerator():
    origFirst=""
    origLast=""

    firstList=["Rusty", "Fiendish","Corky"]
    lastList=["Swindles","Swabslop","Rattlebones"]
    def __init__(self,firstName,lastName):
        self.origFirst=firstName
        self.origLast=lastName

    def CreateName(self):
        x=random.randint(0,len(self.firstList)-1)
        y=random.randint(0,len(self.lastList)-1)
        return self.firstList[x]
        return self.lastList[y]

mypirate=PirateNameGenerator("The Savage Ghost","of the East")
print(mypirate.origFirst, mypirate.origLast)
print(mypirate.CreateName())
