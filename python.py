import random
from tkinter import *
myfont="arial 14 bold"
def showName():
    fn=ftext.get()
    ln=ltext.get()
    ftext.delete(0,"end")
    ltext.delete(0,"end")
    mygen=PirateNameGenerator(fn,ln)
    pirateOutput=mygen.CreateName()
    output.config(text=pirateOutput,compound=CENTER)

    '''clear the boxes
    create and instance of class
    generate a name
    show it on screen'''


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
        return self.firstList[x]+" "+self.lastList[y]

root=Tk()
#create controls
banner=PhotoImage(file="pirate-banner.gif")
banner=banner.subsample(2,2)
##banner=banner.zoom(3,3)
title=Label(root,text="Hey There! I'm a crazy turtle title!",font="fixedsys 20 bold")
flabel=Label(root,text="First Name",font=myfont)
llabel=Label(root,text="Last Name",font=myfont)
ftext=Entry(root,font=myfont)
ltext=Entry(root,font=myfont)
bshow=Button(root,text="SHOW ME MY NAME YAAAA!",font=myfont,command=showName)
output=Label(root,text="HOI",font="BlackPearl",image=banner)

#grid controls
title.grid(row=0,column=0,columnspan=2)
flabel.grid(row=1,column=0)
llabel.grid(row=2,column=0)
ftext.grid(row=1,column=1)
ltext.grid(row=2,column=1)
bshow.grid(row=3,column=0,columnspan=2)
output.grid(row=4,column=0,columnspan=2)

root.mainloop()
