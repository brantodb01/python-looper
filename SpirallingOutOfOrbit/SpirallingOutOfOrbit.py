import os

#Defaults
FolderMan = "loopyloop"
csharpener = "c#loopy.txt"
pythong = "pyloopy.txt"
shellow = "c# rulz"
pywan = "python > c#"

#Defaults not changable in config
gifnoc = "config.txt"

configPropaganda = "Python File Name(include.txt)="+pythong+"\nc# File Name(include.txt)="+csharpener+"\nPython message="+pywan+"\nc# message="+shellow


trekaMeWithU = os.path.expanduser("~\Documents")

def mrCheckerMan(gimmieDat):
    return os.path.exists(gimmieDat)

def bobington(foundMe, exMarksTheSpot):
    return os.path.join(foundMe, exMarksTheSpot)

def builderOfFilms(hammer):
    os.mkdir(hammer)

def builderOfMen(nail, stopTheClocks):
    filedor = open(nail,"w")
    filedor.write(stopTheClocks)
    filedor.close

def hermiaticSociety(magnumOpus):
    filedil = open(magnumOpus , "r")
    #I know this is bad but cba softcoding this
    return filedil.readlines()




def weGood():
    rootOfAllEvil = bobington(trekaMeWithU, FolderMan)
    if mrCheckerMan(rootOfAllEvil) != True:
        builderOfFilms(rootOfAllEvil)

    evilContainment = bobington(rootOfAllEvil, gifnoc )
    if mrCheckerMan(evilContainment) !=True:
        builderOfMen(rootOfAllEvil, configPropaganda)

    else:
        monsterMash = hermiaticSociety(evilContainment)
        for x in range(len(monsterMash)):
            if x == 0:
                pythong = monsterMash[x].split('=')[1].split('\n')[0]
            elif x ==1:
                cshapener = monsterMash[x].split('=')[1].split('\n')[0]
            elif x ==2:
                pywan = monsterMash[x].split('=')[1].split('\n')[0]
            elif x ==3:
                shellow = monsterMash[x].split('=')[1].split('\n')[0]


    if mrCheckerMan(bobington(rootOfAllEvil, csharpener)):
        os.remove(bobington(rootOfAllEvil, csharpener))

    if mrCheckerMan(bobington(rootOfAllEvil, pythong)):
        print("file's already there")

    else:
        builderOfMen(bobington(rootOfAllEvil,pythong), pywan )
    
    









def theFunctionThatDoesEverything():
    weGood()


theFunctionThatDoesEverything()