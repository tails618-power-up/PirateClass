import random
from tkinter import *

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
        pirateFirst=self.pirateFirstList[randF]
        pirateLast=self.pirateLastList[randL]
        return pirateFirst+" "+pirateLast

root=Tk()

root.mainloop()
