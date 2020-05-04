from tkinter import *
from game.gameclass import Person
from game.gameclass import computer
import datetime
import random

global turncount
turncount = 0

                                                                   # multiple functions and inner function

def attackperson():
    global turncount
    turncount = turncount + 1                                      #output


    computerchoice = (random.choice([1, 2, 3]))

    if computerchoice == 1:                                         #if else
        w.config(text='Your swords collide with each other.')
        turnselectionoutputlist.append("Player chose: Attack. Computer chose was attack")
        turnselectionoutputdictionary[turncount] = "Player chose: Attack. Computer chose was attack"
        readgameturn.append("Player chose: Attack. Computer chose was attack")
    if computerchoice == 2:
        w.config(text='Your attack was blocked you got hurt from the impact')
        turnselectionoutputlist.append("Player chose: Attack. Computer chose was block")
        turnselectionoutputdictionary[turncount] = "Player chose: Attack. Computer chose was block"
        readgameturn.append("Player chose: Attack. Computer chose was block")
        p1.currenthealth = p1.currenthealth - c1.attack
    if computerchoice == 3:
        w.config(text='Your enemy tried to use magic you hit them. Stopping them from casting')
        turnselectionoutputlist.append("Player chose: Attack. Computer chose was magic")
        turnselectionoutputdictionary[turncount] = "Player chose: Attack. Computer chose was magic"
        readgameturn.append("Player chose: Attack. Computer chose was magic")
        c1.currenthealth = c1.currenthealth - p1.attack
    print("turn count is: ", turncount, "Player health: ", p1.currenthealth, " Computer Health: ", c1.currenthealth)
    check()


def blockbutton():
    global turncount
    turncount = turncount + 1

    computerchoice = (random.choice([1, 2, 3]))

    if computerchoice == 1:
        w.config(text='You have blocked your enemys attack you do damage to him from the impact')
        turnselectionoutputlist.append("Player chose: Block. Computer chose was attack")
        turnselectionoutputdictionary[turncount] = "Player chose: Block. Computer chose was attack"
        readgameturn.append("Player chose: Block. Computer chose was attack")
        c1.currenthealth = c1.currenthealth - p1.attack
    if computerchoice == 2:
        w.config(text='You both prepared to block nothing happens')
        turnselectionoutputlist.append("Player chose: Block. Computer chose was block")
        turnselectionoutputdictionary[turncount] = "Player chose: Block. Computer chose was block"
        readgameturn.append("Player chose: Block. Computer chose was block")

    if computerchoice == 3:
        w.config(text='Your enemy casted magic you cant block magic!')
        turnselectionoutputlist.append("Player chose: Block. Computer chose was magic")
        turnselectionoutputdictionary[turncount] = "Player chose: Block. Computer chose was Magic"
        readgameturn.append("Player chose: Block. Computer chose was Magic")
        p1.currenthealth = p1.currenthealth - c1.attack
    print("turn count is: ", turncount, "Player health: ", p1.currenthealth, " Computer Health: ", c1.currenthealth)
    check()


def Magicbutton():
    global turncount
    turncount = turncount + 1

    computerchoice = (random.choice([1, 2, 3]))

    if computerchoice == 1:
        w.config(text='Your enemy hit you while you were casting!')
        turnselectionoutputlist.append("Player chose: Magic. Computer chose was Attack")
        turnselectionoutputdictionary[turncount] = "Player chose: Magic. Computer chose was Attack"
        readgameturn.append("Player chose: Magic. Computer chose was Attack")
        p1.currenthealth = p1.currenthealth - c1.attack
    if computerchoice == 2:
        w.config(text='Your enemy tried to block you destroyed his defenses')
        turnselectionoutputlist.append("Player chose: Magic. Computer chose was block")
        turnselectionoutputdictionary[turncount] = "Player chose: Magic. Computer chose was block"
        c1.currenthealth = c1.currenthealth - p1.attack
        readgameturn.append("Player chose: Magic. Computer chose was block")
    if computerchoice == 3:
        w.config(text='You both used magic there was a large explosion negating the spells')
        turnselectionoutputlist.append("Player chose: Magic. Computer chose was Magic")
        turnselectionoutputdictionary[turncount] = "Player chose: Magic. Computer chose was Magic"
        readgameturn.append("Player chose: Magic. Computer chose was Magic")
    print("turn count is: ", turncount, "Player health: ", p1.currenthealth, " Computer Health: ", c1.currenthealth)
    check()



def setupfunction():
    global p1
    p1 = Person(1, 20, 2)
    print("player")
    print(p1.level)
    print(p1.maxhealth)
    print(p1.currenthealth)
    print(p1.attack)

    global c1
    c1 = computer(1, 20, 2)
    print("Computer")
    print(c1.level)
    print(c1.maxhealth)
    print(c1.currenthealth)
    print(c1.attack)

def check():
    global start
    global end

    if p1.currenthealth < 1:
        end = datetime.datetime.now()                                       #datetime end
        print("You started at: ", start, " You ended at: ", end)
        w.config(text='YOU LOSE!')
        try:                                                               #exception handling
            e1input = (e2.get())
            if e1input == "y":
                raise ValueError
        except:
            if e1input == "y":
                print("If your inputing y it needs to be Y")
        e1input.lower()

        if e1input == "Y":
            printtofile()
    if c1.currenthealth < 1:
        end = datetime.datetime.now()
        print("You started at: ", start, " You ended at: ", end)
        try:
            e1input = (e2.get())
            if e1input == "y":
                raise ValueError
        except:
            if e1input == "y":
                print("If your inputing y it needs to be Y")
        w.config(text='YOU WIN!')
        e1input.lower()
        if e1input == "Y":
            printtofile()


def printtofile():
    with open('turnselectionoutputlist.txt', 'w') as f:
        for item in turnselectionoutputlist:                                #for loop
            f.write("%s\n" % item)                                          #File i/o
    with open('turnselectionoutputdictionary.txt', 'w') as f:

        print(turnselectionoutputdictionary, file=f)
    with open('readgameturn.txt', 'w') as f:
        for x in readgameturn:
            f.write(x)
            f.write(" ")


if __name__ == "__main__":
    global start
    start = datetime.datetime.now()                             #datetime start
    setupfunction()
    global readgameturn
    readgameturn = []                                                   #array
    global turnselectionoutputlist
    turnselectionoutputlist = []                                        #list
    global turnselectionoutputdictionary
    turnselectionoutputdictionary = {}                                     #dictionary
    root = Tk()                                                           #gui component
    root.geometry("500x200")
    frame = Frame(root)
    frame.pack()
    Attackbutton = Button(frame, text='Attack', command=attackperson)
    Attackbutton.pack(side=LEFT)
    blockbutton = Button(frame, text='Block', command=blockbutton)
    blockbutton.pack(side=LEFT)
    Magicbutton = Button(frame, text='Magic', command=Magicbutton)
    Magicbutton.pack(side=LEFT)
    w = Label(root, text='')
    w.pack()
    text = Label(root, text='Put Y here for print to file')
    text.pack(side=LEFT)
    e2 = Entry(root)                                                        #user input
    e2.pack(side=LEFT)
    mainloop()


