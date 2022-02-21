
import os
import sys
import random
from enum import Enum, auto
import tkinter
import time
import pickle
from tkinter import *
import threading
from typing import get_args
from PyQt5 import QtCore, QtGui, QtWidgets

app = QtWidgets.QApplication(sys.argv)

class GameInfo():
    def __init__(self):
        self.gamePaused = False
        self.inDecision = False
        self.decisionNr = 'x'
        self.isSkipped = False

gameinfo = GameInfo()

multiplier = 3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(449 * multiplier, 290 * multiplier)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.option8 = QtWidgets.QPushButton(self.centralwidget)
        self.option8.setGeometry(QtCore.QRect(151 * multiplier, 200 * multiplier, 150 * multiplier, 30 * multiplier))
        self.option8.setObjectName("option8")
        self.option1 = QtWidgets.QPushButton(self.centralwidget)
        self.option1.setGeometry(QtCore.QRect(0 * multiplier, 140 * multiplier, 151 * multiplier, 30 * multiplier))
        self.option1.setObjectName("option1")
        self.option2 = QtWidgets.QPushButton(self.centralwidget)
        self.option2.setGeometry(QtCore.QRect(151 * multiplier, 140 * multiplier, 150 * multiplier, 30 * multiplier))
        self.option2.setObjectName("option2")
        self.option3 = QtWidgets.QPushButton(self.centralwidget)
        self.option3.setGeometry(QtCore.QRect(301 * multiplier, 140 * multiplier, 150 * multiplier, 30 * multiplier))
        self.option3.setObjectName("option3")
        self.option4 = QtWidgets.QPushButton(self.centralwidget)
        self.option4.setGeometry(QtCore.QRect(0 * multiplier, 170 * multiplier, 151 * multiplier, 30 * multiplier))
        self.option4.setObjectName("option4")
        self.option6 = QtWidgets.QPushButton(self.centralwidget)
        self.option6.setGeometry(QtCore.QRect(301 * multiplier, 170 * multiplier, 150 * multiplier, 30 * multiplier))
        self.option6.setObjectName("option6")
        self.option9 = QtWidgets.QPushButton(self.centralwidget)
        self.option9.setGeometry(QtCore.QRect(301 * multiplier, 200 * multiplier, 150 * multiplier, 30 * multiplier))
        self.option9.setObjectName("option9")
        self.option5 = QtWidgets.QPushButton(self.centralwidget)
        self.option5.setGeometry(QtCore.QRect(151 * multiplier, 170 * multiplier, 150 * multiplier, 30 * multiplier))
        self.option5.setObjectName("option5")
        self.option7 = QtWidgets.QPushButton(self.centralwidget)
        self.option7.setGeometry(QtCore.QRect(0 * multiplier, 200 * multiplier, 151 * multiplier, 30 * multiplier))
        self.option7.setObjectName("option7")
        self.option12 = QtWidgets.QPushButton(self.centralwidget)
        self.option12.setGeometry(QtCore.QRect(301 * multiplier, 230 * multiplier, 150 * multiplier, 30 * multiplier))
        self.option12.setObjectName("option12")
        self.option11 = QtWidgets.QPushButton(self.centralwidget)
        self.option11.setEnabled(True)
        self.option11.setGeometry(QtCore.QRect(151 * multiplier, 230 * multiplier, 150 * multiplier, 30 * multiplier))
        self.option11.setObjectName("option11")
        self.option10 = QtWidgets.QPushButton(self.centralwidget)
        self.option10.setGeometry(QtCore.QRect(0 * multiplier, 230 * multiplier, 151 * multiplier, 30 * multiplier))
        self.option10.setObjectName("option10")
        self.option15 = QtWidgets.QPushButton(self.centralwidget)
        self.option15.setGeometry(QtCore.QRect(301 * multiplier, 260 * multiplier, 150 * multiplier, 30 * multiplier))
        self.option15.setObjectName("option15")
        self.option14 = QtWidgets.QPushButton(self.centralwidget)
        self.option14.setEnabled(True)
        self.option14.setGeometry(QtCore.QRect(151 * multiplier, 260 * multiplier, 150 * multiplier, 30 * multiplier))
        self.option14.setObjectName("option14")
        self.option13 = QtWidgets.QPushButton(self.centralwidget)
        self.option13.setGeometry(QtCore.QRect(0 * multiplier, 260 * multiplier, 151 * multiplier, 30 * multiplier))
        self.option13.setObjectName("option13")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setEnabled(True)
        self.image.setGeometry(QtCore.QRect(0 * multiplier, 0 * multiplier, 191 * multiplier, 141 * multiplier))
        self.image.setObjectName("image")
        self.image.setScaledContents(True)
        #self.image.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(192 * multiplier, 0 * multiplier, 251 * multiplier, 141 * multiplier))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignCenter|QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.skip = QtWidgets.QPushButton(self.centralwidget)
        self.skip.setGeometry(QtCore.QRect(241 * multiplier, 131 * multiplier, 10 * multiplier, 10 * multiplier))
        self.skip.setObjectName("skip")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.option8.setText(_translate("MainWindow", "PushButton"))
        self.option1.setText(_translate("MainWindow", "PushButton"))
        self.option2.setText(_translate("MainWindow", "PushButton"))
        self.option3.setText(_translate("MainWindow", "PushButton"))
        self.option4.setText(_translate("MainWindow", "PushButton"))
        self.option6.setText(_translate("MainWindow", "PushButton"))
        self.option9.setText(_translate("MainWindow", "PushButton"))
        self.option5.setText(_translate("MainWindow", "PushButton"))
        self.option7.setText(_translate("MainWindow", "PushButton"))
        self.option12.setText(_translate("MainWindow", "PushButton"))
        self.option11.setText(_translate("MainWindow", "PushButton"))
        self.option10.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.skip.setText(_translate("MainWindow", "skip"))

_window = QtWidgets.QMainWindow()
_window.show()
window = Ui_MainWindow()
window.setupUi(_window)
window.retranslateUi(_window)
_window.setWindowIcon(QtGui.QIcon("./assets/icon.png"))
_window.setWindowIconText("The Catmeme Timeline")
_window.setWindowTitle("The Catmeme Timeline")
_window.setStyleSheet("background-color:#121212;");
_translate = QtCore.QCoreApplication.translate
window.label.setStyleSheet("color:#BCBCBC")
window.skip.setEnabled = True
window.label.setText("")

def openWindow():
    app.exec()

twindow = threading.Thread(target=openWindow)
twindow.daemon = True
twindow.start()
evt = threading.Event()


# ! Endings
Endings = {
    0: "Oblivious",
    1: "Betrayal",
    2: "Backrooms",
    3: "Eternal Vibes",
    4: "Eternal Advertisment",
    5: "Ascention",
    6: "Catgirl",
    7: "Bingus",
    8: "Burial",
    9: "Afterlife",
    10: "Doom",
    11: "Profit",
    12: "Burger King",
    13: "Catgirl 2",
    14: "Rat",
    15: "Half Life",
    16: "Filler Episode",
    17: "Cheezit",
    18: "Minecraft",
    19: "Jail",
    20: "Smol Cat",
    21: "Slap Slap",
    22: "Watermelon",
    23: "Suffering",
    24: "Nothingness",
    25: "Matrix",
    26: "Bad",
    27: "Neutral",
    28: "Infinite Pain",
    29: "Good",
    #Items
    "secondbomb": "Died From Second Bomb",
    "tcb": "tcb",
    "tc1": "tc1",
    "tc2": "tc2",
    "tc3": "tc3",
    "dcat": "dcat",
    "tc": "tall cates gotten",
    "glumbosummon": "glumbosummon",
    "heavenunlocked": "heavenunlocked",
    "voidunlocked": "voidunlocked",
    "catgirl1got": "catgirl1got",
    "book": "Book"
}

unlockableStuff = [
    ["tc", ["tc1", "tc2", "tc3", "tcb"]],
    ["catgirl1got", [6]],
    ["glumbosummon", [19, "secondbomb", 23, 20]],
    ["heavenunlocked", [5]],
    ["voidunlocked", [3, 4]]
]




chapter1 = [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, "secondbomb"]
chapter2 = [4, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
filler = (chapter1 + chapter2)
filler.remove(28)
filler.remove(29)

Buttons = {
    1: window.option1,
    2: window.option2,
    3: window.option3,
    4: window.option4,
    5: window.option5,
    6: window.option6,
    7: window.option7,
    8: window.option8,
    9: window.option9,
    10: window.option10,
    11: window.option11,
    12: window.option12,
    13: window.option13,
    14: window.option14,
    15: window.option15
}

for button in Buttons:
    Buttons[button].setStyleSheet("background-color:#212121; border-color: beige; font: 15px; color:#BCBCBC")
    Buttons[button].setEnabled(False)
    Buttons[button].setText("")

window.label.setStyleSheet("font: 12px; color:#BCBCBC;")

try:
    cEndings = pickle.load(open("./EndingsComplete.p", "rb"))
except:
    cEndings = []




# ! General Functions

def setButtonState(button, state):
    if state == True:
        button.setStyleSheet("background-color:#212121; border-color: beige; font: 15px; color:#BCBCBC")
    elif state == False:
        button.setStyleSheet("background-color:#2B1E1E; border-color: beige; font: 15px; color:#BCBCBC")


def clear():
    window.label.setText("")

def printn(text, delay = 0.04):
    QtCore.QCoreApplication.processEvents()
    labeltext = window.label.text()
    printed_text = window.label.text() + "\n"
    for letter in text:
        if gameinfo.isSkipped == True:
            return True
        time.sleep(delay)
        printed_text = printed_text + letter
        window.label.setText(printed_text)
        QtCore.QCoreApplication.processEvents()
    window.label.setText(printed_text)
    return False

def printf(text, delay = 0.04, image="x"):
    rtext = text
    labeltext = window.label.text()
    if image != "x":
        pixmap = QtGui.QPixmap("./assets/" + image + ".png")
        window.image.setPixmap(QtGui.QPixmap.scaled(pixmap, pixmap.size().width(), pixmap.size().height(), QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation))
    ftext = text.split("\n")
    for text in ftext:
        isSkippeda = printn(text, delay)
        if isSkippeda == True:
            window.label.setText(labeltext + "\n" + rtext)
            gameinfo.isSkipped = False
            return

def randomf(list):
    a = random.randrange(0, len(list))
    return list[a]

def unPause():
    if gameinfo.gamePaused == True:
        QtCore.QCoreApplication.processEvents()
        gameinfo.gamePaused = False

def skip():
    gameinfo.isSkipped = True

window.skip.clicked.connect(skip)
def waitForValueChange():
    while gameinfo.gamePaused == True:
        time.sleep(0.1)
    evt.set()

def toEndingsComplete(array):
    endings = []
    for item in array:
        endings.append(Endings[item])
    return endings

Buttons[1].clicked.connect(unPause)

def pause():
    QtCore.QCoreApplication.processEvents()
    Buttons[1].setEnabled(True)
    Buttons[1].setText("Continue")
    gameinfo.gamePaused = True
    t = threading.Thread(target=waitForValueChange)
    t.daemon = True
    t.start()
    while t.is_alive():
        QtCore.QCoreApplication.processEvents()
    window.label.setText("")
    Buttons[1].setText("")
    Buttons[1].setEnabled(False)
    pixmap = QtGui.QPixmap("./assets/" + "waiting.jpg")
    window.image.setPixmap(QtGui.QPixmap.scaled(pixmap, pixmap.size().width(), pixmap.size().height(), QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation))


def giveOption(nr):
    if gameinfo.inDecision == True:
        gameinfo.inDecision = False
        gameinfo.decisionNr = nr - 1
    print(str(nr-1))

Buttons[1].clicked.connect(lambda: giveOption(1))
Buttons[2].clicked.connect(lambda: giveOption(2))
Buttons[3].clicked.connect(lambda: giveOption(3))
Buttons[4].clicked.connect(lambda: giveOption(4))
Buttons[5].clicked.connect(lambda: giveOption(5))
Buttons[6].clicked.connect(lambda: giveOption(6))
Buttons[7].clicked.connect(lambda: giveOption(7))
Buttons[8].clicked.connect(lambda: giveOption(8))
Buttons[9].clicked.connect(lambda: giveOption(9))
Buttons[10].clicked.connect(lambda: giveOption(10))
Buttons[11].clicked.connect(lambda: giveOption(11))
Buttons[12].clicked.connect(lambda: giveOption(12))
Buttons[13].clicked.connect(lambda: giveOption(13))
Buttons[14].clicked.connect(lambda: giveOption(14))
Buttons[15].clicked.connect(lambda: giveOption(15))

def option(options, requirements, hideRequirements = True):
    i = -1
    finalOptions = []
    for option in options:
        i = i + 1
        if requirements[i] == "x":
            Buttons[i + 1].setText(option)
            Buttons[i + 1].setEnabled(True)
            finalOptions.append(i)
        else:
            reqNeeded = len(requirements[i])
            reqMet = 0
            for requirement in requirements[i]:
                if hideRequirements:
                    if Endings[requirement] in cEndings:
                        reqMet = reqMet + 1
                    else:
                        pass
                else:
                    if Endings[requirement] in cEndings:
                        reqMet = reqMet + 1
                    else:
                        pass
            if reqMet == reqNeeded:
                Buttons[i + 1].setText(option)
                Buttons[i + 1].setEnabled(True)
                finalOptions.append(i)
            else:
                Buttons[i + 1].setText(option)
                setButtonState(Buttons[i+1], False)
    Buttons[15].setText("Exit")
    Buttons[15].setEnabled(True)
    finalOptions.append(len(options))

    gameinfo.inDecision = True
    while gameinfo.inDecision == True:
        QtCore.QCoreApplication.processEvents()
    selected = gameinfo.decisionNr
    gameinfo.decisionNr = 'x'

    if selected == 14:
        exit()
    for button in Buttons:
        Buttons[button].setEnabled(False)
        setButtonState(Buttons[button], True)
        Buttons[button].setText("")
    clear()
    return selected

def getEnding(nr):
    if Endings[nr] in cEndings:
        pass
    else:
        cEndings.append(Endings[nr])
    pickle.dump(cEndings, open("./EndingsComplete.p", "wb"))


# * Story Parts (they can be reused)
def CS_DCat():
    printf("...", 1, image="")
    printf("In the realm of the Unknown, outside of all\npossible timelines, the Demon Cat is awoken due\nto the many cosmic endings.", image="demoncat")
    pause()
    if all(elem in cEndings for elem in toEndingsComplete([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27])):
        printf("me petting my cat as we study various\ntimelines to not make the same mistakes\n(it is very confusing to us)", image="timelines")
        time.sleep(1)
        printf("\nWhen every single filler ending is reached,\nwe gain a full understanding of the extended timeline\nof the multiverses. We use this knowledge in\nan attempt to defeat the Demon Cat.", image="timelines")
        pause()
        printf("The Demon Cat summons all of the\ncosmic beings left in existence.\nThis is the final battle.\nThe batlle that decides the Universes Fate.", image="demoncat2")
        pause()
        printf("There is one filler ending that has\npotential to defeat the Demon Cat.\nBut which one is is it?", image="timelimes")
        sel = option(["Minecraft Ending", "Oblivious Ending", "Half Life Ending", "Bingus Ending", "Cheezit Ending", "Burger King Ending", "Doom Ending", "Slap Slap Ending", "Cat Girl Ending", "Profit Ending", "Burial Ending", "Afterlife Ending", "Betrayal Ending", "Watermelon Ending"], ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"])
        if sel == 4:
            printf("The immovable cheezit cat is chosen to go up\nagainst the demon cat and its subordonates. Because\nthe cat is immovable, literally nothing phases him. After\nan eternity of the cosmic cats trying to damage the\ncheezit cat, their cosmic energy runs thin and they fade\nout of existence. Order is restored in the universe.", image="cheezit")
            printf("Good Ending", 0.2)
            getEnding("dcat")
            getEnding(29)
            pause()
        else:
            printf("The Demon Cat wins the battle and is now in control\nover the entire universe forever. Everything that exists is now\nreplaces with pain and suffering. Everything good\nto ever exist is now removed.", image="demoncat2")
            printf("Infinite Pain Ending", 0.2)
            getEnding(28)
            getEnding("dcat")
            pause()
    else:
        printf("But it seems... as though...\nyou are not powerful enough.\nYou need to understand all the timelines for this battle.\nCome back next time.")
        getEnding("dcat")
        pause()

def CS_USDies():
    printf("US Government dismantled", image="usdies")
    pause()
    printf("Entre world government collapses,\nanarchy ensues", image="anarchy")
    pause()
    printf("Angel Cat comes down from heaven to\nbestow upon the physical world the presence\nof the goldy being Glumbo in an attempt to\nrestore order to the world.", image="angelcat")
    sel = option(["summon glumbo", "collapse into anarchy"], [[19, "secondbomb", 23, 20], "x"])
    if sel == 0:
        printf("Glumbo is created, and transcends time itself.\nGlumbo is hungry for power and escapes the grip\nof god to torment the many timelines.", image="glumbo1")
        pause()
        printf("ALTERING JAIL ENDING")
        printf("Glumbo breaks the jailed cat out\nand converts him into a Glumbo Subordonate", image="glumbo2")
        pause()
        printf("ALTERING SECOND BOMB ENDING")
        printf("The pain from the second bomb is converted into cosmic energy and turns this cat into the Glumbo Chile", image="glumbo3")
        pause()
        printf("ALTERING SUFFERING ENDING")
        printf("Glumbo Chile uses this pent up rage\nand pain to turn him into a master\nof psychological manipulation", image="glumbo4")
        pause()
        printf("ALTERING SMOL CAT ENDING")
        printf("Glumbo turns smol cat into Tall Cate,\nwhich becomes a cosmic beast that\nneeds to be defeated.", image="tallcate")
        pause()
        printf("The godly being D Cat is awoken\nfrom his slumber to slay the tall cate", image="dcat")
        pause()
        printf("D cat loses his life in battle but\nstill succeeds in his goal.\nBecomes the deceased r cat.", image="rcat")
        pause()
        printf("The Tall Cate was split into three\npieces scattered across time itself,\nwaiting to be rebuilt.", image="tallcate-pieces")
        getEnding("tcb")
        sel = option(["go back in time to search", "rebuild tall cate"], ["x", ["tc1", "tc2", "tc3"]])
        if sel == 0:
            printf("Good luck, hero.")
            pause()
        elif sel == 1:
            printf("The Three Pieces of the Tall Cate were \nlocated by the Glumbo Subordonate and the\nTall Cate is rebuilt.", image="tallcate")
            pause()
            printf("With the legendary D Cat taken out, \nthe God Cat himself needs to take matters\ninto his own hands.", image="godcat")
            pause()
            printf("The Battle of the Gods Commences", image="battleofgods")
            printf("Tall Cate, Butternut, Glumbo Subordonate, Glumbo Chile,\nand Glumbo himself combine their powers\nin an attempt to kill God himself and take control\nover the universe for themselves.")
            sel = option(["Glumbo Wins", "God Cat Wins"], ["x", "x"])
            if sel == 0:
                printf("God cat is overpowered by these many beasts, and\nButternut seized the opportunity to psychologically manipulate\ngod cat into handing them control over the universe.\nGod cat is then killed by Glumbo himself.", image="glumbo1")
                printf(" \nGlumbo and his subordonates are now\nthe rulers of the universe.")
                printf("Bad Ending", 0.2)
                getEnding(26)
                pause()
            elif sel == 1:
                printf("God cat defeats the beasts in an\nepic battle but losees his control over\nthe universe in the process. A new\nruler needs to be chosen.", image="cate")
                printf(" \nCate is chosen as the new ruler.")
                printf("Netural Ending", 0.2)
                getEnding(27)
                pause()
    elif sel == 1:
        printf("Entire world collapses into anarchy.", image="anarchy")
        pause()
def CS_Chilling():
    printf("casually chilling", image="chilling")
    sel = option(["check on smol cat", "act silly", "check on floppa", "wait its my brithday today", "advertise food and drinks"], ["x", "x", "x", "x", "x"])
    if sel == 0:
        printf("smol cat chilling too", image="smolcat")
        printf("Smol Cat Ending", 0.1)
        getEnding(20)
        pause()
    elif sel == 1:
        printf("cat acts a little silly", image="silly1")
        pause()
        printf("cat makes funny noise", image="silly2")
        printf("Slap Slap Ending", 0.1)
        getEnding(21)   
        pause()
    elif sel == 2:
        printf("floppa kinda chilling too ngl", image="floppa1")
        pause()
        printf("Big Floppa offers you a watermelon.\nWill you accept this?", image="floppa2")
        sel = option(["YES", "commit war crimes against Serbia"], ["x", "x"])
        if sel == 0:
            printf("Watermelon is accepted.\nCat Eats watermelon and becomes watermelon itself.\nLays here for eternity.", image="watermelon")
            printf("Watermelon Ending", 0.1)
            getEnding(22)
            pause()
        elif sel == 1:
            CS_USDies()
    elif sel == 3:
        printf("Cat has birthday party but nobody goes\nso he's sad :(", image="bday1")
        pause()
        printf("LOOK ME IN THE EYES.\nDO YOU FEEL IT? THE MADNESS CONSUMING\nYOUR MIND. THE UTTER DESPAIR\nIN THE FACE OF THE INEVITABLE!!", image="bday2")
        printf("Cat goes down the path of perpetual torment.")
        printf("Suffering Ending", 0.1)
        getEnding(23)
        pause()
    elif sel == 4:
        printf("Cats Advertising food/drinks products dimension reached.", image="eternaladv")
        printf("Eternal Advertisment Ending", 0.1)
        getEnding(4)
        pause()


def CS_Caught():
    printf("gets caught, sent to jail\nfree him?", image="jail1")
    sel = option(["yes", "no"], ["x", "x"])
    if sel == 0:
        CS_Chilling()
    elif sel == 1:
        printf("final chance at escape\nfree him?", image="jail2")
        sel = option(["yes", "no"], ["x", "x"])
        if sel == 0:
            CS_Chilling()
        elif sel == 1:
            printf("Cat stuck in jail forever.", image="jail3")
            printf("Jail Ending", 0.1)
            getEnding(19)
            pause()


def CS_Afterlife():
    printf("me petting my cat in the afterlife\n(we perished lol)", image="afterlife")
    sel = option(["Heaven", "Hell"], [[5], "x"], False)
    if sel == 0:
        printf("me petting my cat after we passed on\n(we were reunited in the afterlife)", image="heaven")
        printf("\nCat and author lived a good life\nand made it to heaven together")
        printf("Afterlife Ending", 0.1)
        getEnding(9)
        pause()
    elif sel == 1:
        printf("me watching my cat find me in hell\nso he can drag me out\n(he is a very good friend)", image="hell1")
        pause()
        printf("my cat is killing a bunch of people\nhe is the doom slayer", image="hell2")
        printf("\nRip and tear.\nTransitions into Doom Eternal storyline")
        printf("Doom Ending", 0.1)
        getEnding(10)
        pause()
    
def CS_Survival():
    printf("me petting my cat after we survived\nthe nuclear blast\n(we got very lucky)", image="normal")
    sel = option(
        [
            "Wait", # 0
            "Teach how to play bongos", # 1
            "Go to Burger King", # 2
            "Transform to catgirl", # 3
            "parralel universe", # 4
            "Go to Black Mesa", # 5
            "body swapping machine", # 6
            "Vibe", # 7
            "second bomb?!", # 8
            "Buy cheez-its", # 9
            "Play minecraft", # 10
            "drink water", # 11
            "dismantle US government", # 12
            "commit federal crime"  # 13
        ],
        [
            "x",
            "x",
            "x",
            [6],
            "x",
            "x",
            "x",
            "x",
            "x",
            "x",
            "x",
            "x",
            "x",
            "x"
        ]
    )

    if sel == 0:
        printf("slowly society goes back to normal.\nanother bomb is launched and time repeates itself.")
        pause()
    elif sel == 1:
        printf("cat learns how to play bongos", image="bongo")
        pause()
        printf("cat makes 4 dabloons from playing bongos", image="profit")
        printf("Profit Ending", 0.1)
        getEnding(11)
        pause()
    elif sel == 2:
        printf("Me petting my cat after surviving\nthe nuclear attack and celebrating it\nat Burger King\n(he likes burgers)", image="burgerking")
        printf("\nCat and author celebrate their survival\nat the only burger king still in operation.")
        printf("Burger King Ending", 0.1)
        getEnding(12)
        pause()
    elif sel == 3:
        printf("CMON TURN INTO A CATGIRL ALREADY *shakes cat with lots of power*", image="catgirl2")
        printf("\nCat turns into a cat girl.\nCat girls become a normal part of human society.", image="catgirl3")
        printf("Catgirl Ending 2", 0.1)
        getEnding(13)
        pause()
    elif sel == 4:
        printf("Parralel Universe is reached.\nCat is a rat in this universe.", image="rat")
        printf("Rat Ending", 0.1)
        getEnding(14)
        pause()
    elif sel == 5:
        printf("Me petting my cat before the resonance\ncascade disaster\n(we didn't prepare for the unforseen consequences)", image="halflife")
        printf("\nResonance Cascade disaster takes place.\nLeads into Half Life storyline.")
        printf("Half Life Ending", 0.1)
        getEnding(15)
        pause()
    elif sel == 6:
        printf("my cat petting me after we\naccidentally turn on the body swapping machine\n(it's a filler episode)", image="normal")
        printf("\nCat and author swap bodies.")
        printf("Filler Episode Ending", 0.1)
        getEnding(16)
        pause()
    elif sel == 7:
        printf("cat starts vibing...", image="vibe1")
        pause()
        printf("\nCats Vibing Dimension reached.", image="vibe2")
        printf("Eternal Vibes Ending", 0.1)
        getEnding(3)
        pause()
    elif sel == 8:
        printf("nevermind, there was a second bomb\n(we perished with imense pain)", image="pain")
        pause()
        getEnding("secondbomb")
        CS_Afterlife()
    elif sel == 9:
        printf("cat get covered in cheezits. becomes immovable.", image="cheezit")
        printf("\nCheezit Ending", 0.1)
        getEnding(17)
        pause()
    elif sel == 10:
        printf("me petting my cat after he saved\nme from dying of fall damage\n(he transferred his life force to me)", image="minecraft1")
        pause()
        printf("me petting my cat before going\nto then nether because the overworld\nbecomes uninhabitable\n(we are going to miss this house)", image="minecraft2")
        pause()
        printf("me petting my cat after our nether\nportal got destroyed by a ghast\n(i think this is our new home now)", image="minecraft3")
        printf("\nStuck in the nether forever.")
        printf("Minecraft Ending", 0.1)
        getEnding(18)
        pause()
    elif sel == 11:
        printf("Cat starts drinking water", image="water1")
        pause()
        printf("Cat drinks all of DCs water supply\nputting DC in a drought", image="water2")
        printf("President of the US dies from dehydration,\ngovernment collapses into anarchy")
        pause()
        CS_USDies()
    elif sel == 12:
        printf("Cat decides to dismantle US Government\nlet me relax, i will dismantle\nthe US government later...", image='relax')
        sel = option(["succeed", "relax more", "get caught"], ['x', "x", "x"])
        if sel == 0:
            CS_USDies()
        elif sel == 1:
            CS_Chilling()
        elif sel == 2:
            CS_Caught()
    elif sel == 13:
        printf("he is about to commit a federal crime\n(he cannot be stopped)", image="federalcrime")
        sel = option(["do not commit federal crime", "gets caught"], ["x", "x"])
        if sel == 0:
            CS_Chilling()
        elif sel == 1:
            CS_Caught()

# ! MAIN MENU


while True:
    while True:
        printf("The Catmeme Timeline", 0.02)
        sel = option(["Play", "View Unlocked Endings", "Debug"], ["x","x","x"])
        if sel == 0:
            break
        elif sel == 1:
            window.label.setStyleSheet("color: #BCBCBC")
            endingssss = []
            for i in Endings:
                try:
                    lol = i - 1
                    endingssss.append(Endings[i])
                except:
                    pass
            endingsssssss = []
            for ending in cEndings:
                if ending in endingssss:
                    endingsssssss.append(ending)
                    printf(ending + " Ending", 0)
            endingssss = []
            for i in Endings:
                try:
                    lol = i - 1
                    endingssss.append(Endings[i])
                except:
                    pass
            for i in range(0,len(endingssss) - len(endingsssssss)):
                printf("???", 0)
            
            endingssss = []
            for i in Endings:
                try:
                    lol = i - 1
                    endingssss.append(Endings[i])
                except:
                    pass

            printf("Total endings: " + str(len(endingsssssss)) + "/" + str(len(endingssss)))
            pause()
            window.label.setStyleSheet("color:#BCBCBC; font: 12px;")
        elif sel == 2:
            sel = option(["Get Chapter 1 Endings", "Get Chapter 2 Endings", "Get All Filler Endings", "Reset Progress", "Give All Tall Cate Pieces"], ["x", "x", "x", "x", "x"])
            if sel == 0:
                for i in chapter1:
                    getEnding(i)
            elif sel == 1:
                for i in chapter2:
                    getEnding(i)
            elif sel == 2:
                for i in filler:
                    getEnding(i)
            elif sel == 3:
                cEndings = []
                getEnding("book")
            elif sel == 4:
                getEnding("tc1")
                getEnding("tc2")
                getEnding("tc3")








    # ! STORY

    if (all(elem in cEndings for elem in ["Nothingness", "Neutral", "Bad"])) and ("dcat" not in cEndings):
        CS_DCat()
    else:
        printf("THE BEGINNING OF TIME")
        pause()
        newUnlockedEndings = 0
        # * CHECK IF ANY OPTION UNLOCKED
        for check in unlockableStuff:
            print(check)
            i = 0
            req = len(check[1])
            for ending in check[1]:
                print(ending)
                if Endings[ending] in cEndings:
                    i = i + 1

            if i == req:
                if Endings[check[0]] not in cEndings:
                    getEnding(check[0])
                    newUnlockedEndings = newUnlockedEndings + 1
        
        if newUnlockedEndings == 1:
            printf("You hear an option unlocking...", image="unlock")
            pause()
        elif newUnlockedEndings >= 2:
            printf("You hear multiple options unlocking...", image="unlock")
            pause()
        printf("me petting my cat before the wave\nof the nuclear bomb hits us\nits our last moment toghether", image="normal")
        if "dcat" in cEndings:
            sel = option(["Wake up", "Pray", "Get Into Basement", "Die", "No-Clip outta there", "Re-Challenge Demon Cat"], ["x", "x", "x", "x", "x", "x"])
        else:
            sel = option(["Wake up", "Pray", "Get Into Basement", "Die", "No-Clip outta there"], ["x", "x", "x", "x", "x"])
        clear()
        if sel == 0: # Wake up"
            printf("me petting my cat after waking up from a dream\nthinking there was going to be a nuclear blast\n(it was a really scary dream...)", image="normal")
            printf("\nIt was all a dream.", image="normal")
            printf("Oblivious Ending", 0.10, "normal")
            getEnding(0)
            pause()
        elif sel == 1: # Pray
            printf("me petting my cat after the nuclear alert\nturned out to be just a mistake\n(we were very happy and relieved)", image="normal")
            if ("tcb" in cEndings) and ("tc1" not in cEndings):
                sel = option(["Check my cat", "Pet my cat", "Obtain Tall Cate Piece 1"], ["x", "x", "x"])
            else:
                sel = option(["Check my cat", "Pet my cat"], ["x", "x"])
            clear()
            if sel == 0: # Check
                printf("me petting my", image="bomb")
                printf("nuclear bomb", 0.10, image="bomb")
                printf("\nThe cat itself turns out to be the nuclear bomb.", image="bomb")
                printf("Betrayal Ending", 0.10, "bomb")
                getEnding(1)
                pause()
            elif sel == 1: # Pet
                CS_Survival()
            elif sel == 2:
                printf("Tall Cate piece 1 retrieved.", image="tallcate-piece1")
                getEnding("tc1")
                pause()
        elif sel == 2: # Get into basement
            printf("We both survive the nuclear blast")
            pause()
            printf("me petting my cat as we slowly succumb to radiation\nsickness from the fallout of the nuclear bomb\n(very painful)", image="radiation")
            sel = option(["Try to find medication", "Go to government that treats survivors", "Do nothing about it"], ["x","x","x"])
            if sel == 0: # Try to find medication
                printf("me petting my cat after finding a nearby,\nbarely functioning hospital that had\nmedication to treat our radiation sickness\n(god bless)", image="normal")
                pause()
                printf("me petting my cat after finding a group\nof survivors who let us join them\n(very kind)", image="normal")
                pause()
                CS_Survival()
            elif sel == 1: # Government
                printf("me petting my cat after receiving\n radiation treatment from the government response team\n(we have major burns and likely some form of cancer)", image="government")
                sel = option(["Cure completely", "Cure", "Sactrifice yourself", "The Cure Dosen't Work"], ["x","x","x","x"])
                if sel == 0: # Cure
                    printf("radiation cured completely")
                    pause()
                    CS_Survival()
                elif sel == 1: # cure bingus
                    printf("radiation cured")
                    printf("me petting my cat after his radiation\ncancer was cured \n(he's hairless now but i still love him)", image="bingus")
                    printf("\nCat becomes a popular meme online.")
                    printf("Bingus Ending", 0.1)
                    getEnding(7)
                    pause()
                elif sel == 2:
                    printf("my cat laying me to my last rest\n(i could save her but not myself)", image="burial")
                    printf("\nThe author dies from cancer, but the cat lives on.")
                    printf("Burial Ending", 0.1)
                    getEnding(8)
                    pause()
                elif sel == 3:
                    printf("we both die from cancer")
                    pause()
                    CS_Afterlife()
            elif sel == 2: # Nothing
                printf("me petting my cat while we are getting\nmutated thanks to the radiation of the\nnuclear bomb.\n(we are becoming horrors)", image="mutation")
                if ("tcb" in cEndings) and ("tc2" not in cEndings):
                    sel = option(["Leave the cat be", "Stay next to it and pet it", "Obtain Tall Cate piece 2"], ["x", "x", "x"])
                else:
                    sel = option(["Leave the cat be", "Stay next to it and pet it"], ["x", "x"])
                if sel == 0:
                    printf("me beholding my cat as the radiation\nfrom the blast causes it to mutate and attain\ngod-like power.\n(it will be merciful to me as i have shown\nit compassion in it's former state of being", image="ascention")
                    printf("\nCat mutates into a demi-god. Shows\nthe author mercy because of our previous bond.")
                    printf("Ascention Ending", 0.1)
                    getEnding(5)
                    pause()
                elif sel == 1:
                    printf("me after i fused with my cat due\nto the radiation\n(it was very painful)", image="catgirl1")
                    printf("\nAuthor and cat fuse toghether \nand becomes a cat girl maid.\nCat girls become a normal part of society.")
                    printf("Cat Girl Ending", 0.1)
                    getEnding(6)
                    pause()
                elif sel == 2:
                    getEnding("tc2")
                    printf("Tall Cate Piece 2 retrieved", image="tallcate-piece2")
                    pause()
        elif sel == 3: # Die
            printf("We both die from the nuclear blast")
            pause()
            CS_Afterlife()
        elif sel == 4: # Noclip outta there
            printf("Me petting my cat after we no-clipped out of reality\nto get away from the nuclear blast\n(this place seems familliar)", image="backrooms")
            sel = option(["Stay here and cry", "Go further"], ["x", [3, 4]])
            clear()
            if sel == 0:
                printf("Author and cat are stuck in the backrooms dimension forever.", image="backrooms")
                printf("\nBackrooms Ending", 0.1)
                getEnding(2)
                pause()
            elif sel == 1:
                printf("Noclip dimension, cats with snacks/drinks dimension\nand cats vibing dimension coexist,\ncreating a dimensional rift, sending you to the void.")
                pause()
                for i in range(0, 5):
                    printf("me petting my cat in the void", image="void")
                    pause()
                printf("me peting my cat in the void")
                if ("tcb" in cEndings) and ("tc3" not in cEndings):
                    sel = option(["Continue", "THIS HAS TO STOP!", "Obtain tall cate piece 3"], ["x", "x", "x"])
                else:
                    sel = option(["Continue", "THIS HAS TO STOP!"], ["x", "x"])
                if sel == 0:
                    printf("After an eternity in the void, a powerful\nsurge of energy is felt.", image="surge")
                    pause()
                    printf("The cracks in the simulation begin to show.", image="polycat")
                    pause()
                    printf("me petting my cat as the simulation shuts down\n(we will both be erased from existence)", image="simulation")
                    printf("Simulation shuts down, existence is erased.")
                    printf("Nothingness Ending", 0.1)
                    getEnding(24)
                    pause()
                elif sel == 1:
                    printf("The ceiling cat, as the only mortal\nbeing that can traverse the backrooms breaks\nyou out of the void", image="ceilingcat")
                    pause()
                    printf("Do you return to the fake reality with\nthe blue pill, or escape the matrix\nand learn the truth with the red pill?", image="matrix")
                    sel = option(["blue pill", "red pill"], ["x", "x"])
                    if sel == 0:
                        printf("you return to the beginning...")
                        pause()
                    elif sel == 1:
                        printf("You escaped the simulation.\nTransitions into the Matrix storyline.")
                        printf("Matrix Ending", 0.1)
                        getEnding(25)
                        pause()
                elif sel == 2:
                    getEnding("tc3")
                    printf("Tall Cate piece 3 retrieved.", image="tallcate-piece3")
                    pause()
        elif sel == 5:
            CS_DCat()