
import os
import sys
import random
from enum import Enum
from typing import runtime_checkable
import simpleaudio as sa
import time
import pickle
import tabulate



# ! Endings
Endings = {
    0: "Oblivious",
    1: "Betrayal",
    2: "Backrooms",
    3: "Eternal Vibes",
    #4: "Advertisment",
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
    18: "Minecraft"
}
unontainable = ["Advertisement"]



try:
    cEndings = pickle.load(open("./EndingsComplete.p", "rb"))
except:
    cEndings = []


# ! General Functions

def clear():
    os.system("cls")

def printf(text, delay = 0.04):
    ftext = text.split("\n")
    for text in ftext:
        printed_text = ""
        for letter in text:
            time.sleep(delay)
            printed_text = printed_text + letter
            print(printed_text, end="\r")
        print(printed_text)

def randomf(list):
    a = random.randrange(0, len(list))
    return list[a]

def pause():
    for i in range(0,10):
        os.system("echo | set /p=\" \"")
    os.system("Pause >nul | echo | set /p=\">\"")
    print("\n")
    os.system("cls")
    print("\n")

def option(options, requirements, hideRequirements = True):
    i = -1
    finalOptions = []
    for option in options:
        i = i + 1
        if requirements[i] == "x":
            print(str(i) + " - " + option)
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
                print(str(i) + " - " + option)
                finalOptions.append(i)
            else:
                print(str(i) + " - " + option + " [LOCKED]")
                reqNeeded = len(requirements[i])
                reqMet = 0
                for requirement in requirements[i]:
                    if hideRequirements:
                        if Endings[requirement] in cEndings:
                            print("  " + Endings[requirement] + " - COMPLETE")
                            reqMet = reqMet + 1
                        else:
                            print("  " + "???")
                    else:
                        if Endings[requirement] in cEndings:
                            print("  " + Endings[requirement] + " - COMPLETE")
                            reqMet = reqMet + 1
                        else:
                            print("  " + Endings[requirement])
                if reqMet == reqNeeded:
                    finalOptions.append(i)
    print(str(len(options)) + " - " + "Exit")
    finalOptions.append(len(options))
    while True:
        try:
            selected = int(input(" > "))
            if selected in finalOptions:
                break
            else:
                pass
        except:
            pass

    if selected == len(options):
        exit()
    clear()
    return selected

def getEnding(nr):
    if Endings[nr] in cEndings:
        pass
    else:
        cEndings.append(Endings[nr])
    pickle.dump(cEndings, open("./EndingsComplete.p", "wb"))

# * Story Parts (they can be reused)


def CS_Afterlife():
    printf("me petting my cat in the afterlife\n(we perished lol)")
    sel = option(["Heaven", "Hell"], [[5], "x"], False)
    if sel == 0:
        printf("me petting my cat after we passed on\n(we were reunited in the afterlife)")
        printf("\nCat and author lived a good life\nand made it to heaven together")
        printf("Afterlife Ending", 0.1)
        getEnding(9)
        pause()
    elif sel == 1:
        printf("me watching my cat find me in hell\nso he can drag me out\n(he is a very good friend)")
        pause()
        printf("my cat is killing a bunch of people\nhe is the doom slayer")
        printf("\nRip and tear.\nTransitions into Doom Eternal storyline")
        printf("Doom Ending", 0.1)
        getEnding(10)
        pause()
    
def CS_Survival():
    printf("me petting my cat after we survived\nthe nuclear blast\n(we got very lucky)")
    sel = option(
        [
            "Wait", # 0
            "Teach how to play bongos", # 1
            "Go to Burger King", # 2
            "Transform to catgirl", # 3
            "Squeeze into parralel universe", # 4
            "Go to Black Mesa", # 5
            "Look at body swapping machine", # 6
            "Vibe", # 7
            "wait there was actually a second bomb", # 8
            "Buy cheez-its", # 9
            "Play minecraft" # 10
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
            "x"
        ]
    )

    if sel == 0:
        printf("slowly society goes back to normal.\nanother bomb is launched and time repeates itself.")
        pause()
    elif sel == 1:
        printf("cat learns how to play bongos")
        pause()
        printf("cat makes 4 dabloons from playing bongos")
        printf("Profit Ending", 0.1)
        getEnding(11)
        pause()
    elif sel == 2:
        printf("Me petting my cat after surviving\nthe nuclear attack and celebrating it\nat Burger King\n(he likes burgers)")
        printf("\nCat and author celebrate their survival\nat the only burger king still in operation.")
        printf("Burger King Ending", 0.1)
        getEnding(12)
        pause()
    elif sel == 3:
        printf("CMON TURN INTO A CATGIRL ALREADY *shakes cat with lots of power*")
        printf("\nCat turns into a cat girl.\nCat girls become a normal part of human society.")
        printf("Catgirl Ending 2", 0.1)
        getEnding(13)
        pause()
    elif sel == 4:
        printf("Parralel Universe is reached.\nCat is a rat in this universe.")
        printf("Rat Ending", 0.1)
        getEnding(14)
        pause()
    elif sel == 5:
        printf("Me petting my cat before the resonance\ncascade disaster\n(we didn't prepare for the unforseen consequences)")
        printf("\nResonance Cascade disaster takes place.\nLeads into Half Life storyline.")
        printf("Half Life Ending", 0.1)
        getEnding(15)
        pause()
    elif sel == 6:
        printf("my cat petting me after we\naccidentally turn on the body swapping machine\n(it's a filler episode)")
        printf("\nCat and author swap bodies.")
        printf("Filler Episode Ending", 0.1)
        getEnding(16)
        pause()
    elif sel == 7:
        printf("cat starts vibing...")
        printf("\nCats Vibing Dimension reached.")
        printf("Eternal Vibes Ending", 0.1)
        getEnding(3)
        pause()
    elif sel == 8:
        printf("nevermind, there was a second bomb\n(we perished with imense pain)")
        pause()
        CS_Afterlife()
    elif sel == 9:
        printf("cat get covered in cheezits. becomes immovable.")
        printf("\nCheezit Ending", 0.1)
        getEnding(17)
        pause()
    elif sel == 10:
        printf("me petting my cat after he saved\nme from dying of fall damage\n(he transferred his life force to me)")
        pause()
        printf("me petting my cat before going\nto then nether because the overworld\nbecomes uninhabitable\n(we are going to miss this house)")
        pause()
        printf("me petting my cat after our nether\nportal got destroyed by a ghast\n(i think this is our new home now)")
        printf("\nStuck in the nether forever.")
        printf("Minecraft Ending", 0.1)
        getEnding(18)
        pause()

# ! MAIN MENU



while True:
    printf("The Catmeme Timeline", 0.02)
    sel = option(["Play", "View Unlocked Endings"], ["x","x","x"])
    if sel == 0:
        break
    elif sel == 1:
        printf("Endings:")
        for ending in cEndings:
            print("   " + ending + " Ending")
        endingssss = []
        for i in Endings:
            endingssss.append(Endings[i])
        for i in range(0,len(endingssss) - len(cEndings)):
            print("   ???")
        
        endingssss = []
        for i in Endings:
            endingssss.append(Endings[i])

        printf("Total endings: " + str(len(cEndings)) + "/" + str(len(endingssss)))
        pause()









# ! STORY

printf("THE BEGINNING OF TIME")
pause()
printf("me petting my cat before the wave")
printf("of the nuclear bomb hits us")
printf("its our last moment toghether")
sel = option(["Wake up", "Pray", "Get Into Basement", "Die", "No-Clip outta there"], ["x", "x", "x", "x", "x"])
clear()
if sel == 0: # Wake up
    printf("me petting my cat after waking up from a dream\nthinking there was going to be a nuclear blast\n(it was a really scary dream...)")
    printf("\nIt was all a dream.")
    printf("Oblivious Ending", 0.10)
    getEnding(0)
    pause()
elif sel == 1: # Pray
    printf("me petting my cat after the nuclear alert\nturned out to be just a mistake\n(we were very happy and relieved)")
    sel = option(["Check my cat", "Pet my cat"], ["x", "x"])
    clear()
    if sel == 0: # Check
        printf("me petting my")
        printf("nuclear bomb", 0.10)
        printf("\nThe cat itself turns out to be the nuclear bomb.")
        printf("Betrayal Ending", 0.10)
        getEnding(1)
        pause()
    elif sel == 1: # Pet
        CS_Survival()
elif sel == 2: # Get into basement
    printf("We both survive the nuclear blast")
    pause()
    printf("me petting my cat as we slowly succumb to radiation\nsickness from the fallout of the nuclear bomb\n(very painful)")
    sel = option(["Try to find medication", "Go to government that treats survivors", "Do nothing about it"], ["x","x","x"])
    if sel == 0: # Try to find medication
        printf("me petting my cat after finding a nearby,\nbarely functioning hospital that had\nmedication to treat our radiation sickness\n(god bless)")
        pause()
        printf("me petting my cat after finding a group\nof survivors who let us join them\n(very kind)")
        pause()
        CS_Survival()
    elif sel == 1: # Government
        printf("me petting my cat after receiving\n radiation treatment from the government response team\n(we have major burns and likely some form of cancer)")
        sel = option(["Cure completely", "Cure", "Sactrifice yourself", "The Cure Dosen't Work"], ["x","x","x","x"])
        if sel == 0: # Cure
            printf("radiation cured completely")
            pause()
            CS_Survival()
        elif sel == 1: # cure bingus
            printf("radiation cured")
            printf("me petting my cat after his radiation\ncancer was cured \n(he's hairless now but i still love him)")
            printf("\nCat becomes a popular meme online.")
            printf("Bingus Ending", 0.1)
            getEnding(7)
            pause()
        elif sel == 2:
            printf("my cat laying me to my last rest\n(i could save her but not myself)")
            printf("\nThe author dies from cancer, but the cat lives on.")
            printf("Burial Ending", 0.1)
            getEnding(8)
            pause()
        elif sel == 3:
            printf("we both die from cancer")
            pause()
            CS_Afterlife()
    elif sel == 2: # Nothing
        printf("me petting my cat while we are getting\nmutated thanks to the radiation of the\nnuclear bomb.\n(we are becoming horrors)")
        sel = option(["Leave the cat be", "Stay next to it and pet it"], ["x", "x"])
        if sel == 0:
            printf("me beholding my cat as the radiation\nfrom the blast causes it to mutate and attain\ngod-like power.\n(it will be merciful to me as i have shown\nit compassion in it's former state of being")
            printf("\nCat mutates into a demi-god. Shows\nthe author mercy because of our previous bond.")
            printf("Ascention Ending", 0.1)
            getEnding(5)
            pause()
        elif sel == 1:
            printf("me after i fused with my cat due\nto the radiation\n(it was very painful)")
            printf("\nAuthor and cat fuse toghether \nand becomes a cat girl maid.\nCat girls become a normal part of society.")
            printf("Cat Girl Ending", 0.1)
            getEnding(6)
            pause()
elif sel == 3: # Die
    printf("We both die from the nuclear blast")
    pause()
    CS_Afterlife()
elif sel == 4: # Noclip outta there
    printf("Me petting my cat after we no-clipped out of reality\nto get away from the nuclear blast\n(this place seems familliar)")
    sel = option(["Stay here and cry", "Go further"], ["x", [3]])
    clear()
    if sel == 0:
        printf("Author and cat are stuck in the backrooms dimension forever.")
        printf("\nBackrooms Ending", 0.1)
        getEnding(2)
        pause()
    elif sel == 1:
        printf("to be continued...")
        pause()


