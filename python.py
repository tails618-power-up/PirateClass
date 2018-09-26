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
        x=0
mypirate=PirateNameGenerator("The Savage Ghost","of the East")
